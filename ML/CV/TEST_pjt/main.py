import os
from fastapi import FastAPI, UploadFile, HTTPException
from confluent_kafka import Producer
import json
from deepface import DeepFace
import numpy as np
import cv2
import dlib
from models import download_models  # 모델 다운로드 함수 가져오기
from db import get_db_connection

# Kafka 서버 주소 환경 변수로부터 가져오기
KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'localhost:9092')

# Kafka 프로듀서 설정
producer_config = {
    'bootstrap.servers': KAFKA_SERVER  # Kafka 서버 주소
}
producer = Producer(producer_config)

# Kafka 메시지 전달 보고 함수
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# 전역 변수로 모델 로드
model = None
detector = None
device = None  # 사용할 장치 (cuda 또는 cpu)

# FastAPI 인스턴스 생성
app = FastAPI()

# 서버 시작 시 모델 로드
@app.on_event("startup")
def load_models():
    global model, detector, device
    print("Loading models...")

    # 필요한 모델 다운로드
    download_models()

    # 얼굴 인식 모델 로드 (Facenet 사용)
    model = DeepFace.build_model("Facenet")
    print("Facenet model loaded successfully.")
    
    # dlib 얼굴 검출기 및 랜드마크 예측기 로드
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    print("Dlib models loaded successfully.")

# 회원 등록 API
@app.post("/register/")
async def register_user(name: str, files: list[UploadFile]):
    try:
        # 3장의 사진을 필수로 받도록 설정
        if len(files) < 3:
            raise HTTPException(status_code=400, detail="You must upload exactly 3 images.")

        images = [await file.read() for file in files]
        if not images or len(images) < 3:
            raise HTTPException(status_code=400, detail="Invalid number of images uploaded.")

        vectors = []
        for img in images:
            # 이미지 파일을 numpy 배열로 변환
            nparr = np.frombuffer(img, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # 얼굴 검출 및 벡터 추출
            gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)
            if not faces:
                print("No faces detected in one of the images.")
                continue

            for face in faces:
                face_img = img_np[max(face.top(), 0):min(face.bottom(), img_np.shape[0]), 
                                  max(face.left(), 0):min(face.right(), img_np.shape[1])]
                if face_img.size == 0:
                    print("Face area extraction failed.")
                    continue

                embedding = DeepFace.represent(face_img, model_name='Facenet', enforce_detection=False)[0]["embedding"]
                vectors.append(embedding)

        if not vectors:
            raise HTTPException(status_code=400, detail="No faces detected in the uploaded images.")

        # 벡터 데이터를 Kafka로 전송
        message = {
            'name': name,
            'vectors': vectors
        }
        producer.produce('face_recognition', key=name, value=json.dumps(message), callback=delivery_report)
        producer.flush()  # 메시지 전송을 보장하기 위해 flush 호출

        # 데이터베이스 연결 및 저장
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, vectors) VALUES (%s, %s)", 
                       (name, json.dumps(vectors)))
        conn.commit()
        cursor.close()
        conn.close()

        return {"status": "User registered successfully", "vectors": vectors}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# 얼굴 인식 및 회원 정보 반환 API
@app.post("/recognize/")
async def recognize_faces(file: UploadFile):
    try:
        # 업로드된 이미지 읽기 및 numpy 배열로 변환
        image = await file.read()
        nparr = np.frombuffer(image, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # DeepFace를 이용한 얼굴 검출 및 임베딩 추출
        detected_faces = DeepFace.extract_faces(img_np, detector_backend='retinaface', enforce_detection=False)
        if not detected_faces:
            raise HTTPException(status_code=400, detail="No faces detected in the image.")

        recognized_users = []

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, vectors FROM users")
        users = cursor.fetchall()

        for face in detected_faces:
            face_vector = DeepFace.represent(face["face"], model_name='Facenet', enforce_detection=False)[0]["embedding"]
            max_similarity = 0
            best_match_name = None

            for user in users:
                user_name, user_vectors = user
                vectors = json.loads(user_vectors)
                
                for vector in vectors:
                    # 코사인 유사도를 사용하여 얼굴 벡터 비교
                    similarity = np.dot(face_vector, vector) / (np.linalg.norm(face_vector) * np.linalg.norm(vector))
                    if similarity > max_similarity and similarity > 0.8:
                        max_similarity = similarity
                        best_match_name = user_name

            recognized_users.append(best_match_name)

        cursor.close()
        conn.close()

        return {"recognized_users": list(set(recognized_users))}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
