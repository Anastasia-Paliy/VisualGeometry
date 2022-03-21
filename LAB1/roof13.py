import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
for x in range(width // 2):
        for y in range(x * height // width, height - x * height // width):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y), (255, 0, 255))

for x in range(width // 2, width):
        for y in range(height - x * height // width, x * height // width):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y), (255, 0, 255))
                
image.show()
del draw
