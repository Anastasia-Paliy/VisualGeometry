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
                
                draw.point((x, y), (r // 128 * 255,
                                    g // 128 * 255,
                                    b // 128 * 255))
                
image.show()
del draw
    
