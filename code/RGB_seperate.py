import cv2 as cv
import sys

img = cv.imread('cat.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Org RGB',img)
cv.imshow('Upper left half', img[0:img,shape[0]//2, 0:img.shape[1]//2,: ]) # 세로, 가로 BGR 채널 전부 
cv.imshow('Center half', img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4,:])

cv.imshow("R 채널", img[:,:,2])
cv.imshow("G 채널", img[:,:,1])
cv.imshow("B 채널", img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()