import cv2
import os
import numpy as np

#User parameters -------------------------------------------------------------------------------------------
videoName = 'Town Growth'
resolution=4096
frameRate=5
#--------------------------------------------------------------------------------------------------------------

imgList=os.listdir() #Gets list of all files in the directory
fourcc = cv2.VideoWriter_fourcc(*'XVID') #Video codec
videoWriter = cv2.VideoWriter(videoName+'.avi', fourcc, frameRate, (resolution, resolution)) #The video writer object

frCount=1
for fileName in imgList: #For each image
    if '.py' not in fileName: #Make sure not to interpret this python script as an image!
        cvImage = cv2.imread(fileName) #Read the image into opencv numpy array
        videoWriter.write(cvImage) #Append the video with the new image
        print('frame '+str(frCount)+' done') #Print the frame number that just got added, useful for knowing if the program is stuck
        frCount+=1 #Bump frame count

videoWriter.release() #finish writing video
            