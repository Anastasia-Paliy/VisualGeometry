import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
for x in range(0, width - 1):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                r0 = pix[x + 1, y][0]
                g0 = pix[x + 1, y][1]
                b0 = pix[x + 1, y][2]
                delta = ((r + g + b) // 3) - ((r0 + g0 + b0) // 3)
                c = 128 + 2 * delta
                draw.point((x, y), (c, c, c))
                
image.show()
del draw
    
