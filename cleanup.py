import os
import numpy as np
import cv2, png
cap = cv2.VideoCapture('working_files\source_videos\FORWEB2_1 - Copy.mp4')
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    try: 
        h, w, c = frame.shape
        if w%2 == 0: w = w/2
        else: w = w/2 + 0.5
        h = int(h)
        w = int(w)
        if count != 0 and count != 1:
            frameCropped = frame[0:h, 0:w]
            frameConjoined = cv2.hconcat([frameConjoined, frameCropped])
        elif count == 1:
            outputIMG = cv2.imread("working_files/output_image/output.png")
            frameCropped = frame[0:h, 0:w]
            frameConjoined = cv2.hconcat([outputIMG, frameCropped])
        else:
            frameCropped = frame[0:h, 0:w]
            cv2.imwrite("working_files/output_image/output.png", frameCropped)
        if ret is False:
            print("done!")
            break
        count += 1
        print(count, "of", total)
    except:
        print("an error happened but this is normal if all the frames were processed before this message appeared - please tell me if they were are not")
        break
try:cv2.imwrite("working_files/output_image/output.png", frameConjoined)
except: print("the bad kind of error happened")
print("complete")
cap.release()