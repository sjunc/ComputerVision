import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
frames = []
while True:
    ret, frame = cap.read()
    
    if not ret:
        print('프레임 획득에 실패해 루프를 나갑니다.')
        break 
    cv.imshow('Video display', frame)
    
    key = cv.waitKey(1)
    if key == ord('c'):   # 'c'키가 들어오면 프레임을 리스트에 추가 
        frames.append(frame)
    elif key == ord('q'): # 'q'키가 들어오면 루프를 빠져나감
        break

cap.release()               # 카메라와 연결을 끊음
cv.destroyAllWindows()

if len(frames) > 0:       #만약 캡쳐한 프레임이 있으면
    imgs = frames[0]    # 이걸 이미지로 두고
    for i in range(1, min(3, len(frames))): # 최대 3장까지 가로로 이어 붙여서
        imgs = np.hstack((imgs, frames[i]))   # 이미지를 수평방향으로 붙임. 
        
    cv.imshow('collected images', imgs)
    
    cv.waitKey()
    cv.destrotyAllWindows()