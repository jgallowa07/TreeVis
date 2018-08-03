import io
import sys
import os
import numpy as np
from keras.preprocessing import image
from PIL import Image

def LoadImageData(rootdir,labelPath,numSamples,imagePostFix=".png",RowsInImage=1000,ColumnsInImage=1000):
	'''
	This function takes in a directory with images with prefix 1 .. n,
	and a labels file where all labels are in one line and seperated by a space. 

	returns the respective tensors for all data
	
	Image data will be a 4D Tendsor with Shape: (Samples,)

	'''
	labelsfile = open(labelPath,"r")
	labels = labelsfile.readline().split()
	labels = np.asarray(labels)
	labels = labels.astype(float)

	allImageData = np.zeros([numSamples,RowsInImage,ColumnsInImage,3])

	for i in range(numSamples):
		filename = str(i) + imagePostFix
		filepath = os.path.join(rootdir,filename)
		img = Image.open(filepath)
		allImageData[i] = image.img_to_array(img)

	return allImageData,labels

		
		
		
