import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
k = 1
for start in range(0, width, 50):
        for x in range(start, start + min(50, width - start)):
                for y in range(height):
                        r = pix[x, y][0]
                        g = pix[x, y][1]
                        b = pix[x, y][2]
                        draw.point((x, y), (int(r * k), int(g * k), int(b * k)))
        k += 0.1
        
image.show()
del draw
