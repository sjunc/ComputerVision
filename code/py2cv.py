import sys
import cv2 as cv 

img = cv.imread('soccer.jpg') #imread image read

if img is None: 
    sys.exit('file not founded') # 1초 = 1000ms 20초 20000 ms

print(img[0,0])
print(img[0,0,0], img[0,0,1], img[0,0,2])




cv.imshow('Image Display', img) # 윈도우에 영상 표시
cv.waitKey() # 키보드 입력 대기 0 ()공란: 무한정 대기
cv.destroyAllWindows() # 창 종료 