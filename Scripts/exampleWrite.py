
from colorsys import hsv_to_rgb
from PIL import Image

# Make some RGB values. 
# Cycle through hue vertically & saturation horizontally
colors = []
for hue in range(360):
    for sat in range(100):
        # Convert color from HSV to RGB
        #rgb = hsv_to_rgb(hue/360, sat/100, 1)
        #rgb = [int(0.5 + 255*u) for u in rgb]
        hsv = (hue//360,sat//100,1)
        colors.extend(hsv)

# Convert list to bytes
colors = bytes(colors)
img = Image.frombytes('HSV', (100, 360), colors)
img.show()
#img.save('hues.png')	






