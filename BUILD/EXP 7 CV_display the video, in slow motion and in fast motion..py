import cv2

# Open video
cap = cv2.VideoCapture(r"C:\Users\Yavan\Downloads\road cross cv.mp4")

# Initial speed (Normal)
delay = 30

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Player", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('s'):
        delay = 100      # Slow Motion
        print("Slow Motion")

    elif key == ord('f'):
        delay = 10       # Fast Motion
        print("Fast Motion")

    elif key == ord('n'):
        delay = 30       # Normal Motion
        print("Normal Motion")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
