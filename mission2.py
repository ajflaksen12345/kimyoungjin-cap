import cv2, sys
import matplotlib.pyplot as plt
import numpy as np

# 파일 불러오기
# src1 파일을 src2 파일처럼 만들기
src1 = cv2.imread("C:/Users/SBA/opencvDojang/misson/03.png")
src2 = cv2.imread("C:/Users/SBA/opencvDojang/misson/misson_image03.png")

# 예외처리
if src1 is None or src2 is None:
    sys.exit('image load failed')

# 하늘 부드럽게
dst1 = cv2.fastNlMeansDenoisingColored(src1, None, 8, 10, 7, 21)

# bilateralFilter
dst2 = cv2.bilateralFilter(dst1, -1, 10, 5)
# 밝기를 좀 높여주기
dst3 = cv2.add(dst2, (10, 10, 10))



cv2.imshow('dst3', dst2)
cv2.imshow('src1', src2)
cv2.waitKey()
cv2.destroyAllWindows()
