'''
requires pygame (pip install pygame)
also uses a ton of assets that i haven't provided because oops, and uses filepath names because i'm dumb
so it won't actually work if you download it, but it's the thought that counts
wordle clone, never finished but it works just fine
'''
import math as m
import pygame as p
import random as r
import time as t
p.init()
G = p.display.set_mode((800,800))
G.fill((255,255,255))
p.display.set_caption('Wordle')
clock = p.time.Clock()
crashed = False
def init():
    global lookupX, lookupY, lookupSizeX, lookupSizeY, lookupType, size, row, col, current, gu, addcache, clearcache, addframes, strout, anitype, addAni, shakeAni, flipAni, jumpAni, words, b1, wordOp, target, seq, jtrig
    gu = []
    for i in range(30):
        gu.append(127)
    row = 0
    col = 0
    size = 70
    current = 0
    addcache = []
    clearcache = []
    addframes = []
    seq = 0
    strout = ''
    for i in range(30):
        addframes.append(0)
    anitype = []
    for i in range(30):
        anitype.append(0)
    addAni = [0, 4, 10]
    shakeAni = [-2, 2, 5, -5, -7, 7, 5, -5, -3, 3, 2, -2]
    flipAni = [1, 0.8, 0.5, 0.3, 0, 0.3, 0.5, 0.8, 1]
    jumpAni = [6, 5, 4, -3, -5, -7, -3, 2, 4, -3]
    jtrig = 0
    words = open(r'C:\PythonPrograms\Libraries\5LettersMore.txt').read()
    b1 = p.image.load(r'C:\PythonPrograms\Images\Wordle\White.png')
    b1 = p.transform.scale(b1, (size, size))
    wordOp = open(r'C:\PythonPrograms\Libraries\5LettersCommon.txt').read()
    wordOp = wordOp.split()
    target = wordOp[r.randint(0,len(wordOp) - 1)]
    print(target)
    lookupX = []
    lookupY = []
    lookupSizeX = []
    lookupSizeY = []
    lookupType = []
    for j in range(6):
        for i in range(5):
            # p.draw.rect(G,(211,214,218),(400 - 2.5 * (size + (size/10)) + i * (size + (size/10)),120 + j * (size + (size/10)),size,size),2)
            tin = p.image.load(r'C:\PythonPrograms\Images\Wordle\Null.png')
            tin = p.transform.scale(tin, (size, size))
            lookupX.append(400 - 2.5 * (size + (size/10)) + i * (size + (size/10)))
            lookupY.append(120 + j * (size + (size/10)))
            lookupSizeX.append(size)
            lookupSizeY.append(size)
            lookupType.append(0)
            G.blit(tin,(400 - 2.5 * (size + (size/10)) + i * (size + (size/10)), 120 + j * (size + (size/10))))
def resetScreen():
    G.fill((255,255,255))
    lookupX = []
    lookupY = []
    lookupSizeX = []
    lookupSizeY = []
    lookupType = []
    for j in range(6):
        for i in range(5):
            lookupX.append(400 - 2.5 * (size + (size/10)) + i * (size + (size/10)))
            lookupY.append(120 + j * (size + (size/10)))
            lookupSizeX.append(size)
            lookupSizeY.append(size)
            lookupType.append(0)
            # p.draw.rect(G,(211,214,218),(400 - 2.5 * (size + (size/10)) + i * (size + (size/10)),120 + j * (size + (size/10)),size,size),2)
            tin = p.image.load('C:\PythonPrograms\Images\Wordle\\' + chr(gu[j * 5 + i] - 32) + '.png')
            tin = p.transform.scale(tin, (size, size))
            G.blit(tin,(400 - 2.5 * (size + (size/10)) + i * (size + (size/10)), 120 + j * (size + (size/10))))
# def shake(r1):
    # ints = 1
    # sin = 0
    # con = 0
    # time = 13
    # yp = 120 + r1 * (size + (size/10))
    # for k in range(4):
        # ints += 0
        # for j in range(time):
            # conb = con
            # con += (j  - (time - 1) / 2) * ints * (j % 3 == 0)
            # for i in range(row * 5, row * 5 + 5):
                # G.blit(b1, (400 - 2.5 * (size + (size/10)) + i % 5 * (size + (size/10)) + conb, yp))
                # # p.draw.rect(G,(0,0,0),(400 - 2.5 * (size + (size/10)) + i * (size + (size/10)) + conb, 120 + r1 * (size + (size/10)),size,size))
                # ne = p.image.load('C:\PythonPrograms\Images\Wordle\\' + chr(gu[i] - 32) + '.png')
                # ne = p.transform.scale(ne, (size, size))
                # G.blit(ne, (400 - 2.5 * (size + (size/10)) + i % 5 * (size + (size/10)) + con, yp))
                # p.display.update()
