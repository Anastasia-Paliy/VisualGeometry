import random
from PIL import Image, ImageDraw

image = Image.open("Lego.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()

green = [0 for i in range(256)]
red = [0 for i in range(256)]
blue = [0 for i in range(256)]

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                
                green[g] += 1
                red[r] += 1
                blue[b] += 1

T = int(0.005 * width * height)

for i in range(255):
        if red[i] > T:
                A1 = i
                break
for i in range(255, 0, -1):
        if red[i] > T:
                B1 = i
                break

for i in range(255):
        if green[i] > T:
                A2 = i
                break
for i in range(255, 0, -1):
        if green[i] > T:
                B2 = i
                break

for i in range(255):
        if blue[i] > T:
                A3 = i
                break
for i in range(255, 0, -1):
        if blue[i] > T:
                B3 = i
                break



for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]

                if r <= A1:
                        r = 0
                elif r >= B1:
                        r = 255
                else:
                        r = (r - A1) * 255 // (B1 - A1)
                
                if g <= A2:
                        g = 0
                elif g >= B2:
                        g = 255
                else:
                        g = (g - A2) * 255 // (B2 - A2)

                if b <= A3:
                        b = 0
                elif b >= B3:
                        b = 255
                else:
                        b = (b - A3) * 255 // (B3 - A3)
                        
                draw.point((x, y), (r, g, b))
                
image.show()
del draw



