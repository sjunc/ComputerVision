import cv2 as cv 
import sys

img=cv.imread('cat.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.rectangle(img, (50, 40), (205, 100), (0,0,255), 2) # 직사각형 그리기 좌상단, 우하단 색상, 굵기 
cv.putText(img,'20202384', (50, 24), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2) # 글씨 적기

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()