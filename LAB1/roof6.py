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
                if x <= width // 3:
                        c = (r + g) // 2
                        draw.point((x, y), (c, c, 0))
                elif width // 3 < x <= 2 * width // 3:
                        draw.point((x, y), (r, 0, 0))
                else:
                        draw.point((x, y), (0, g, 0))
                
image.show()
del draw
