class turtleTools():
    r'''
    This is a helper module for turtle projects
    Requires turtle to be imported as t
    Requires a canvas (t.setup()), and coordinate minimums and maximums as initial arguments
    Anytime the coordinates change or the screen resolution changes, you must reinitialize the module
    If the mouse coordinates are off, you can use turtletools.realign() to put them back in place (this is a last resort)
    Key presses use tkinter event.char in lookup (a space is ' ', a shift is ', tab is \t')
    Display turtleTools.keys while pressing a key to display the associated event.char
    If you would like more control, initialize turtools with an extra 'True' at the end of the initial arguments to activate KEYNUM mode

    Commands:
    getMouseCoords() - returns the coordinates of the mouse in two separate floats x then y
    mouseDown() - returns a boolean True if the LMB is being clicked and False otherwise, this can be configured to include RMB if needed
    keyPressed(key) - returns a boolean True if the key (character) input is being held down and False otherwise. This uses tkinter event.char in lookup
    realign() - this method attempts to realign the mouse coordinates with the window coordinates. It does this by resizing the window.
    '''
    def __init__(self, cv, xmin, ymin, xmax, ymax, keynum=False):
        import turtle as t
        t.setworldcoordinates(xmin, ymin, xmax, ymax)
        t.penup()
        t.tracer(0, 0)
        t.speed(0)
        t.delay(0)
        t.ht()
        self.window = t.Screen()
        self.x = 0
        self.y = 0
        self.keys = []
        self.cv = cv
        self.screenwidth = self.cv.winfo_screenwidth()
        self.screenheight = self.cv.winfo_screenheight()
        self.initwidth = self.cv.winfo_width()
        self.initheight = self.cv.winfo_height()
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.marginleft = -13
        self.margintop = -13
        self.marginright = -7
        self.marginbottom = -7
        self.wasmaxed = 0
        self.resized = 0
        self.clicked = False
        self.cv.bind('<Button-1>', self.mouse)
        self.cv.bind('<Button1-ButtonRelease>', self.release)
        self.keyNum = keynum
        self.cv.bind('<KeyPress>', self.keyPress)
        self.cv.bind('<KeyRelease>', self.keyRelease)
        t.listen()
    def getMouseCoords(self):
        self.width = self.cv.winfo_width()
        self.height = self.cv.winfo_height()
        if self.height == self.screenheight - 72:
            if self.screenwidth/self.screenheight == 16/9 and self.wasmaxed == 0:
                self.resized = 1
            else:
                self.resized = 2
                self.wasmaxed = 1
        elif self.width == self.screenwidth and self.height == self.screenheight - 63:
            self.resized = 1
            self.wasmaxed = 1
        else:
            if self.resized > 0 or self.width != self.initwidth or self.height != self.initheight:
                self.resized = 2
                self.wasmaxed = 0
        if self.resized == 0:
            self.offsetX = -13
            self.offsetY = -13
        elif self.resized == 1:
            self.offsetX = -13
            self.offsetY = -13.5
        else:
            self.offsetX = -4
            self.offsetY = -4
        x, y = self.cv.winfo_pointerx() - self.cv.winfo_rootx(), self.cv.winfo_pointery() - self.cv.winfo_rooty()
        self.w, self.h = self.width + self.marginleft + self.marginright, self.height + self.margintop + self.marginbottom
        self.scalex = (self.xmax - self.xmin) / self.w
        self.scaley = (self.ymin - self.ymax) / self.h
        self.x = (x + self.offsetX) * self.scalex + self.xmin
        self.y = (y + self.offsetY) * self.scaley + self.ymax
        return self.x, self.y
    def realign(self):
        self.width = self.cv.winfo_width()
        self.height = self.cv.winfo_height()
        self.window.setup(self.xmax - self.xmin, self.ymax - self.ymin)
        self.resized = 2
    def mouse(self, event):
        self.clicked = True
    def release(self, event):
        self.clicked = False
    def mouseDown(self):
        return self.clicked
    def keyPressed(self, key):
        if key in self.keys:
            return True
        return False
    def keyPress(self, event):
        if event.char not in self.keys:
            self.keys.append(event.char)
            if self.keyNum:
                self.keys.append(event.keycode)
    def keyRelease(self, event):
        try:
            self.keys.remove(event.char)
            if self.keyNum:
                self.keys.remove(event.keycode)
        except:
            self.keys = []
