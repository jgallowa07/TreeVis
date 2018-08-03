import msprime
from VisualizeTrees import *

nodes = open("toyNodeTable.txt","r")
edges = open("toyEdgeTable.txt","r")
ts = msprime.load_text(nodes=nodes,edges=edges)
img = VisualizeNodes(ts,rescaled_time=False)
for t in ts.trees():
    print(t.draw(format="unicode"))
img.show()
