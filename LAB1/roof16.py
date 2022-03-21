import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
for x in range(0, width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                if (x - width)**2 + (y - height // 2)**2 <= (height // 2)**2:
                        draw.point((x, y), (r + 80, g + 40, b))
                
image.show()
del draw
    
