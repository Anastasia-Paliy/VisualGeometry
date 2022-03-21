import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()
for x in range(0, width, 100):
        for y in range(height // 4, 3 * height // 4):
                for i in range(50):
                        draw.point((x + i, y), (128, 255, 0))

draw.ellipse((width // 2 - height // 4,
              height // 4,
              width // 2 + height // 4,
              3 * height // 4),
             (255, 128, 0),
             (255, 128, 0))
                
image.show()
del draw
