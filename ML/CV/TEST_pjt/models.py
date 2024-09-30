import os
import sys
import torch
import importlib.util
import requests 

def download_file(url, dest):
    if not os.path.exists(dest):
        print(f"Downloading {url}...")
        response = requests.get(url)
        with open(dest, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {dest}")
    else:
        print(f"{dest} already exists.")

def download_models():
    os.makedirs("weights", exist_ok=True)
    # AnimeGAN2 모델 가중치 다운로드
    download_file("https://github.com/bryandlee/animegan2-pytorch/archive/refs/heads/master.zip", "weights/animegan2_pytorch.zip")
    download_file("https://github.com/bryandlee/animegan2-pytorch/releases/download/v2.0/face_paint_512_v1.pt", "weights/face_paint_512_v1.pt")
    download_file("https://github.com/bryandlee/animegan2-pytorch/releases/download/v2.0/face_paint_512_v2.pt", "weights/face_paint_512_v2.pt")
    download_file("https://github.com/bryandlee/animegan2-pytorch/releases/download/v2.0/paprika.pt", "weights/paprika.pt")

    # Dlib 모델 다운로드
    download_file("http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2", "shape_predictor_68_face_landmarks.dat.bz2")
    # Dlib 모델 압축 해제
    if not os.path.exists("shape_predictor_68_face_landmarks.dat"):
        import bz2
        with bz2.open("shape_predictor_68_face_landmarks.dat.bz2", "rb") as f_in:
            with open("shape_predictor_68_face_landmarks.dat", "wb") as f_out:
                f_out.write(f_in.read())
        print("Dlib model extracted.")


def load_model(model_path, device):
    # 현재 파일의 위치를 기준으로 절대 경로를 생성하여 모듈 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(current_dir, 'weights', 'animegan2_pytorch', 'model.py')
    
    # 모듈을 동적으로 로드
    spec = importlib.util.spec_from_file_location("model", model_dir)
    model_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model_module)
    
    # Generator 클래스 사용
    Generator = model_module.Generator
    
    model = Generator()
    checkpoint = torch.load(model_path, map_location=device)
    model.load_state_dict(checkpoint)
    model.to(device).eval()
    
    return model




