 
'''
To change the video framerate, size or format
'''
import cv2
import numpy as np
import os
from os.path import isfile, join
from natsort import natsorted

pathIn = './VideoConversion/Images/'

# Video to images
vidcap = cv2.VideoCapture('trump.mp4')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        image = cv2.resize(image,(450,360),interpolation = cv2.INTER_AREA)
        cv2.imwrite(pathIn+"image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

sec = 0
frameRate = 0.04 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)


# Images to video
pathOut = './VideoConversion/video.mp4'
fps = 25

frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]#for sorting the file names properly
files = natsorted(files)

for i in range(len(files)):
    filename=pathIn + files[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(pathOut,fourcc, fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()