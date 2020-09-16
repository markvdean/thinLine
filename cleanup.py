import os # todo: add more comments
import numpy as np
import cv2
x = "\\" + str(input("file pls  "))
cap = cv2.VideoCapture("working_files\\source_videos" + x)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count = 0
if input("timelapse mode? yes/no  ") == "no": # adjusts ending and beginning of cropped frame region
    k = int(input("slice width? int>0  "))
    w1 = cap.get(3)
    w2 = w1
    if w1%2 == 0: w1 = w1/2
    else: w = w1/2 - k/2
    if w2%2 == 0: w2 = w2/2 + k
    else: w = w2/2 + k/2
    k = 0
else:
    k = int(input("slice width? int>0  "))
    w1 = 0
    w2 = k
if k >= 3 and input("blend slices? (best used in timelapse mode) yes/no  ") == "yes": # add option for ignoring absolutes and therefore reducing minimum to 2 with adjusted version of the blending part?
    blend = True
    bpoint = round(float(1/k), 2)
else: blend = False
h = cap.get(4)
h = int(h)
w1 = int(w1)
w2 = int(w2)
while cap.isOpened():
    try:
        ret, frame = cap.read()
        if count != 0 and count != 1:
            frameCropped = frame[0:h, w1:w2]
            frameConjoined = cv2.hconcat([frameConjoined, frameCropped])
            # if count % 2 != 0: cv2.imwrite("working_files/output_image/previousframe-1.png", frameCropped)
            # else: cv2.imwrite("working_files/output_image/previousframe-2.png", frameCropped)
        elif count == 1:
            outputIMG = cv2.imread("working_files/output_image/output.png")
            frameCropped = frame[0:h, w1:w2]
            if blend == True:
                w3 = w1 + k
                w4 = w2 + k
                frame4nextCropped = frame[0:h, w3:w4]
                cv2.imwrite("working_files/output_image/previousframe-2.png", frame4nextCropped)
                w3 = w1
                w4 = w1 + 1
                for i in range(k):
                    frame4Blend1 = frame[0:h, w3:w4]
                    frame4Blend2 = cv2.imread("working_files/outputimage/previousframe-1.png")
                    frame4Blend2 = frame4Blend2[0:h, w3:w4]
                    frameInBlending = 
                    # todo: split slice into pixels and blend previous frame over the top in a linear gradient starting with the previous ending with the current, ignoring absolutes for blending, adding original on the end, though.
                    w3 += 1
                    w4 += 1
            frameConjoined = cv2.hconcat([outputIMG, frameCropped])
        else:
            frameCropped = frame[0:h, w1:w2]
            cv2.imwrite("working_files/output_image/output.png", frameCropped)
            if blend == True:
                w3 = w1 + k
                w4 = w2 + k
                cv2.imwrite("working_files/output_image/previousframe-1.png", frame)
        if ret is False:
            print("done!")
            break
        w1 += k
        w2 += k
    except: 
        print("uh oh")
        break
    count += 1
    print(count, "of", total)  
try: cv2.imwrite("working_files/output_image/output.png", frameConjoined)
except: print("uh oh")
print("complete")
cap.release()