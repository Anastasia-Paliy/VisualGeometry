import random
from PIL import Image, ImageDraw

image = Image.open("bear.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
for x in range(width):
        for y in range(height):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]
                draw.point((x, y), (x, b, c))
image.show()
del draw
