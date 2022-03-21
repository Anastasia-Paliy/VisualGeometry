import random
from PIL import Image, ImageDraw

image1 = Image.open("park.jpg")
image2 = Image.open("winter.jpg")
draw = ImageDraw.Draw(image1)
# Images are of equal size
width  = image1.size[0]
height = image1.size[1]	
im1 = image1.load()
im2 = image2.load()

for x in range(width // 3, 2 * width // 3):
        t = (x - width // 3) / (width //3 - 1)
        for y in range(height):
                r1 = im1[x, y][0]
                g1 = im1[x, y][1]
                b1 = im1[x, y][2]

                r2 = im2[x, y][0]
                g2 = im2[x, y][1]
                b2 = im2[x, y][2]

                draw.point((x, y), (int((1 - t) * r1 + t * r2) ,
                                    int((1 - t) * g1 + t * g2),
                                    int((1 - t) * b1 + t * b2)))
                
for x in range(2 * width // 3, width):
        for y in range(height):
                r = im2[x, y][0]
                g = im2[x, y][1]
                b = im2[x, y][2]
        
                draw.point((x, y), (r, g, b))
             
                
image1.show()
del draw
