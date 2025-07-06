import cv2 as cv

img = cv.imread("images/park.jpg")
cv.imshow('orginal img', img)

# averaging 
average = cv.blur(img, (3,3))
cv.imshow('Average blur', average)

# gaussian blur
# 0: SigmaX (standard deviation in the X-axis).
gaussian_blur = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian blur', gaussian_blur)

# median blur 
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# bilateral

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral image', bilateral)

cv.waitKey(0)