import numpy as np
import sys
import cv2 as cv 

a = np.array([4, 5, 0, 1, 2, 3, 6, 7, 9, 8, 10, 11])
print(a)
print(type(a))
print(a.shape)
a.sort()
print(a)

b = np.array([-4.3, -2.3, 12.9, 8.99, 10.1, -1.2])
b.sort()
print(b)

c = np.array(['one', 'two', 'three', 'four', 'five', 'seven', 'six'])
c.sort()
print(c)

type(c)
dir(c) # 사용 가능한 멤버 함수를 알려주는 함수
help(c.sort) # 함수가 하는 일에 대한 설명을 해주는 함수
img = cv.imread('soccer.jpg') #imread image read

if img is None: 
    sys.exit('file not founded') # 1초 = 1000ms 20초 20000 ms

print(img[0,0])
print(img[0,0,0], img[0,0,1], img[0,0,2])




cv.imshow('Image Display', img) # 윈도우에 영상 표시
cv.waitKey() # 키보드 입력 대기 0 ()공란: 무한정 대기
cv.destroyAllWindows() # 창 종료 