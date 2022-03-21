import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                c = int(r * 0.1 + g * 0.6 + b * 0.3)
                draw.point((x, y), (c + 40, c + 20, c))
image.show()
del draw
