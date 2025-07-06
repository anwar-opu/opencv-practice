import cv2 as cv
import numpy as np

img = cv.imread('images/park.jpg')
cv.imshow('orginal', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blank', blank)

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

mergerd = cv.merge([b,g,r])
cv.imshow("Mergerd img", mergerd)

cv.waitKey(0)
cv.destroyAllWindows()