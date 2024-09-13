# face_utils.py
import cv2
from deepface import DeepFace
import numpy as np

def extract_vectors_from_images(images, model):
    vectors = []
    for img in images:
        # 이미지 파일을 numpy 배열로 변환
        nparr = np.frombuffer(img, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # 얼굴을 검출하고 벡터화
        try:
            detected_faces = DeepFace.extract_faces(img_np, detector_backend='retinaface', enforce_detection=False)
            if detected_faces:
                for face in detected_faces:
                    # 이미 로드된 모델 사용하여 벡터 추출 (모델을 전달하지 않음)
                    embedding = DeepFace.represent(face["face"], model_name='Facenet', enforce_detection=False)[0]["embedding"]
                    vectors.append(embedding)
            else:
                print("No faces detected in the image.")
        except Exception as e:
            print(f"Error in extracting faces or vectors: {e}")
    return vectors
