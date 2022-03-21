import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
for x in range(0, width):
        for y in range(height):
                if (2 * x - y) // (width // 12) % 2 == 0:
                        draw.point((x, y), (128, 128, 0))
                
image.show()
del draw
    
