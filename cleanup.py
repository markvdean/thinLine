import os
import numpy as np
import cv2
cap = cv2.VideoCapture('working_files\source_videos\FORWEB2_1 - Copy.mp4')
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count = 0
w1 = cap.get(3)
w2 = w1
h = cap.get(4)
if w1%2 == 0: w1 = w1/2
else: w = w1/2 - 0.5
if w2%2 == 0: w2 = w2/2 + 1
else: w = w2/2 + 0.5
w1 = int(w1)
w2 = int(w2)
h = int(h)
while cap.isOpened():
    ret, frame = cap.read()
    if count != 0 and count != 1:
        frameCropped = frame[w1:h, 0:w2]
        frameConjoined = cv2.hconcat([frameConjoined, frameCropped])
    elif count == 1:
        outputIMG = cv2.imread("working_files/output_image/output.png")
        frameCropped = frame[w1:h, 0:w2]
        frameConjoined = cv2.hconcat([outputIMG, frameCropped])
    else:
        frameCropped = frame[w1:h, 0:w2]
        cv2.imwrite("working_files/output_image/output.png", frameCropped)
    if ret is False:
        print("done!")
        break
    count += 1
    print(count, "of", total)   
cv2.imwrite("working_files/output_image/output.png", frameConjoined)
print("complete")
cap.release()