import cv2 as cv
import sys

cap = cv.VideoCapture(0,cv.CAP_DSHOW)  #  카메라 번호 0 카메라 하나 카메라와 연결 시도

#CAP_DSHOW: 웹캠 화면을 화면에 바로 표시하기 

if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
while True: # 동영상 입력을 위해 무한 반복 
    ret, frame = cap.read() # READ로 프레임 읽어옴. 첫번째는 성공 여부, 두번째는 프레임 내용
    
    if not ret: # 만약 프레임 얻는데 실패하면 영상 내보내는 것 종료
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow('Video display', frame)   # 잘되면 화면에 표시 
    
    key = cv.waitKey(500) #1 밀리초 동안 키보드 입력 기다림 늘리면 끊어지는 이미지
    if key == ord('q'): # q 키 들어오면 루프를 빠져 나감 
        break

cap.release()
cv.destroyAllWindows()