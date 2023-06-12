import cv2
import keyboard


# Задание 1
img = cv2.imread('variant-3.jpeg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('hsv', hsv)
k = cv2.waitKey(3) & 0xFF

keyboard.wait("enter")


# Задание 2
cap = cv2.VideoCapture(0)



cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    i = 0
    ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Задание 3

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if i % 5 == 0:
            a = x + (w // 2)
            b = y + (h // 2)
            if (405 > a > 205) and (305 > b > 105):
                print('goal')
            else:
                print('outside')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
