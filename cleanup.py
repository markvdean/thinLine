import os
import numpy as np
import cv2
x = "\\" + str(input("file pls  "))
cap = cv2.VideoCapture("working_files\\source_videos" + x)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count = 0
# w1 = cap.get(3)
# w2 = w1
w1 = 0
w2 = 10
h = cap.get(4)
# if w1%2 == 0: w1 = w1/2
# else: w = w1/2 - 0.5
# if w2%2 == 0: w2 = w2/2 + 1
# else: w = w2/2 + 0.5
# w1 = int(w1)
# w2 = int(w2)
h = int(h)
while cap.isOpened():
    try:
        ret, frame = cap.read()
        if count != 0 and count != 1:
            frameCropped = frame[0:h, w1:w2]
            frameConjoined = cv2.hconcat([frameConjoined, frameCropped])
            cv2.imshow("preview", frameConjoined)
        elif count == 1:
            outputIMG = cv2.imread("working_files/output_image/output.png")
            frameCropped = frame[0:h, w1:w2]
            frameConjoined = cv2.hconcat([outputIMG, frameCropped])
            cv2.imshow("preview", frameConjoined)
        else:
            frameCropped = frame[0:h, w1:w2]
            cv2.imwrite("working_files/output_image/output.png", frameCropped)
        if ret is False:
            print("done!")
            break
        w1 += 10
        w2 += 10
    except: 
        print("uh oh")
        break
    count += 1
    print(count, "of", total)  
try: cv2.imwrite("working_files/output_image/output.png", frameConjoined)
except: print("uh oh")
print("complete")
cap.release()