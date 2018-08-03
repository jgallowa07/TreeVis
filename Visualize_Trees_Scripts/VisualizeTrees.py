import msprime
import numpy as np
from treestats import *
from PIL import Image,ImageColor

## Assign angles in [0,2*pi] to each sample, then compute the average angle
## for each internal node of each tree of all samples below each node.

Ne = 500
ts = msprime.simulate(Ne, recombination_rate=1.0,random_seed=12)

def Visualize(ts):

    #sample_angles = np.random.uniform(0.0, 2*np.pi, ts.num_samples)
    #one_weights = np.repeat(1.0,ts.num_samples)

    #color each sample evenly around the hue circle
    initial_hues = np.linspace(0,2*np.pi,ts.num_samples,endpoint=False)

    #The function for that will compute mean hue for the weight[0] 
    #of the parent node given it's two children's hues.
    def angle_mean(a):
        # gives the angle of the average vector in the unit circle
        # https://en.wikipedia.org/wiki/Mean_of_circular_quantities
        return np.math.atan2(sum(np.sin(a)), sum(np.cos(a)))

    wt = weighted_trees(ts, [initial_hues], angle_mean)
        
    RowsInImage = 1000
    ColumnsInImage = 1000
    length = ts.sequence_length
    chromPos = 0
    nt = ts.num_trees 

    #initialize empty tensor 
    data = np.zeros((RowsInImage,ColumnsInImage,3), dtype=np.uint8)
    #find oldest node to scale the trees by
    oldest_node = max([n.time for n in ts.nodes()])
    rescaled_oldest_node = Ne - (1/(1/Ne + oldest_node))

    #un-normalize the tree heights
    #rescaled_time = Ne - 1/(1/Ne + ts.tables.nodes.time)
    #oldest_node = max(rescaled_time)

    #get the correct column index interval for respective trees along the genome
    bp = (np.array([b for b in ts.breakpoints()])*(ColumnsInImage/ts.sequence_length)).astype(np.int)

    for i,t in enumerate(wt):
        node_times = np.array([ts.node(u).time for u in t.nodes()])
        rescaled_time = Ne - (1/(1/Ne + node_times))
        #oldest_node = max(node_times)
        #Get the correct row index for respective node times in each sparse tree
        node_rows = (rescaled_time * (RowsInImage / rescaled_oldest_node)).astype(np.int)
        #print(node_rows)
        #break
        node_hues = (np.array([w[0] for w in t.node_weights()])*((360/(2*np.pi)))%360).astype(np.int)
        #print(node_rows,node_hues)
        for r,h in zip(node_rows,node_hues):
            for pixel in range(bp[i],bp[i+1]):
                colorstring = "hsl("+str(h)+",100%,50%)"
                data[(RowsInImage-1) - r][pixel] = ImageColor.getcolor(colorstring,mode="HSV")

    img = Image.fromarray(data)
    return img


img = Visualize(ts)
img.save("hv.png")
img.show()
