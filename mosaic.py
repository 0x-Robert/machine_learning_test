#OPENCV로 모자이크 처리하기
#OpenCV에는 흐림 효과 또는 테두리 검출과 같은 필터함수가 있지만 모자이크 처리를 하는 함수는 없음 모자이크 처리하는
#함수를 mosaic()이라는 이름으로 정의하고 mosaic.py라는 모듈파일로 만들기

import cv2

def mosaic(img, rect, size):
    #모자이크 적용할 부분 추출하기
    (x1,y1,x2,y2) = rect
    w = x2 -x1
    h = y2 -y1
    i_rect = img[y1:y2, x1:x2]
    #축소하고 확대하기
    i_small = cv2.resize(i_rect,(size, size))
    i_mos = cv2.resize(i_small, (w,h), interpolation=cv2.INTER_AREA)
    
    #모자이크 적용
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2



