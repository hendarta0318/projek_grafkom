from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1360,1000

def cover():

    glBegin(GL_QUADS)
    glVertex2f(250, 100)#kiri atas, kiri bawah
    glVertex2f(520, 100)#<=kanan bawah, kanan atas
    glVertex2f(520, 270)#<=kanan atas, kanan bawah
    glVertex2f(250, 270)#kiri bawah, kiri atas
    glEnd()

def iterate():
    glViewport(0, 0, 1360, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1360, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glClearColor(255,255,0,0)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 0.0)
    cover()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1360, 695)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("LABMATH (LABIRIN MATHEMATIC)")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
