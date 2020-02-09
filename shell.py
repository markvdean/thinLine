from PIL import Image
from moduleA import extractFrames
from moduleB import cropFrames
import os
import shutil
import numpy
if not os.path.exists("working_files/output_image"):
   os.mkdir("working_files/output_image")
print("Videos:")
for i in range(len(os.listdir("working_files/source_videos"))):
   print(i, " ", os.listdir("working_files/source_videos")[i])
choice = os.listdir("working_files/source_videos")[int(input("Enter number of video you want to make an image out of: "))]
print(choice, "selected.")
shutil.rmtree("working_files/split_frames", ignore_errors=True)
extractFrames("working_files/source_videos/{0}".format(choice), "working_files/split_frames")
cropFrames()
# if not os.path.exists("working_files/cropped_frames"):
#    os.mkdir("working_files/cropped_frames")
# if input("Should the frames be extracted? y/n  ") == "y":
#    shutil.rmtree("working_files/split_frames", ignore_errors=True)
#    extractFrames("working_files/source_videos/{0}".format(choice), "working_files/split_frames")
# if input("Should the frames be cropped? y/n  ") == "y":
#    shutil.rmtree("working_files/cropped_frames", ignore_errors=True)
#    os.mkdir("working_files/cropped_frames")
#    cropFrames()
# print("Attaching cropped frames")
# width = 0
# height = int(input("Enter the pixel height of the video:  "))
# for i in range(len(os.listdir("working_files/cropped_frames"))):
#    width += 1
# outputIMG = Image.new('RGB', (width, height), color = 'red')
# x_offset = width
# count = 0
# for i in os.listdir("working_files/cropped_frames"):
#    f = str(count) + "_cropped.png"
#    now = Image.open("working_files/cropped_frames/{:s}".format(f))
#    outputIMG.paste(now, (x_offset, 0))
#    x_offset -= 1
#    count += 1
# outputIMG.save("working_files/output_image/output.png", format="png")
# print("done")
# print("Operations complete - please check the following directory: working_files/output_image")