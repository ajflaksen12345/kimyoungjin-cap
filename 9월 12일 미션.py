import cv2
import os
import random
from PIL import Image

def data_augmentation(img_path, save_path, class_name):
    """
    데이터 증식 함수

    Args:
        img_path (str): 이미지 파일 경로
        save_path (str): 증식된 이미지 저장 경로
        class_name (str): 클래스 이름
    """

    # 이미지 로드
    img = cv2.imread(img_path)

    # 이미지 크기 조절
    img = cv2.resize(img, (224, 224))

    # 파일 이름 생성 함수
    def generate_filename(original_filename, modification):
        return f"{os.path.splitext(original_filename)[0]}_{modification}{os.path.splitext(original_filename)[1]}"

    # 원본 이미지 저장
    cv2.imwrite(os.path.join(save_path, generate_filename(os.path.basename(img_path), "")), img)

    # 회전
    for angle in range(10, 31, 5):
        rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 시계 방향 90도 회전 (예시)
        cv2.imwrite(os.path.join(save_path, generate_filename(os.path.basename(img_path), f"rot_{angle}")), rotated_img)

    # 좌우 반전
    flipped_img = cv2.flip(img, 1)
    cv2.imwrite(os.path.join(save_path, generate_filename(os.path.basename(img_path), "hflip")), flipped_img)

    # 상하 반전
    flipped_img = cv2.flip(img, 0)
    cv2.imwrite(os.path.join(save_path, generate_filename(os.path.basename(img_path), "vflip")), flipped_img)

    # 임의 크기 자르기 (예시)
    cropped_img = img[30:194, 30:194]  # 이미지 중앙 부분 자르기
    cv2.imwrite(os.path.join(save_path, generate_filename(os.path.basename(img_path), "resize")), cropped_img)

# 사용 예시
img_dir = "images"  # 이미지 파일이 있는 디렉토리
save_dir = "augmented_images"  # 증식된 이미지를 저장할 디렉토리
class_name = "jelly"

# 저장 디렉토리 생성
os.makedirs(save_dir, exist_ok=True)

# 각 이미지에 대해 데이터 증식 수행
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(img_dir, filename)
        data_augmentation(img_path, save_dir, class_name)
