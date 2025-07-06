import cv2 as cv

# image show -
# img  = cv.imread('images/cat.jpg')

# cv. imshow('cat', img)

# cv.waitKey(0)
# cv.destroyAllWindows()

# video show -

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) &0xFF==ord('d'):
        break

capture.release()
cv.destoryAllWindows()