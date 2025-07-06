import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# 1. print the image a certain color
# Set entire image to red (BGR: 0, 0, 255)
# blank[200:300, 300:400] = 0, 0, 255

# cv.imshow('Red', blank)

# 2. draw rectangle

# cv.rectangle(blank, (30,10),(250,250),(0,255,255),thickness=2)
# cv.imshow('Rectangle', blank)

# 3. draw a circle
# blank[:] = 0, 255, 0 

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# 4. line draaw
# cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(225,255,225),thickness=2)
# cv.imshow('line', blank)

# write a text on an image
cv.putText(blank,'hello',(255,255), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0), thickness=2 )
cv.imshow('text', blank)
cv.waitKey(0)
cv.destroyAllWindows()


