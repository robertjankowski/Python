import cv2
import numpy as np

'''
hue is mapped -> 0-359 degrees as [0-179]
saturation is mapped -> 0-100 degrees as [0-255]
value is 0-255
'''
# detecting green object
lower_bound = np.array([33, 80, 40])
upper_bound = np.array([102, 255, 255])

cam = cv2.VideoCapture(0)

kernel_open = np.ones((5, 5))
kernel_close = np.ones((20, 20))

while True:
    rec, img = cam.read()
    img = cv2.resize(img, (600, 400))

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, lower_bound, upper_bound)

    mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
    mask_close = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_close)

    mask_final = mask_close

    img_hsv, conts, _ = cv2.findContours(mask_final.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
    for i in range(len(conts)):
        x, y, w, h = cv2.boundingRect(conts[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('mask_close', mask_close)
    cv2.imshow('mask_open', mask_open)
    cv2.imshow('mask', mask)
    cv2.imshow('cam', img)
    k = cv2.waitKey(10)
    if k == 27:
        break
