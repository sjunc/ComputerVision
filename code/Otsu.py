import cv2 as cv
import sys
import matplotlib.pyplot as plt


img = cv.imread('cat.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

t, bin_img = cv.threshold(img[:,:,2],0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print("오츄 알고리즘이 찾은 최적 임계값 ", t)

cv.imshow('R channel', img[:,:,2])
cv.imshow('R channel binarization', bin_img)

cv.waitKey()
cv.destroyAllWindows()
