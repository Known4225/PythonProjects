'''
Requires turtletools
This is a cool button
They don't do anything, but they sure look cool
'''
import turtle as t
from turtletools import turtleTools
import math as m
t.setup(960, 720)
t.colormode(255)
t.title("CoolButton")
tps = 30
turtools = turtleTools(t.getcanvas(), -240, -180, 240, 180, True)
class button:
    def __init__ (self, x, y, size=20, wide=2, text=""):
        # configurable controls
        t.Screen().bgcolor(39, 39, 39)
        self.buttonColor = (50, 50, 50)
        self.ring1Color = (80, 80, 80)
        self.ring2Color = (0, 0, 0)
        self.textColor = (150, 150, 150)
        self.buttonText = text
        self.x = x
        self.y = y
        self.size = size
        self.wide = wide
        self.ani1speed = 1
        self.ani2speed = 1
        self.circPrez = 24

        self.sp = t.Turtle()
        self.sp.hideturtle()
        self.circ = (2 * self.wide + m.pi * 1.25) * self.size
        self.straight = self.wide * self.size
        self.proportion = self.straight / self.circ
        self.mouseType = 0
        self.ani1Frames = 0
        self.ani2Frames = 0
        t.setworldcoordinates(-240, -180, 240, 180)
        self.sp.penup()
    def tick(self):
        self.sp.clear()
        self.mx, self.my = turtools.getMouseCoords(False)
        self.drawButton()
        if self.isTouchingMouse():
            if turtools.mouseDown():
                self.mouseType = 10
            if self.ani1Frames < 14:
                self.ani1Frames += self.ani1speed
        else:
            if self.ani1Frames > 0:
                self.ani1Frames -= self.ani1speed
        if self.mouseType > 0:
            if self.ani2Frames < 14:
                self.ani2Frames += self.ani2speed
            else:
                self.mouseType -= 1
        else:
            if self.ani2Frames > 0:
                self.ani2Frames -= self.ani2speed
        self.animation1(self.ani1Frames, False, True)
        self.animation2(self.ani2Frames, True, True)
        self.sp.pencolor(self.textColor[0], self.textColor[1], self.textColor[2])
        self.sp.goto(self.x, self.y - 19)
        self.sp.write(self.buttonText, move=False, align='center', font=('Calibri', 50))
        t.Screen().update()
    def drawButton(self):
        self.sp.pencolor(self.buttonColor[0], self.buttonColor[1], self.buttonColor[2])
        self.sp.pensize(self.size * 5)
        self.sp.goto(self.x - self.size * self.wide, self.y)
        self.sp.pendown()
        self.sp.goto(self.x + self.size * self.wide, self.y)
        self.sp.penup()
    def isTouchingMouse(self): #need a better approximation
        if self.mx >= (self.x - (self.wide + 1.25) * self.size) and self.mx <= (self.x + (self.wide + 1.25) * self.size) and self.my >= (self.y - self.size * 1.25) and self.my <= (self.y + self.size * 1.25):
            return True
        else:
            return False
    def animation1(self, frame, vert1, vert2):
        self.sp.pencolor(self.ring1Color[0], self.ring1Color[1], self.ring1Color[2])
        self.sp.pensize(self.size * 0.1)
        self.animationShell(frame, vert1, vert2)
    def animation2(self, frame, vert1, vert2):
        self.sp.pencolor(self.ring2Color[0], self.ring2Color[1], self.ring2Color[2])
        self.sp.pensize(self.size * 0.5)
        self.animationShell(frame, vert1, vert2)
    def animationShell(self, frame, vert1, vert2): #optimize the math
        vfac = (vert1 - 0.5) * 2
        vfac2 = (vert2 - 0.5) * 2
        angle = 180 / self.circPrez
        self.sp.goto(self.x, self.y + vfac * 1.25 * self.size)
        frameset = self.sigmoid(frame, 7)
        if frame > 0:
            self.sp.pendown()
        if frameset > self.proportion:
            self.sp.goto(self.x + self.straight, self.y + vfac * 1.25 * self.size)
            if frameset > 1 - self.proportion:
                for i in range(self.circPrez + 1):
                    self.sp.goto(self.x + self.straight + self.size * 1.25 * m.sin(m.radians(i * angle)), self.y + self.size * vfac * 1.25 * m.cos(m.radians(i * angle)))
                self.sp.goto(self.x + self.straight - self.straight * (frameset - (1 - self.proportion)) / self.proportion, self.y - vfac * 1.25 * self.size)
            else:
                theta = self.circPrez * ((frameset - self.proportion) / (1 - 2 * self.proportion))
                for i in range(round(theta)):
                    self.sp.goto(self.x + self.straight + self.size * 1.25 * m.sin(m.radians(i * angle)), self.y + self.size * vfac * 1.25 * m.cos(m.radians(i * angle)))
                self.sp.goto(self.x + self.straight + self.size * 1.25 * m.sin(m.radians(theta * angle)), self.y + self.size * vfac * 1.25 * m.cos(m.radians(theta * angle)))
        else:
            self.sp.goto(self.x + self.straight * frameset / self.proportion, self.y + vfac * 1.25 * self.size)
        self.sp.penup()
        self.sp.goto(self.x, self.y + vfac2 * 1.25 * self.size)
        if frame > 0:
            self.sp.pendown()
        if frameset > self.proportion:
            self.sp.goto(self.x - self.straight, self.y + vfac2 * 1.25 * self.size)
            if frameset > 1 - self.proportion:
                for i in range(self.circPrez + 1):
                    self.sp.goto(self.x - self.straight - self.size * 1.25 * m.sin(m.radians(i * angle)), self.y + self.size * vfac2 * 1.25 * m.cos(m.radians(i * angle)))
                self.sp.goto(self.x - self.straight + self.straight * (frameset - (1 - self.proportion)) / self.proportion, self.y - vfac2 * 1.25 * self.size)
            else:
                theta = self.circPrez * ((frameset - self.proportion) / (1 - 2 * self.proportion))
                for i in range(round(theta)):
                    self.sp.goto(self.x - self.straight - self.size * 1.25 * m.sin(m.radians(i * angle)), self.y + self.size * vfac2 * 1.25 * m.cos(m.radians(i * angle)))
                self.sp.goto(self.x - self.straight - self.size * 1.25 * m.sin(m.radians(theta * angle)), self.y + self.size * vfac2 * 1.25 * m.cos(m.radians(theta * angle)))
        else:
            self.sp.goto(self.x - self.straight * frameset / self.proportion, self.y + vfac2 * 1.25 * self.size)
        self.sp.penup()
    def sigmoid(self, frame, offset):
        return 1 / (1 + m.e ** -(frame - offset))
main = [button(-170, 150, 20, 2, "text"), button(-50, 150, 20, 1, "link"), button(120, 150, 20, 4.5, "projects")] #you can create any buttons wherever you want (canvas is 480 by 360)
def tick():
    for i in range(len(main)):
        main[i].tick()
if tps == 'inf' or tps == 'infinity':
    while True:
        tick()
else:
    while True:
        t.ontimer(tick(), int(1000/tps))
