'''
Requires turtletools

Windows:
Shift key - turtools.keyPressed(16) (this is 7 on linux)
Space key - turtools.keyPressed(32) (this is o on linux)
Up arrow - turtools.keyPressed(38) (this is a on linux (problem))
Left arrow - turtools.keyPressed(37) (this is ctrl on linux)
Right arrow - turtools.keyPressed(39) (this is s on linux (problem))
Down arrow - turtools.keyPressed(40) (this is d on linux)

Linux:
Shift key - turtools.keyPressed(50) (this is ___ on windows)
Space key - turtools.keyPressed(65) (this is ___ on windows)
Up arrow - turtools.keyPressed(111) (this is ___ on windows)
Left arrow - turtools.keyPressed(113) (this is ___ on windows)
Right arrow - turtools.keyPressed(114) (this is ___ on windows)
Down arrow - turtools.keyPressed(116) (this is ___ on windows)

This project uses orthographic and perspective projection, by default it will use perspective
'''
import turtle as t
from turtletools import turtleTools
import math as m
t.setup(960, 720)
t.colormode(255)
t.title("3D Viewer")
t.Screen().bgcolor(255, 255, 255)
tps = 120
turtools = turtleTools(t.getcanvas(), -240, -180, 240, 180, True)
class main:
    def __init__(self):
        self.sp = t.Turtle()
        self.sp.hideturtle()
        self.sp.pencolor(0, 0, 0)
        self.sp.pensize(5)
        self.renderCoords = [-5, -5, -5, -5, -5, 5, -5, -5, -5, -5, 5, -5, -5, -5, -5, 5, -5, -5, 5, 5, 5, 5, 5, -5, 5, 5, 5, 5, -5, 5, 5, 5, 5, -5, 5, 5,
         -5, -5, 5, -5, 5, 5, -5, -5, 5, 5, -5, 5, 5, 5, -5, 5, -5, -5, 5, 5, -5, -5, 5, -5, 5, -5, 5, 5, -5, -5, -5, 5, -5, -5, 5, 5]
        # self.renderCoords = [5, 5, 5, 5, 5, -5, 5, 5, 5, 5, -5, 5, 5, 5, 5, -5, 5, 5]
        self.dir1 = 30
        self.dir2 = 30
        self.fov = 130
        self.scaling = 10

        self.bufferFrames = 1
        self.keys = ["null"]

        # optional camera code
        # self.camX = -10
        # self.camY = 0
        # self.camZ = 0
        # for i in range(0, len(self.renderCoords), 3):
        #     self.renderCoords[i] -= self.camX
        #     self.renderCoords[i + 1] -= self.camY
        #     self.renderCoords[i + 2] -= self.camZ


        for i in range(len(self.renderCoords)):
            self.renderCoords[i] *= self.scaling
    def tick(self):
        self.sp.clear()
        self.controls()
        # print(turtools.keys)
        for i in range(0, len(self.renderCoords), 6):
            self.drawLinePers(self.renderCoords[i], self.renderCoords[i + 1], self.renderCoords[i + 2],self.renderCoords[i + 3],self.renderCoords[i + 4],self.renderCoords[i + 5], self.dir1, self.dir2, self.fov)
            # self.drawLineOrth(self.renderCoords[i], self.renderCoords[i + 1], self.renderCoords[i + 2],self.renderCoords[i + 3],self.renderCoords[i + 4],self.renderCoords[i + 5], self.dir1, self.dir2, self.fov)
    def drawLineOrth(self, x1, y1, z1, x2, y2, z2, dir1, dir2, fov):
        #adapted from ti-84 program: AXIS
        dir1 = m.radians(dir1)
        dir2 = m.radians(dir2)
        H = m.sin(-dir2)
        I = m.sin(dir1) * m.cos(dir2)
        J = m.cos(dir1)
        K = m.cos(dir2)
        L = m.sin(dir1) * m.sin(dir2)
        O = 0
        self.sp.goto(x1 * K + y1 * O + z1 * H, x1 * L + y1 * J + z1 * I)
        self.sp.pendown()
        self.sp.goto(x2 * K + y2 * O + z2 * H, x2 * L + y2 * J + z2 * I)
        self.sp.penup()
    def goto3D(self, x, y, z, SD1, CD1, SD2, CD2, fov):
        calc1 = CD1 * y + SD1 * x
        inter = fov / ((calc1 * SD2 + fov) - (CD2 * z))
        self.sp.goto(((SD2 * z) + (calc1) * CD2) * inter, ((CD1 * x) - (SD1 * y)) * inter)
    def drawLinePers(self, x1, y1, z1, x2, y2, z2, dir1, dir2, fov):
        #adapted from Arms Design - 3D Wireframe
        CD1 = m.cos(m.radians(dir1))
        SD1 = m.sin(m.radians(dir1))
        CD2 = m.cos(m.radians(dir2))
        SD2 = m.sin(m.radians(dir2))
        self.goto3D(x1, y1, z1, SD1, CD1, SD2, CD2, fov)
        self.sp.pendown()
        self.goto3D(x2, y2, z2, SD1, CD1, SD2, CD2, fov)
        self.sp.penup()
    def controls(self):
        if turtools.mouseDown():
            if self.keys.count("mouse") == 0:
                self.keys.append("mouse")
                self.keys.append(0)
        else:
            self.removeKey("mouse")
        if turtools.keyPressed('w') or turtools.keyPressed("Up"):
            self.refillKey('w')
        else:
            self.removeKey('w')
        if self.keys.count('w'):
            self.dir1 -= 1
        if turtools.keyPressed('s') or turtools.keyPressed("Down"):
            self.refillKey('s')
        else:
            self.removeKey('s')
        if self.keys.count('s'):
            self.dir1 += 1
        if turtools.keyPressed('d') or turtools.keyPressed("Right"):
            self.refillKey('d')
        else:
            self.removeKey('d')
        if self.keys.count('d'):
            self.dir2 += 1
        if turtools.keyPressed('a') or turtools.keyPressed("Left"):
            self.refillKey('a')
        else:
            self.removeKey('a')
        if self.keys.count('a'):
            self.dir2 -= 1

    def refillKey(self, key):
        if self.keys.count(key) > 0:
            self.keys[self.keys.index(key) + 1] = self.bufferFrames
        else:
            self.keys.append(key)
            self.keys.append(self.bufferFrames)

    def removeKey(self, key):
        if self.keys.count(key) > 0:
            i = self.keys.index(key)
            if self.keys[i + 1] == 0:
                self.keys.pop(i)
                self.keys.pop(i)
            else:
                self.keys[i + 1] -= 1

# mainloop
obj = main()
def tick():
    obj.tick()
    # t.setworldcoordinates(-240, -180, 240, 180) do this to stretch the program on higher resolutions
    t.Screen().update() # do this to keep the program bounded at original resolutions (making the window bigger or smaller won't make things on the screen bigger or smaller)
if tps == 'inf' or tps == 'infinity':
    while True:
        tick()
else:
    while True:
        t.ontimer(tick(), int(1000/tps))