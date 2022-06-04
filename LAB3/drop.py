import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0


def line(x1, y1, x2, y2, color):  # рисуем линию из точки (x1,y1) в точку (x2,y2)
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY
            y = y1
            dirY = sign(y2 - y1)
            for x in range(x1, x2 + 1):
                    draw.point((x,y), color)
                    err += dErr
                    if err + err >= dX:
                            y += dirY
                            err -= dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y), color)
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY

                            
def bezie(p0, p1, p2, p3, color):
	oldBx = p0[0]
	oldBy = p0[1]
	for i in range(101):
		t = i / 100
		Bx = int((1-t)*(1-t)*(1-t)*p0[0] + 3*t*(1-t)*(1-t)*p1[0] + 3*t*t*(1-t)*p2[0] + t*t*t*p3[0])
		By = int((1-t)*(1-t)*(1-t)*p0[1] + 3*t*(1-t)*(1-t)*p1[1] + 3*t*t*(1-t)*p2[1] + t*t*t*p3[1])
		line(oldBx, oldBy, Bx, By, color)
		oldBx = Bx
		oldBy = By

image = Image.new('RGBA', (400, 400))
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей
for x in range(width):
        for y in range(height):
                draw.point((x, y), (255, 255, 255))
                
x11 = 200
y11 = 100
x12 = 190
y12 = 295
x13 = 150
y13 = 295
x14 = 200
y14 = 300

line(x11, y11, x12, y12, (255, 0, 0))
line(x13, y13, x14, y14, (255, 0, 0))
bezie((x11, y11), (x12 , y12), (x13 , y13), (x14, y14), (0, 0, 255))


x22 = 210
x23 = 250

line(x11, y11, x22, y12, (255, 0, 0))
line(x23, y13, x14, y14, (255, 0, 0))
bezie((x11, y11), (x22 , y12), (x23 , y13), (x14, y14), (0, 0, 255))

image.show()
#image.save("result.jpg")
del draw