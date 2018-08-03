import msprime as msp
import numpy as np
from PIL import Image

def Visualize(Filename):

	treeSequence = msp.load(Filename)
	trees = treeSequence.trees()
	tableCollection = treeSequence.dump_tables()
	nodes = tableCollection.nodes
	numTrees = treeSequence.num_trees
	print(numTrees)

	RowsInImage = 1000
	ColumnsInImage = 1000

	data = np.zeros((RowsInImage,ColumnsInImage,3), dtype=np.uint8)

	length = treeSequence.sequence_length
	proportions = []

	EdgeTable = tableCollection.edges
	NodeTable = tableCollection.nodes

	minimumTime = min(NodeTable.time)
#	print(minimumTime)

	#Change to retrospective "Time Ago"
	timeShift = NodeTable.time - minimumTime + 1
	NodeTable.set_columns(flags=NodeTable.flags,time=timeShift,population=NodeTable.population)
#	print(NodeTable.time)
	ts = tableCollection.tree_sequence()


	oldestParent = 0
	for e in EdgeTable:
		parentNodeID = e.parent
		parentNode = ts.node(parentNodeID)
		parentAge = parentNode.time
		if (parentAge > oldestParent):
			oldestParent = parentAge 

	#Move the trees down 5 pixels so that there's no wrap-around
	oldestParent += 5
		
	for ee in EdgeTable:
		parentNodeID = ee.parent
		parentNode = ts.node(parentNodeID)
		parentAge = parentNode.time
		childNodeID = ee.child 
		childNode = ts.node(childNodeID)
		childAge = childNode.time
		
		childAgeProp = childAge / oldestParent
		childAgeRow = int(round(RowsInImage * childAgeProp)) 

		parentAgeProp = parentAge / oldestParent
		parentAgeRow = int(round(RowsInImage * parentAgeProp)) 

		leftProp = ee.left / length
		leftIntCol = int(round(ColumnsInImage * leftProp))

		rightProp = ee.right / length
		rightIntCol = int(round(ColumnsInImage * rightProp))

		for pixel in range(leftIntCol,rightIntCol - 1):
			data[999 - childAgeRow][pixel] = [240,128,128] #salmon
			data[999 - parentAgeRow][pixel] = [255,215,18] #gold


	img = Image.fromarray(data)
	return img

	#img.show()

		 
		
				




		

		


