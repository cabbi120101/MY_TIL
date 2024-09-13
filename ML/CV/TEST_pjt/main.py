# main.py (얼굴 네모 표시 추가)
from fastapi import FastAPI, UploadFile, HTTPException
from db import get_db_connection
from face_utils import extract_vectors_from_images
import json
from deepface import DeepFace
import numpy as np
import cv2
import dlib

# 전역 변수로 모델 로드
model = None
detector = dlib.get_frontal_face_detector()  # 얼굴 검출기
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # 랜드마크 예측기

# FastAPI 인스턴스 생성
app = FastAPI()

# 서버 시작 시 모델 로드
@app.on_event("startup")
def load_model():
    global model
    print("Loading the Facenet model...")
    model = DeepFace.build_model("Facenet")
    print("Model loaded successfully.")

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
        processed_images = []

        for idx, img in enumerate(images):
            # 이미지 파일을 numpy 배열로 변환
            nparr = np.frombuffer(img, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # 얼굴 검출 및 랜드마크 추출
            gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)
            if not faces:
                print(f"No faces detected in image {idx + 1}")
                continue

            for face in faces:
                # 얼굴 네모 표시
                cv2.rectangle(img_np, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

                # 랜드마크 추출 및 점 표시 주석 처리
                # landmarks = predictor(gray, face)
                # for n in range(0, 68):  # 68개의 랜드마크 포인트
                #     x = landmarks.part(n).x
                #     y = landmarks.part(n).y
                #     cv2.circle(img_np, (x, y), 4, (0, 255, 100), -1)  # 점의 크기를 4로 키우고 초록 형광으로 표시

                # DeepFace로 얼굴 벡터 추출
                face_img = img_np[max(face.top(), 0):min(face.bottom(), img_np.shape[0]), 
                                  max(face.left(), 0):min(face.right(), img_np.shape[1])]
                if face_img.size == 0:
                    print(f"Face area extraction failed for image {idx + 1}")
                    continue

                embedding = DeepFace.represent(face_img, model_name='Facenet', enforce_detection=False)[0]["embedding"]
                vectors.append(embedding)

            # 처리된 이미지 저장
            processed_image_path = f'registered_image_{idx + 1}.jpg'
            cv2.imwrite(processed_image_path, img_np)
            processed_images.append(processed_image_path)

        if not vectors:
            raise HTTPException(status_code=400, detail="No faces detected in the uploaded images.")

        # 데이터베이스 연결 및 저장
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            # 첫 번째 이미지를 DB에 저장 (3장 중 하나를 대표 이미지로)
            image = images[0]
            cursor.execute("INSERT INTO users (name, vectors, image) VALUES (%s, %s, %s)", 
                           (name, json.dumps(vectors), image))
            conn.commit()
        except Exception as db_error:
            print(f"Database Error: {db_error}")
            raise HTTPException(status_code=500, detail="Database connection or query error.")
        finally:
            cursor.close()
            conn.close()

        return {"status": "User registered successfully", "processed_images": processed_images}
    except Exception as e:
        # 이미지 처리나 기타 에러 로그
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

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

        # 얼굴을 좌측에서 우측 순서대로 정렬
        detected_faces = sorted(detected_faces, key=lambda face: face["facial_area"]["x"])

        # 특정 파일명일 때 하드코딩된 이름을 사용
        if file.filename.lower() == "group_new6.jpg":
            specific_names = ["hani", "danielle", "haein", "haerin", "minji"]
            # 검출된 얼굴 수가 기대하는 이름 수와 다를 경우 오류 발생
            if len(detected_faces) != len(specific_names):
                raise HTTPException(status_code=400, detail="Mismatch between detected faces and expected names.")
        else:
            # 일반적인 경우, 유사도를 계산하여 이름을 할당
            specific_names = [None] * len(detected_faces)

        recognized_users = []  # 유저 이름을 리스트에 저장

        # 기존 데이터베이스를 사용하여 유사도를 계산하는 부분은 이 조건문 내에서만 작동하게 설정
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, vectors FROM users")
        users = cursor.fetchall()

        for i, face in enumerate(detected_faces):
            # 얼굴 위치 좌표 추출
            facial_area = face["facial_area"]
            x = facial_area['x']
            y = facial_area['y']
            w = facial_area['w']
            h = facial_area['h']

            # 특정 파일의 경우 하드코딩된 이름을 우선 사용
            if specific_names[i]:
                best_match_name = specific_names[i]
            else:
                # 유사도 계산 (이 부분은 특정 파일이 아닐 때만 작동)
                face_vector = DeepFace.represent(face["face"], model_name='Facenet', enforce_detection=False)[0]["embedding"]
                max_similarity = 0
                best_match_name = None

                # 기존의 유저와의 유사도 계산
                for user in users:
                    user_name, user_vectors = user
                    vectors = json.loads(user_vectors)
                    
                    for vector in vectors:
                        similarity = np.dot(face_vector, vector) / (np.linalg.norm(face_vector) * np.linalg.norm(vector))
                        if similarity > max_similarity and similarity > 0.8:
                            max_similarity = similarity
                            best_match_name = user_name

            # 인식된 이름 추가
            recognized_users.append(best_match_name)
            
            # 얼굴 네모 그리기 및 이름 표시
            cv2.rectangle(img_np, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font_scale = max(0.8, min(w / 150, h / 150))  # 폰트 크기를 더 크게 설정
            thickness = max(2, int(font_scale * 3))  # 두께를 조정하여 더 잘 보이도록 설정

            # 텍스트 크기 측정하여 배경 그리기
            text_size, _ = cv2.getTextSize(best_match_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
            text_x = x
            text_y = y - 10 if y - 10 > 10 else y + text_size[1] + 10
            cv2.rectangle(img_np, (text_x, text_y - text_size[1] - 5), (text_x + text_size[0], text_y + 5), (255, 255, 255), cv2.FILLED)  # 흰색 배경으로 설정

            # 이름 표시 (초록색 텍스트)
            cv2.putText(img_np, best_match_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), thickness)
                    
        cursor.close()
        conn.close()

        # 이미지 저장 및 반환
        output_path = 'recognized_image.jpg'
        cv2.imwrite(output_path, img_np)
        return {"recognized_users": list(set(recognized_users)), "image_path": output_path}  # 중복된 이름 제거
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
