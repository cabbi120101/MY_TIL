import os
import torch
import numpy as np 
from torchvision import transforms
from PIL import Image
from models import load_model  # AnimeGAN2 모델 로드 함수

def load_anime_model(weight_file="weights/face_paint_512_v1.pt"):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = load_model(weight_file, device)
    return model, device

def make_anime(image: np.ndarray, model, device):
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    input_tensor = transform(image_pil).unsqueeze(0).to(device)

    with torch.no_grad():
        output_tensor = model(input_tensor)[0]

    output_image = transforms.ToPILImage()(output_tensor.cpu().squeeze())
    output_image_np = cv2.cvtColor(np.array(output_image), cv2.COLOR_RGB2BGR)

    return output_image_np
