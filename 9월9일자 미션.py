import cv2
import numpy as np

# 초기 설정
drawing = False  # 그리기 여부
mode = 0  # 0: 다각형, 1: 원
ix, iy = -1, -1
points = []
img = np.zeros((512, 512, 3), np.uint8)

# 마우스 이벤트 콜백 함수
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        mode = 0
        points = [(x, y)]
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        mode = 1
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode == 0:
                cv2.line(img, (ix, iy), (x, y), (0, 255, 0), 2)
                ix, iy = x, y
                points.append((x, y))
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 0:
            cv2.polylines(img, [np.array(points)], True, (0, 255, 0), 2)
            points = []
        mode = -1

# 창 생성 및 마우스 이벤트 연결
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('   
s'):
        # 이미지 저장 (원하는 경로 지정)
        cv2.imwrite('image.png', img)
    elif k == ord('r'):
        # 리사이징 및 필터링 (예시)
        resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
        blurred = cv2.GaussianBlur(resized, (5, 5), 0)
        cv2.imshow('resized', blurred)
    elif k == 27:
        break

cv2.destroyAllWindows()
