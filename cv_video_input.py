import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if ret == False:
        continue
    
    cv2.imshow("Video", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()