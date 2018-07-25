
import numpy as np
from PIL import Image


Rows = 50
Columns = 100

data = np.zeros((Rows,Columns,3), dtype=np.uint8 )

for r in range(Rows):
	for c in range(Columns):
		data[r][c] = [2*r,2*c,0]

img = Image.fromarray(data)
img.show()

		






