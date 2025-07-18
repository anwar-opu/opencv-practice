import cv2 as cv
import numpy as np
img = cv.imread('images/park.jpg')
cv.imshow('orginal', img)

# translation
# img.shape[1] → width
# img.shape[0] → height

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down
translated = translate(img,0,100)
cv.imshow('translated image', translated)


# Rotation
def rotate(img, angle,rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1.0)
    dimenstions = (width,height)

    return cv.warpAffine(img,rotMat,dimenstions)

rotated = rotate(img, -45)
cv.imshow('rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow("rotated rotated", rotated_rotated)

# Resizing 
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resize)

# filpping
flipping = cv.flip(img, -1)
cv.imshow("filpping", flipping)

# cropping 
cropped = img[200:400 , 300:400] 
cv.imshow("cropped", cropped)

cv.waitKey(0)