import cv2 as cv

# capture = cv.VideoCapture(0)

while True:
    # isTrue, frame = capture.read()
    frame = cv.imread('original images/image 1.jpg')

    if frame is None:
        print("Error: Could not read the image.")
        break

    frame_resized = cv.resize(frame, (640, 480), interpolation=cv.INTER_AREA)
    frame_bw = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
    frame_denoise = cv.medianBlur(frame_bw, ksize=5)
    frame_edges = cv.Canny(frame_denoise, 100, 200)

    cv.imwrite('processed images/resized_frame.png', frame_resized)
    cv.imwrite('processed images/black_and_white_frame.png', frame_bw)
    cv.imwrite('processed images/edges_detection_frame.png', frame_edges)
    cv.imwrite('processed images/denoise_frame.png', frame_denoise)

    cv.imshow('Normal', frame)
    cv.imshow('Resized', frame_resized)
    cv.imshow('Black and White', frame_bw)
    cv.imshow('Edges', frame_edges)
    cv.imshow('Denoise', frame_denoise)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# capture.release()
cv.destroyAllWindows()
