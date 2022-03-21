import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()

k = 1

for x in range(width // 2):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y),
                           (r * x // width * 2,
                            g * x // width * 2,
                            b * x // width * 2))

for start in range(width // 2, width, 10):
        for x in range(start, start + min(10, width - start)):
                for y in range(height):
                        r = pix[x, y][0]
                        g = pix[x, y][1]
                        b = pix[x, y][2]
                        draw.point((x, y), (int(r * k), int(g * k), int(b * k)))
        k += 0.05


                
        
image.show()
del draw
