import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/park.jpg')
cv.imshow('orginal image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray image', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# only used for visualize the masked region 
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('mask', masked)

# grayscale histogram 
# gray_hist = cv.calcHist([gray],[0], mask, [256], [0,256] )

# plt.figure()
# plt.title("grayscale histogram")
# plt.xlabel('Bins')
# plt.ylabel(" # of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# color histogram
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate (colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)