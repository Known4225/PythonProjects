'''
Requires turtletools
'''
import turtle as t
from turtletools import turtleTools
import math as m
t.setup(960, 720)
t.colormode(255)
t.title("AnimationTest")
tps = 60
turtools = turtleTools(t.getcanvas(), -240, -180, 240, 180, True)
class master:
    def __init__ (self):
        t.Screen().bgcolor(50, 50, 50)
        self.sp = t.Turtle()
        self.sp.hideturtle()
        self.sp.pencolor(200, 200, 200)
        self.oldfunc = 0
        self.x = 0
        self.y = 0
        self.xold = 0
        self.yold = 0
        self.xdest = 0
        self.ydest = 0
        self.mouseType = 0
        self.frameCount = 0
    def tick(self):
        t.setworldcoordinates(-240, -180, 240, 180)
        self.sp.clear()
        self.mx, self.my = turtools.getMouseCoords()
        self.sp.pensize(100)
        self.sp.goto(self.x, self.y)
        self.sp.pendown()
        self.sp.forward(0)
        self.sp.penup()
        if turtools.mouseDown():
            if self.mouseType == 0:
                # if abs(self.xdest - self.x) < 1 and abs(self.ydest - self.y) < 1:
                self.frameCount = 0
                self.oldfunc = 0
                self.xold = self.x
                self.yold = self.y
                self.mouseType = 1
            self.xdest = self.mx
            self.ydest = self.my
        else:
            self.mouseType = 0
        func = self.sigmoid(self.frameCount/5, 8)
        # func = self.sin(self.frameCount, 0)
        # func = self.log(self.frameCount, 50)
        # func = self.cosNormal(self.frameCount, self.oldfunc)
        # func = self.exponent(self.frameCount, 0.93)
        self.oldfunc = func
        self.x = self.xold + (self.xdest - self.xold) * func
        self.y = self.yold + (self.ydest - self.yold) * func
        print(func)
        self.frameCount += 1
    def sigmoid(self, frame, offset):
        return 1 / (1 + m.e ** -(frame - offset))
    def sin(self, frame, offset):
        return m.sin(m.radians(frame + offset))
    def log(self, frame, base):
        if frame < 1:
            return 0
        if frame > base:
            return 1
        return m.log(frame) / m.log(base)
    def cosNormal(self, frame, last):
        out = -m.cos(m.radians(frame + 90))
        if out < last:
            return last
        return out
    def exponent(self, frame, base):
        return abs(base ** frame - 1)
main = master()
if tps == 'inf' or tps == 'infinity':
    while True:
        main.tick()
else:
    while True:
        t.ontimer(main.tick(), int(1000/tps))