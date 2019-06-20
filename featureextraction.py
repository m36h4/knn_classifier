import os
import csv
from PIL import Image as PImage
import numpy as np
from os import listdir
import cv2
import numpy as np
from matplotlib import pyplot as plt
list_new = []
path = "/root/MeghaInternship/Megha/group04/test/general_store_outdoor/"
def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = PImage.open(path + image)
        loadedImages.append(img)

    return loadedImages
images = loadImages(path)
for img in images:
	
# Display image in top subplot
	#plt.subplot(2,1,1)
	#plt.title('Original image')
	#plt.axis('off')
	#plt.imshow(img)
	image = np.asarray(img)
	red,blue,green = cv2.split(image)
	#print red

	#print green

	#print blue

	#plt.subplot(2,1,2)
	#plt.title('Histograms from color image')
	#plt.xlim((0,256))

	red_pixels = red.flatten()
	blue_pixels = blue.flatten()
	green_pixels = green.flatten()
	#print green_pixels

	hist  = cv2.calcHist([red_pixels], [0], None, [8], [0,255])
	hist,bins = np.histogram(red_pixels.ravel(),8,[0,255])
	
	a = hist.flatten()
	#print a
	
	hist  = cv2.calcHist([blue_pixels], [0], None, [8], [0,255])
	hist,bins = np.histogram(blue_pixels.ravel(),8,[0,255])
	
	b = hist.flatten()
	#print b

	hist  = cv2.calcHist([green_pixels], [0], None, [8], [0,255])
	hist,bins = np.histogram(green_pixels.ravel(),8,[0,255])
	
	c = hist.flatten()
	#print c

	d=np.concatenate((a,b,c), axis=None)
	list_new.append(d)
	
	
#np.savetxt('main1.csv',d,delimiter=',',fmt='%.4d')
out = open('general_store_outdoorts.csv', 'w')
for row in list_new:
	for column in row:
		out.write('%d;' % column)
    	out.write('\n')
out.close()
