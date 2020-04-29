#이미지를 대상으로하는 머신러닝
#머신러닝 개선힌트
#손글씨 숫자인식에 사용한 데이터셋은 UCI가 공개한 간단한 이미지 세트
#손글씨 숫자 데이터셋으로는 MNIST라는 데이터셋이 유명함 이데이터셋은 7만개의 손글씨 숫자를 제공
#http://yann.lecun.com/exdb/mnist/
#이미지 데이터 머신러닝시에는 이미지크기와, 색공간 형식 통일 및 이미지를 전처리 해야함 
#이미지를 일정한크기로 변환후 색공간을 맞춰야함


#윤곽검출 엽서의 우편번호 인식하기
#사용기술 opencv,물체인식,문자인식
#opencv로 간단하게 이미지 윤곽검출하는 기능만들기
#open cv의 findContours()함수를 사용함
#find_contours.py

import cv2
import matplotlib.pyplot as plt

#이미지 읽어 들이고 크기변경하기
img = cv2.imread("flower.jpg")
img = cv2.resize(img, (300,169))

#색 공간 변경하기
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7,7),0)
im2 = cv2.threshold(gray, 140, 240, cv2.THRESH_BINARY_INV)[1]

#화면 왼족에 변환한 이미지 출력하기
plt.subplot(1,2,1)
plt.imshow(im2, cmap="gray")

#윤곽 검출하기
cnts = cv2.findContours(im2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]

#검출한 윤곽그리기
for pt in cnts:
    x,y,w,h = cv2.boundingRect(pt)

    #너무 크거나 작은 부분 제거하기
    if w < 30 or w > 200: continue
        print(x,y,w,h) #결과 출력하기
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2 )
        
#화면 오른쪽에 결과 출력하기
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.savefig("find_contours.png", dpi=200)
plt.show()


