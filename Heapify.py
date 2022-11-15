'''
requires keyboard module (pip install keyboard)
Usage:
when run it will prompt you with the option to automatically advance through the heapsort, type 'none' for default experience
a list of length 15 will generate (this can be configured), then an empty heap will be created. Press space to advance through the heap sort.
This project will show how the heap sort algorithm works.
The first heap will be adding elements to the empty heap and swapping to create a max heap
The second heap will be remove elements from the max heap to sort the list
Heap sort is an O(nlog(n)) time complexity algorithm
'''


import turtle as t
import math as m
import random as r
import keyboard as key
t.speed(0)
t.hideturtle()
t.penup()
t.pencolor('Black')
t.fillcolor('White')
t.screensize(400, 3000)
t.pensize(4)
def drawArray(ar, y):
    stx = 50 * (len(ar) / 2)
    sty = y
    t.goto(stx, sty - 50)
    t.pendown()
    t.goto(-stx, sty - 50)
    t.goto(-stx, sty)
    for i in range(len(ar) + 1):
        t.goto(-stx + 50 * i, sty)
        t.goto(-stx + 50 * i, sty - 50)
        t.goto(-stx + 50 * i, sty)
    t.penup()
    for i in range(len(ar)):
        t.goto(-stx  + 25 + 50 * i, sty - 42)
        t.write(ar[i], move=False, align='center', font=('Courier', 20, 'bold'))
    for i in range(len(ar)):
        t.goto(-stx  + 25 + 50 * i, sty + 8)
        t.write(i + 1, move=False, align='center', font=('Courier', 20, 'bold'))
def drawSegment(ar, y, seg, lnth):
    stx = -50 * (lnth / 2) + (seg - 1) * 50
    sty = y
    t.goto(stx, sty - 50)
    t.pendown()
    t.goto(stx + 50, sty - 50)
    t.goto(stx + 50, sty)
    t.goto(stx, sty)
    t.goto(stx, sty - 50)
    t.penup()
    t.goto(stx  + 25, sty - 42)
    t.write(ar, move=False, align='center', font=('Courier', 20, 'bold'))
    t.goto(stx  + 25, sty + 8)
    t.write(seg, move=False, align='center', font=('Courier', 20, 'bold'))
def heapify():
    g = 1