def eval():
    global row, col, gu, addframes, addcache, clearcache, anitype, lookupX, lookupSizeX, lookupSizeY, strout
    for i in clearcache:
        r1 = b1
        r1 = p.transform.scale(r1, (lookupSizeX[i], lookupSizeY[i]))
        G.blit(r1, (lookupX[i] - (lookupSizeX[i] - size)/2, lookupY[i] - (lookupSizeY[i] - size)/2))
    clearcache = []
    addframes = []
    for i in range(30):
        addframes.append(0)
    anitype = []
    for i in range(30):
        anitype.append(0)
    if current % 5 == 0 and current//5 == row + 1:
        guess = ''
        lookupX = []
        for i in range(30):
            lookupX.append(400 - 2.5 * (size + (size/10)) + (i % 5) * (size + (size/10)))
        for i in addcache:
            r1 = p.image.load('C:\PythonPrograms\Images\Wordle\\' + chr(gu[i] - 32) + '.png')
            r1 = p.transform.scale(r1, (size, size))
            G.blit(r1, (lookupX[i], lookupY[i]))
        addcache = []
        lookupSizeX = []
        lookupSizeY = []
        for i in range(30):
            lookupSizeX.append(size)
            lookupSizeY.append(size)
        addframes[row * 5] = len(flipAni)
        anitype[row * 5] = 3
        addcache.append(row * 5)
        clearcache.append(row * 5)
        for i in range(row * 5, row * 5 + 5):
            guess += chr(gu[i])
        if guess in words:
            out = []
            cache = []
            for i in range(len(target)):
                cache.append(target[i])
            for i in range(len(guess)):
                if guess[i] in cache:
                    if target[i] == guess[i]:
                        out.append('4')
                        del cache[cache.index(guess[i])]
                    else:
                        out.append('2')
                else:
                    out.append('2')
            for i in range(len(target)):
                if guess[i] in cache and out[i] != '4':
                    out[i] = '3'
                    del cache[cache.index(guess[i])]
            strout = ''
            for i in out:
                strout += i
            # for i in range(row * 5, row * 5 + 5):
                # t1 = p.image.load('C:\PythonPrograms\Images\Wordle\\' + chr(gu[i] - 32) + strout[i % 5] + '.png')
                # t1 = p.transform.scale(t1, (size, size))
                # G.blit(t1, (400 - 2.5 * (size + (size/10)) + i % 5 * (size + (size/10)),120 + row * (size + (size/10))))
            row += 1
            col = 0
        else:
            addcache = []
            clearcache = []
            lookupSizeX = []
            lookupSizeY = []
            for i in range(30):
                lookupSizeX.append(size)
                lookupSizeY.append(size)
            for i in range(row * 5, row * 5 + 5):
                addframes[i] = len(shakeAni)
                anitype[i] = 2
                addcache.append(i)
                clearcache.append(i)
            lookupX = []
            for i in range(30):
                lookupX.append(400 - 2.5 * (size + (size/10)) + (i % 5) * (size + (size/10)))
    else:
        addcache = []
        lookupSizeX = []
        lookupSizeY = []
        for i in range(30):
            lookupSizeX.append(size)
            lookupSizeY.append(size)
        for i in range(row * 5, row * 5 + 5):
            addframes[i] = len(shakeAni)
            anitype[i] = 2
            addcache.append(i)
            clearcache.append(i)
        lookupX = []
        for i in range(30):
            lookupX.append(400 - 2.5 * (size + (size/10)) + (i % 5) * (size + (size/10)))
