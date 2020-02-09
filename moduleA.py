import cv2
import os
import numpy
def extractFrames(pathIn, pathOut):
	print("Performing frame extraction")
	os.mkdir(pathOut)
	cap = cv2.VideoCapture(pathIn)
	count = 0
	while (cap.isOpened()):
   	# Capture frame-by-frame
		ret, frame = cap.read()
		if ret == True:
			#length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
			#percent = count / length
			#percent = percent * 100
			#format(percent, '1f')
			#print(percent, "%")
			cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
			count += 1
		else:
			break
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
	print("done")