from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.5, 0.5, 0.5, 1.0) 
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def getCoordinates(axe, dirA):
        
        points = []
        for i in range(4):
                point = [0, 0, 0]
                point[axe] = dirA
                                
                if i//2 == 0:
                        point[(axe+1)%3] = -0.5
                else:
                        point[(axe+1)%3] = 0.5
                if i%3 == 0:
                        point[(axe+2)%3] = -0.5
                else:
                        point[(axe+2)%3] = 0.5
                points.append(point)

        return(points)


def draw(*args, **kwargs):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotated(0.01,1,1,1)
        
        glBegin(GL_QUADS)

        c = 0
        for axe in range(3):
                for dirA in [-0.5, 0.5]:
                        points = getCoordinates(axe, dirA)
                        glColor3f(*colors[c])
                        for point in points:
                                glVertex3d(*point)
                        c += 1
                        c %= 6
        glEnd()
        glutSwapBuffers()
        glutPostRedisplay()      


global colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Cube")
glutDisplayFunc(draw)
init()
colors = [(255*i, 255*j, 255*k) for i in range(2)
          for j in range(2)
          for k in range(2)]
glutMainLoop()
