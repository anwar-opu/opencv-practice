import cv2 as cv

img = cv.imread('images/park.jpg')

cv.imshow('park', img)

# Converting to grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('park gray', gray)

# blur image
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# bilateral = cv.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
# cv.imshow('Bilateral Blur', bilateral)

# Edge Concode
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', canny)

# dilated the image
dilated = cv.dilate(canny, (7,7), iterations=5)
cv.imshow('dilated', dilated)

# eroded 
eroded = cv.erode(dilated, (7,7), iterations=5)
cv.imshow('Eroded', eroded)

# Resize
resize = cv.resize(img,(500,500))
cv.imshow('Resize', resize)

resize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize with interpolation ', resize)

# Cropping img[y1:y2, x1:x2]
# (0,0) --------> x (width)
#   |
#   |
#   |
#   v
#   y (height)

cropped = img[50:200, 200:500]
cv.imshow("Cropped image", cropped)

cv.waitKey(0)