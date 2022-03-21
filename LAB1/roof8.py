import random
from PIL import Image, ImageDraw

image = Image.open("roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]	
pix = image.load()

green = [0 for i in range(256)]
red = [0 for i in range(256)]
blue = [0 for i in range(256)]
brightness = [0 for i in range(256)]

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                
                green[g] += 1
                red[r] += 1
                blue[b] += 1
                brightness[(r + g + b) // 3] += 1

m = max(green)
g_gist = [height // 2 * x // m for x in green]
m = max(red)
r_gist = [height // 2 * x // m for x in red]
m = max(blue)
b_gist = [height // 2 * x // m for x in blue]
m = max(brightness)
w_gist = [height // 2 * x // m for x in brightness]


for x in range(512):
        for y in range(height//2 - g_gist[x//2], height//2):
                draw.point((x, y), (0, 255, 0))

for x in range(512):
        for y in range(height//2 - r_gist[x//2], height//2):
                draw.point((x + width // 2, y), (255, 0, 0))

for x in range(512):
        for y in range(height - w_gist[x//2], height):
                draw.point((x, y), (192, 192, 192))

for x in range(512):
        for y in range(height - b_gist[x//2], height):
                draw.point((x + width // 2, y), (0, 0, 255))
                
image.show()
del draw