def deleteHeap(ar, yset):
    counter = 0
    layers = 0
    while len(ar) > 2 ** layers - 1:
        layers += 1
    gralay = layers * 0.3
    circ = 30 / gralay
    sty = yset - circ * 2
    stx = 0
    ang = 20
    yval = 100
    xArray = []
    yArray = []
    angArray = []
    xArray.append(0)
    yArray.append(sty)
    angArray.append(0)
    ind = 1
    for i in range(1, layers):
        for j in range((2 ** i) // 2):
            rad = m.radians(ang)
            xArray.append(xArray[ind // 2] - yval/m.tan(rad))
            yArray.append(sty - i * yval)
            angArray.append(rad)
            xArray.append(xArray[ind // 2] + yval/m.tan(rad))
            yArray.append(sty - i * yval)
            angArray.append(rad)
            ind += 2
        ang += 69/(layers - 1)
    i = 0
    while i < len(ar):
        k = 2 * i + 1
        l = 2 * i + 2
        t.goto(stx + xArray[i], yArray[i])
        t.pendown()
        t.begin_fill()
        t.circle(circ)
        t.end_fill()
        t.penup()
        t.goto(stx + xArray[i] + 1, yArray[i] + (3 / (gralay)))
        t.write(ar[i], move=False, align='center', font=('Courier', int(circ), 'bold'))
        icache = i
        while i != 0:
            if ar[(i + 1) // 2 - 1] < ar[i]:
                cache = ar[i]
                ar[i] = ar[(i + 1) // 2 - 1]
                ar[(i + 1) // 2 - 1] = cache
                t.goto(stx + xArray[i], yArray[i])
                t.pendown()
                t.begin_fill()
                t.circle(circ)
                t.end_fill()
                t.penup()
                t.goto(stx + xArray[i] + 1, yArray[i] + (3 / (gralay)))
                t.write(ar[i], move=False, align='center', font=('Courier', int(circ), 'bold'))
                i = (i + 1) // 2 - 1
                t.goto(stx + xArray[i], yArray[i])
                t.pendown()
                t.begin_fill()
                t.circle(circ)
                t.end_fill()
                t.penup()
                t.goto(stx + xArray[i] + 1, yArray[i] + (3 / (gralay)))
                t.write(ar[i], move=False, align='center', font=('Courier', int(circ), 'bold'))
            else:
                i = 0
        i = icache
        if k < len(ar):
            t.goto(stx + xArray[i] + circ * m.sin(3 * m.pi / 2 - angArray[k]), yArray[i] + circ * (1 + m.cos(3 * m.pi / 2 - angArray[k])))
            t.pendown()
            t.goto(stx + xArray[k] + circ * m.sin(m.pi / 2 - angArray[k]), yArray[k] + circ * (1 + m.cos(m.pi / 2 - angArray[k])))
            t.penup()
        if l < len(ar):
            t.goto(stx + xArray[i] + circ * m.sin(m.pi / 2 + angArray[l]), yArray[i] + circ * (1 + m.cos(m.pi / 2 + angArray[l])))
            t.pendown()
            t.goto(stx + xArray[l] + circ * m.sin(3 * m.pi / 2 + angArray[l]), yArray[l] + circ * (1 + m.cos(3 * m.pi / 2 + angArray[l])))
            t.penup()
        i += 1
    end = len(ar) - 1
    final = []
    while end > -1:
        if auto != '2' and auto != 'both':
            wait('space')
        counter += 1
        cache = ar[0]
        ar[0] = ar[end]
        ar[end] = cache
        final.append(cache)
        t.goto(stx + xArray[end], yArray[end])
        t.pendown()
        t.begin_fill()
        t.circle(circ)
        t.end_fill()
        t.penup()
        t.goto(stx + xArray[end] + 1, yArray[end] + (3 / (gralay)))
        t.write(ar[end], move=False, align='center', font=('Courier', int(circ), 'bold'))
        t.goto(stx + xArray[0], yArray[0])
        t.pendown()
        t.begin_fill()
        t.circle(circ)
        t.end_fill()
        t.penup()
        t.goto(stx + xArray[0] + 1, yArray[0] + (3 / (gralay)))
        t.write(ar[0], move=False, align='center', font=('Courier', int(circ), 'bold'))
        if auto != '2' and auto != 'both':
            wait('space')
        counter += 1
        t.goto(stx + xArray[end], yArray[end])
        t.pendown()
        t.begin_fill()
        t.circle(circ)
        t.end_fill()
        t.penup()
        drawSegment(final[-1], yArray[-1] - 70, len(ar) - end, len(ar))
        i = 0
        while 2 * (i + 1) - 1 < end:
            if ar[(i + 1) * 2] > ar[(i + 1) * 2 - 1] and 2 * (i + 1) < end:
                swap = (i + 1) * 2
            else:
                swap = (i + 1) * 2 - 1
            if ar[swap] > ar[i]:
                if auto != '2' and auto != 'both':
                    wait('space')
                counter += 1
                cache = ar[swap]
                ar[swap] = ar[i]
                ar[i] = cache
                t.goto(stx + xArray[i], yArray[i])
                t.pendown()
                t.begin_fill()
                t.circle(circ)
                t.end_fill()
                t.penup()
                t.goto(stx + xArray[i] + 1, yArray[i] + (3 / (gralay)))
                t.write(ar[i], move=False, align='center', font=('Courier', int(circ), 'bold'))
                t.goto(stx + xArray[swap], yArray[swap])
                t.pendown()
                t.begin_fill()
                t.circle(circ)
                t.end_fill()
                t.penup()
                t.goto(stx + xArray[swap] + 1, yArray[swap] + (3 / (gralay)))
                t.write(ar[swap], move=False, align='center', font=('Courier', int(circ), 'bold'))
                i = swap
            else:
                i = 2 ** (layers - 1)
        end -= 1
    print('List sorted:')
    print(final)
    print('Number of operations: ' + str(counter))
    return [yArray[-1] - 140, final, counter]
def animateHeap(ar, yset):
    counter = 0
    layers = 0
    while len(ar) > 2 ** layers - 1:
        layers += 1
    gralay = layers * 0.3
    circ = 30 / gralay
    sty = yset - circ * 2
    stx = 0
    ang = 20
    yval = 100
    xArray = []
    yArray = []
    angArray = []
    xArray.append(0)
    yArray.append(sty)
    angArray.append(0)
    ind = 1
    for i in range(1, layers):
        for j in range((2 ** i) // 2):
            rad = m.radians(ang)
            xArray.append(xArray[ind // 2] - yval/m.tan(rad))
            yArray.append(sty - i * yval)
            angArray.append(rad)
            xArray.append(xArray[ind // 2] + yval/m.tan(rad))
            yArray.append(sty - i * yval)
            angArray.append(rad)
            ind += 2
        ang += 69/(layers - 1)
    # for i in angArray:
    #     print(m.degrees(i))
    i = 0
    while i < len(ar):
        k = 2 * i + 1
        l = 2 * i + 2
        t.goto(stx + xArray[i], yArray[i])
        t.pendown()
        t.begin_fill()
        t.circle(circ)
        t.end_fill()
        t.penup()
        t.goto(stx + xArray[i] + 1, yArray[i] + (3 / (gralay)))
        t.write(ar[i], move=False, align='center', font=('Courier', int(circ), 'bold'))
        if auto != '1' and auto != 'both':
            wait('space')
        counter += 1
        icache = i
        while i != 0:
            if ar[(i + 1) // 2 - 1] < ar[i]:
                cache = ar[i]
                ar[i] = ar[(i + 1) // 2 - 1]
                ar[(i + 1) // 2 - 1] = cache
                t.goto(stx + xArray[i], yArray[i])
                t.pendown()
                t.begin_fill()
                t.circle(circ)
                t.end_fill()
                t.penup()
                t.goto(stx + xArray[i] + 1, yArray[i] + (3 / (gralay)))
                t.write(ar[i], move=False, align='center', font=('Courier', int(circ), 'bold'))
                i = (i + 1) // 2 - 1
                t.goto(stx + xArray[i], yArray[i])
                t.pendown()
                t.begin_fill()
                t.circle(circ)
                t.end_fill()
                t.penup()
                t.goto(stx + xArray[i] + 1, yArray[i] + (3 / (gralay)))
                t.write(ar[i], move=False, align='center', font=('Courier', int(circ), 'bold'))
                if auto != '1' and auto != 'both':
                    wait('space')
                counter += 1
            else:
                i = 0
        i = icache
        if k < len(ar):
            t.goto(stx + xArray[i] + circ * m.sin(3 * m.pi / 2 - angArray[k]), yArray[i] + circ * (1 + m.cos(3 * m.pi / 2 - angArray[k])))
            t.pendown()
            t.goto(stx + xArray[k] + circ * m.sin(m.pi / 2 - angArray[k]), yArray[k] + circ * (1 + m.cos(m.pi / 2 - angArray[k])))
            t.penup()
        if l < len(ar):
            t.goto(stx + xArray[i] + circ * m.sin(m.pi / 2 + angArray[l]), yArray[i] + circ * (1 + m.cos(m.pi / 2 + angArray[l])))
            t.pendown()
            t.goto(stx + xArray[l] + circ * m.sin(3 * m.pi / 2 + angArray[l]), yArray[l] + circ * (1 + m.cos(3 * m.pi / 2 + angArray[l])))
            t.penup()
        i += 1
    print('Max Heap Created:')
    print(ar)
    print('Number of operations: ' + str(counter))
    drawArray(ar, yArray[-1] - 70)
    return [yArray[-1] - 140, ar, counter]
def wait(kl):
    while not key.is_pressed('space'):
            t.goto(0, 0)
    while key.is_pressed('space'):
            t.goto(0, 0)
    # i = 0
    # while 2 * i + 2 < len(ar):
    #     k = 2 * i + 1
    #     l = 2 * i + 2
    #     t.goto(stx + xArray[i] + circ * m.sin(3 * m.pi / 2 - angArray[k]), yArray[i] + circ * (1 + m.cos(3 * m.pi / 2 - angArray[k])))
    #     t.pendown()
    #     t.goto(stx + xArray[k] + circ * m.sin(m.pi / 2 - angArray[k]), yArray[k] + circ * (1 + m.cos(m.pi / 2 - angArray[k])))
    #     t.penup()
    #     t.goto(stx + xArray[i] + circ * m.sin(m.pi / 2 + angArray[l]), yArray[i] + circ * (1 + m.cos(m.pi / 2 + angArray[l])))
    #     t.pendown()
    #     t.goto(stx + xArray[l] + circ * m.sin(3 * m.pi / 2 + angArray[l]), yArray[l] + circ * (1 + m.cos(3 * m.pi / 2 + angArray[l])))
    #     t.penup()
    #     i += 1
    # if 2 * i + 1 < len(ar):
    #     k = 2 * i + 1
    #     t.goto(stx + xArray[i] + circ * m.sin(3 * m.pi / 2 - angArray[k]), yArray[i] + circ * (1 + m.cos(3 * m.pi / 2 - angArray[k])))
    #     t.pendown()
    #     t.goto(stx + xArray[k] + circ * m.sin(m.pi / 2 - angArray[k]), yArray[k] + circ * (1 + m.cos(m.pi / 2 - angArray[k])))
    #     t.penup()
auto = input('Auto:')
array = []
for i in range(15):
    array.append(r.randint(0, 99))
print('Array:')
print(array)
drawArray(array, 350)
yset = 280
out1 = animateHeap(array, yset)
yset = out1[0]
newAr = out1[1]
out2 = deleteHeap(newAr, yset)
yset = out2[0]
print('Total Operations: ' + str(out1[2] + out2[2]))
t.mainloop()