import cv2 as cv

# capture = cv.VideoCapture(0)


while True:
    # isTrue, frame = capture.read()
    frame = cv.imread('images/image 1.jpg')

    frame_resized = cv.resize(frame, (640, 480), interpolation=cv.INTER_AREA)
    frame_bw = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
    frame_denoise = meidanblur_img = cv.medianBlur(frame_resized, ksize=5)
    frame_edges = cv.Canny(frame_resized, 125, 175)

    cv.imwrite('images/black and white.png', frame_bw)

    cv.imshow('Normal', frame)
    # cv.imshow('Resized', frame_resized)
    # cv.imshow('Black and White', frame_bw)
    # cv.imshow('Edges', frame_edges)
    # cv.imshow('Denoise', frame_denoise)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# capture.release()
cv.destroyAllWindows()
