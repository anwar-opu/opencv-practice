import cv2 as cv

img = cv.imread('images/park.jpg')
cv.imshow('Orginal', img)


# BGR to Gray 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# RGB to BGR 
bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('BGR', bgr)

cv.waitKey(0)
cv.destroyAllWindows()