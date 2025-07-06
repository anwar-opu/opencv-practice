import cv2 as cv

img = cv.imread('images/cat.jpg')
cv.imshow('cat', img)

def rescaleFrame(frame, scale=0.75):
    # image, video and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# resize_image = rescaleFrame(img)
# cv.imshow('cat_resize', resize_image)

def changesRes(width,height):
    # live video
    capture.set(3,width)
    capture.set(4,height)

# reading video
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break  # Stop if video ends or can't read frame

    frame_resize = rescaleFrame(frame, scale=0.2)

    cv.imshow('video', frame)
    cv.imshow('video_resize', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
