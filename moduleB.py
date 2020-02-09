from PIL import Image
import os
import numpy
def cropFrames():
	print("Merging split frames")
	width = 0
	height = int(input("Enter the pixel height of the video:  "))
	for i in range(len(os.listdir("working_files/split_frames"))):
		width += 1
	outputIMG = Image.new('RGB', (width, height), color = 'red')
	x_offset = width
	count = 0
	for i in os.listdir("working_files/split_frames"):
		f = "frame" + str(count) + ".jpg"
		im = Image.open("working_files/split_frames/{:s}".format(f), mode='r')
		width, height = im.size
		w1 = width/2
		w1 += 150
		w2 = w1 + 1
		cropped_Image = im.crop((w1, 0, w2, height)
		outputIMG.paste(cropped_Image, (x_offset, 0))
		x_offset -= 1
		count += 1
	outputIMG.save("working_files/output_image/output.png", format="png")
	print("done")