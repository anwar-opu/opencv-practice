import cv2 as cv
import numpy as np

img = cv.imread("images/cat.jpg")

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# canny = cv.Canny(img, 125,175)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow('draw contours', blank)

cv.waitKey(0)