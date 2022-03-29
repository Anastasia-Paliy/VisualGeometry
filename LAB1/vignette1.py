import random
from PIL import Image, ImageDraw
from math import sqrt

image = Image.open("winter.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
im = image.load()

R = min(width, height) // 2
x0 = width // 2
y0 = height // 2

for x in range(width):
        for y in range(height):
                r = im[x, y][0]
                g = im[x, y][1]
                b = im[x, y][2]

                if (x - x0)*(x - x0) + (y - y0)*(y - y0) >= R * R:
                        draw.point((x, y), (255, 255, 255))

                elif 9 * R * R // 16 < (x - x0)*(x - x0) + (y - y0)*(y - y0) < R * R:
                        t = 4 * sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0)) / R - 3
                        draw.point((x, y), (int((1 - t) * r + t * 255),
                                            int((1 - t) * g + t * 255),
                                            int((1 - t) * b + t * 255)))
                else:
                        continue

             
                
image.show()
del draw
