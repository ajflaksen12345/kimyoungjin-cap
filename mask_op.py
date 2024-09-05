import cv2, sys

#이미지 불러오기 
img = cv2.imread('data2/opencv-logo-white.png',cv2.IMREAD_UNCHANGED)
dst = cv2.imread('data2/cat/bmp')
# 모든 행, 모든 열, 0~2번채널
src = img[:,:,0:3]
# 알파채널만 슬라이싱 
mask = img[:,:,3]
#print(mask.shape)


# # 마스크 연산
# cv2.copyTo(src,mask,d
# st)

# cv2.imshow('img', dst)
# cv2 waitkey()
