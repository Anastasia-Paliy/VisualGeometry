import random
from PIL import Image, ImageDraw
from math import *

image = Image.open("park.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
im = image.load()

A1 = width // 2
B1 = height // 2
A2 = 3 * A1 // 4
B2 = 3 * B1 // 4
x0 = width // 2
y0 = height // 2

for x in range(width):
        for y in range(height):
                r = im[x, y][0]
                g = im[x, y][1]
                b = im[x, y][2]

                if (x - x0)*(x - x0)/(A1 * A1) + (y - y0)*(y - y0)/(B1 * B1) >= 1:
                        draw.point((x, y), (255, 255, 255))
               
                elif ((x - x0)*(x - x0)/(A1 * A1) + (y - y0)*(y - y0)/(B1 * B1) <= 1
                      and
                      (x - x0)*(x - x0)/(A2 * A2) + (y - y0)*(y - y0)/(B2 * B2) >= 1):

                        psi = atan2(y - y0, x - x0)
                       
                        fi1 = atan2(A1 * sin(psi), B1 * cos(psi))
                        x1 = A1 * cos(fi1) + x0
                        y1 = B1 * sin(fi1) + y0

                        fi2 = atan2(A2 * sin(psi), B2 * cos(psi))
                        x2 = A2 * cos(fi2) + x0
                        y2 = B2 * sin(fi2) + y0

                        #draw.point((x1, y1), (0, 0, 0))
                        #draw.point((x2, y2), (0, 0, 0))

                        d1 = sqrt((x1 - x0)*(x1 - x0) + (y1 - y0)*(y1 - y0))
                        d2 = sqrt((x2 - x0)*(x2 - x0) + (y2 - y0)*(y2 - y0))
                        d = sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))

                        t = (d - d2) / (d1 - d2)
                       
                        draw.point((x, y), (int((1 - t) * r + t * 255),
                                            int((1 - t) * g + t * 255),
                                            int((1 - t) * b + t * 255)))
                        
                else:
                        continue

                
image.show()
del draw
