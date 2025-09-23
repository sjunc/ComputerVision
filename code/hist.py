import cv2 as cv
import sys
import matplotlib.pyplot as plt


img = cv.imread('cat.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
h = cv.calcHist([img], [2], None, [256], [0,256]) # 2번 채널인 R 채널에서 히스토그램 구함
plt.plot(h, color = 'r', linewidth = 1)

