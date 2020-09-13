import os
import numpy
import cv2
cap = cv2.VideoCapture('working_files\source_videos\DJI_0485_Trim_2.mp4')
count = 0
while cap.isOpened():
    frame = cap.read()
    h, w, c = frame.shape
    if w % 2 == 0:
        w1 = w/2 - 1
        w2 = w/2
    else:
        w1 = w/2 - 0.5
        w2 = w/2 + 0.5
    if count != 0 and count != 1:
        frameCropped = frame[0:w1, 0:w2]
    elif frame == 1:
        outputIMG = "working_files/output_image/output.png"
        frameCropped = frame[0:w1, 0:w2]
    else:
        frame.save("working_files/output_image/output.png", format="png")
    try: cv2.imshow('preview', outputIMG)
    except: break
    count += 1

cap.release()
cv2.destroyAllWindows() # destroy all opened windows