def control():
    global col, gu, crashed, addframes, current, anitype, addcache, clearcache
    kl = 0
    for event in p.event.get():
        if event.type == p.KEYDOWN:
            k = event.key
            # resetScreen()
            if k != kl and currentlyAnimating == 0:
                if k == 39:
                    kl = k
                    k = 105
                if k == 8:
                    kl = k
                    if current % 5 > 0 or current//5 == row + 1:
                        current -= 1
                        gu[current] = 127
                        t1 = p.image.load(r'C:\PythonPrograms\Images\Wordle\Null.png')
                        t1 = p.transform.scale(t1, (size, size))
                        G.blit(t1, (400 - 2.5 * (size + (size/10)) + (col - 1) * (size + (size/10)),120 + row * (size + (size/10))))
                        if len(clearcache) > 0:
                            r2 = clearcache[len(clearcache) - 1]
                            r1 = b1
                            r1 = p.transform.scale(r1, (lookupSizeX[r2], lookupSizeY[r2]))
                            G.blit(r1, (lookupX[r2] - (lookupSizeX[r2] - size)/2, lookupY[r2] - (lookupSizeY[r2] - size)/2))
                            G.blit(t1, (400 - 2.5 * (size + (size/10)) + (col - 1) * (size + (size/10)),120 + row * (size + (size/10))))
                            addcache.pop()
                            clearcache.pop()
                            addframes[r2] = 0
                            anitype[r2] = 0
                elif k == 13:
                    kl = k
                    if strout == '44444':
                        init()
                    else:
                        eval()
                elif k > 96 and k < 123 and (current)//5 < row + 1 and strout != '44444':
                    kl = k
                    gu[current] = k
                    current += 1
                    t1 = p.image.load('C:\PythonPrograms\Images\Wordle\\' + chr(k - 32) + '.png')
                    t1 = p.transform.scale(t1, (size, size))
                    addframes[row * 5 + col] = len(addAni)
                    anitype[row * 5 + col] = 1
                    addcache.append(row * 5 + col)
                    clearcache.append(row * 5 + col)
                    #G.blit(t1, (400 - 2.5 * (size + (size/10)) + col * (size + (size/10)),120 + row * (size + (size/10))))
                col = current % 5 + 5 * (current//5 == row + 1)
        if event.type == p.QUIT:
            crashed = True
def loop():
    global addframes, currentlyAnimating, seq, jtrig
    if counter % 3 == 0:
        currentlyAnimating = 0
        if (len(clearcache) > 0 or len(addcache) > 0):
            currentlyAnimating = 0
            for i in clearcache:
                r1 = b1
                r1 = p.transform.scale(r1, (lookupSizeX[i], lookupSizeY[i]))
                G.blit(r1, (lookupX[i] - (lookupSizeX[i] - size)/2, lookupY[i] - (lookupSizeY[i] - size)/2))
                if addframes[i] > 0:
                    if anitype[i] == 1:
                        lookupSizeX[i] = size + addAni[addframes[i] - 1]
                        lookupSizeY[i] = size + addAni[addframes[i] - 1]
                    elif anitype[i] == 2:
                        lookupX[i] += shakeAni[addframes[i] - 1]
                    elif anitype[i] == 3:
                        currentlyAnimating = 1
                        lookupSizeY[i] = int(size * flipAni[addframes[i] - 1])
                        if flipAni[addframes[i] - 1] == 0:
                            lookupType[i] = 1
                        if addframes[i] == 2:
                            if seq < 4:
                                jtrig = 0
                                addframes[i + 1] = len(flipAni)
                                anitype[i + 1] = 3
                                addcache.append(i + 1)
                                clearcache.append(i + 1)
                                seq += 1
                            else:
                                print('done1')
                                jtrig = 1
                                seq = 0
                        if addframes[i] > len(flipAni) - 2 and jtrig == 1:
                            print('done3')
                            jtrig = 2
                    elif anitype[i] == 4:
                        currentlyAnimating = 1
                        lookupY[i] += jumpAni[addframes[i] - 1]
                else:
                    if anitype[i] == 3:
                        if jtrig == 2 and strout == '44444':
                            print('done2')
                            for j in range(5):
                                addframes[i - 4 + j] = len(jumpAni)
                                anitype[i - 4 + j] = 4
                                addcache.append(i - 4 + j)
                                clearcache.append(i - 4 + j)
                    anitype[i] = 0
                    del clearcache[clearcache.index(i)]
            for i in addcache:
                if lookupType[i] == 1:
                    r1 = p.image.load('C:\PythonPrograms\Images\Wordle\\' + chr(gu[i] - 32) + strout[i % 5] + '.png')
                else:
                    r1 = p.image.load('C:\PythonPrograms\Images\Wordle\\' + chr(gu[i] - 32) + '.png')
                r1 = p.transform.scale(r1, (lookupSizeX[i], lookupSizeY[i]))
                G.blit(r1, (lookupX[i] - (lookupSizeX[i] - size)/2, lookupY[i] - (lookupSizeY[i] - size)/2))
                if addframes[i] > 0:
                    addframes[i] -= 1
                else:
                    # resetScreen()
                    del addcache[addcache.index(i)]
        p.display.update()
init()
counter = 0
while not crashed:
    counter += 1
    control()
    loop()
    # if counter % 300 == 0:
        # resetScreen()
    # for event in p.event.get():
        # if event.type == p.QUIT:
                # crashed = True
    clock.tick(60)
p.quit()
quit()
