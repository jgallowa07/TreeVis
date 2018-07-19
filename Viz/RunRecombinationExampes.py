import msprime as msp
import numpy as np
from PIL import Image
import subprocess
from VisualizeRecombination import *

for i in range(5):

	#Run Simulations without recobination
	subprocess.check_output(["../Sims/slim","../Sims/Recipes/SingleLocusWithoutRecombination.slim"])
	image = Visualize("../Sims/Trees/Temp.trees")
	image.save( "../Images/LocusWithNoRecombination/" + str(i) + "_NR.png")

for i in range(5):

	#Run Simulation with recombination
	subprocess.check_output(["../Sims/slim","../Sims/Recipes/SingleLocusWithRecombination.slim"])
	image = Visualize("../Sims/Trees/Temp.trees")
	image.save( "../Images/LocusWithRecombination/" + str(i) + "_WR.png")

