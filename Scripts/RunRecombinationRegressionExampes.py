import msprime as msp
import numpy as np
from PIL import Image
import subprocess
from VisualizeRecombination import *
import sys
import io

RecipeName = "variatingRecomb.slim"
TreeFileName = "VRecombTemp.trees"
ImgName = "_VR.png"

Labels = ""

for i in range(3):
	
	RR = np.random.uniform(1e-8,1e-12)
	RR = round(RR,10)
	Labels += str(RR) + " "

	RRstr = "RR="+str(RR)

	subprocess.check_output(["../slim","-d",RRstr,"../Recipes/variatingRecomb.slim"])
	image = Visualize("../Trees/" + TreeFileName)
	image.save( "../Images/RecombRegressionData/" + str(i) + ImgName)

labelsFile = "../Images/RecombRegressionData/Labels"
fi = open(labelsFile,"w")
fi.write(Labels) 

