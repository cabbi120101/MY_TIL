import os
import torch

# 다운로드한 모델 파일 경로를 지정하세요
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "weights", "face_paint_512_v1.pt")

try:
    checkpoint = torch.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")
