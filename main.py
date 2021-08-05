import cv2 as c
import numpy as np


#img = c.imread('img/chb.jpg')
#c.imshow('img', img)
#c.waitKey(0)


e = True
cap = c.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)


while True:
    success,img = cap.read()
    new = img #c.resize(img, (int(img.shape[1] * 1.5) ,img.shape[0]))
    new = c.cvtColor(new, c.COLOR_BGR2GRAY)
    new = c.Canny(new, 90 ,90)
    new = c.flip(new, 0)
    c.imshow('h',new)

    if c.waitKey(1) & 0xFF == ord('q'):
        break
#