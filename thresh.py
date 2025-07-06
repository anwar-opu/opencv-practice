import cv2 as cv

img = cv.imread('images/park.jpg')
cv.imshow('orginal image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholading

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('simple thresholded', thresh)
print(threshold)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded inverse', thresh_inv)
print(threshold)

# Adaptive thresholding 

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 5)
cv.imshow('Adaptive thresholding ', adaptive_thresh)


cv.waitKey(0)