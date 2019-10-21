import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret is True:
        cv2.imshow('frame', frame)
        grey = cv2.GaussianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (7, 7), 1)
        cv2.imshow('grey', grey)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
