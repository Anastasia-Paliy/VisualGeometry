import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()

green = [0 for i in range(256)]

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                green[g] += 1

m = max(green)
gist = [height // 2 * x // m for x in green]

for x in range(512):
        for y in range(height//2 - gist[x//2], height//2):
                draw.point((x, y), (0, 255, 0))
                
image.show()
del draw



