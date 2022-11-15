'''
All cards are rendered using the turtle, there are no image files necessary (this also means no face cards).
Use draw_card([hand, suit], x, y, angle, back).
Hand is a string 1 - 10 for instance a 5 of hearts is a '5' in hand.
Suit is one character SDHC (Spade, Diamond, Heart, Club).
x and y are on a canvas of 700x650 with 0, 0 being the top left.
angle is a bearing in degrees with 0 being straight up and 180 being straight down.
back is a value 0 or 1, 0 means the card is facing you, 1 means the card is flipped over.
'''
import turtle as t
import math as m
import random as r
c = t.getcanvas()
t.hideturtle()
t.speed(0)
def draw_spade(x, y, size, ang):
    t.pencolor('BLACK')
    rang = m.radians(ang)
    t.pensize(size / 8)
    t.penup()
    t.goto(x - size * m.cos(rang) - size/3 * m.sin(rang), y - size/3 * m.cos(rang) + size * m.sin(rang))
    t.pendown()
    t.goto(x + size * m.sin(rang), y + size * m.cos(rang))
    t.goto(x + size/2 * m.sin(rang), y + size/2 * m.cos(rang))
    t.goto(x + size * m.sin(rang), y + size * m.cos(rang))
    t.goto(x + size * m.cos(rang) - size/3 * m.sin(rang), y - size/3 * m.cos(rang) - size * m.sin(rang))
    t.penup()
    t.goto(x + size/1.7 * m.cos(rang) - size/2 * m.sin(rang), y - size/2 * m.cos(rang) - size/1.7 * m.sin(rang))
    t.pensize(size)
    t.pendown()
    t.goto(x + size/3 * m.sin(rang), y + size/3 * m.cos(rang))
    t.goto(x - size/1.7 * m.cos(rang) - size/2 * m.sin(rang), y - size/2 * m.cos(rang) + size/1.7 * m.sin(rang))
    t.penup()
    t.pensize(size / 5)
    t.goto(x, y)
    t.pendown()
    t.goto(x - size * m.sin(rang), y - size * m.cos(rang))
    t.penup()
    t.pensize(3)
def draw_club(x, y, size, ang):
    t.pencolor('BLACK')
    rang = m.radians(ang)
    t.penup()
    t.goto(x + size/1.7 * m.cos(rang) - size/2.5 * m.sin(rang), y - size/2.5 * m.cos(rang) - size/1.7 * m.sin(rang))
    t.pensize(1.2 * size)
    t.pendown()
    t.forward(0)
    t.penup()
    t.goto(x + size/2 * m.sin(rang), y + size/2 * m.cos(rang))
    t.pendown()
    t.forward(0)
    t.penup()
    t.goto(x - size/1.7 * m.cos(rang) - size/2.5 * m.sin(rang), y - size/2.5 * m.cos(rang) + size/1.7 * m.sin(rang))
    t.pendown()
    t.forward(0)
    t.penup()
    t.pensize(size / 2)
    t.goto(x, y)
    t.pendown()
    t.forward(0)
    t.pensize(size / 5)
    t.goto(x - size * m.sin(rang), y - size * m.cos(rang))
    t.penup()
    t.pensize(3)
def draw_heart(x, y, size, ang):
    t.pencolor('RED')
    rang = m.radians(ang)
    t.pensize(size / 8)
    t.penup()
    t.goto(x - size * m.cos(rang) + size/3 * m.sin(rang), y + size/3 * m.cos(rang) + size * m.sin(rang))
    t.pendown()
    t.goto(x - size * m.sin(rang), y - size * m.cos(rang))
    t.goto(x - size/2 * m.sin(rang), y - size/2 * m.cos(rang))
    t.goto(x - size * m.sin(rang), y - size * m.cos(rang))
    t.goto(x + size * m.cos(rang) + size/3 * m.sin(rang), y + size/3 * m.cos(rang) - size * m.sin(rang))
    t.penup()
    t.goto(x + size/1.7 * m.cos(rang) + size/2 * m.sin(rang), y + size/2 * m.cos(rang) - size/1.7 * m.sin(rang))
    t.pensize(size)
    t.pendown()
    t.goto(x - size/3 * m.sin(rang), y - size/3 * m.cos(rang))
    t.goto(x - size/1.7 * m.cos(rang) + size/2 * m.sin(rang), y + size/2 * m.cos(rang) + size/1.7 * m.sin(rang))
    t.penup()
    t.pensize(3)
def draw_diamond(x, y, size, ang):
    t.pencolor('RED')
    rang = m.radians(ang)
    t.pensize(size / 8)
    t.penup()
    t.goto(x - 1.25 * size * m.sin(rang), y - 1.25 * size * m.cos(rang))
    t.pendown()
    t.goto(x + size * m.cos(rang), y - size * m.sin(rang))
    t.goto(x + 1.25 * size * m.sin(rang), y + 1.25 * size * m.cos(rang))
    t.goto(x - size * m.cos(rang), y + size * m.sin(rang))
    t.goto(x - 1.25 * size * m.sin(rang), y - 1.25 * size * m.cos(rang))
    t.penup()
    t.pensize(size / 4)
    t.goto(x - 1.125 * size * m.sin(rang), y - 1.125 * size * m.cos(rang))
    t.pendown()
    t.goto(x + 1.125 * size * m.sin(rang), y + 1.125 * size * m.cos(rang))
    t.penup()
    t.goto(x - 0.9 * size * m.cos(rang), y + 0.9 * size * m.sin(rang))
    t.pendown()
    t.goto(x + 0.9 * size * m.cos(rang), y - 0.9 * size * m.sin(rang))
    t.penup()
    t.pensize(size / 1.2)
    t.goto(x - 0.625 * size * m.sin(rang), y - 0.625 * size * m.cos(rang))
    t.pendown()
    t.goto(x + 0.5 * size * m.cos(rang), y - 0.5 * size * m.sin(rang))
    t.goto(x + 0.625 * size * m.sin(rang), y + 0.625 * size * m.cos(rang))
    t.goto(x - 0.5 * size * m.cos(rang), y + 0.5 * size * m.sin(rang))
    t.goto(x - 0.625 * size * m.sin(rang), y - 0.625 * size * m.cos(rang))
    t.penup()
    t.pensize(3)
def draw_card(card, x, y, angle, back):
    a = m.radians(angle)
    pattern = [[], [0, 0, 1],[0, 120, 1, 0, -120, 180],
    [0, 120, 1, 0, 0, 1, 0, -120, 180],
    [-50, 120, 1, 50, 120, 1, -50, -120, 180, 50, -120, 180],
    [-50, 120, 1, 50, 120, 1, 0, 0, 1, -50, -120, 180, 50, -120, 180],
    [-50, 120, 1, 50, 120, 1, -50, 0, 1, 50, 0, 1, -50, -120, 180, 50, -120, 180],
    [-50, 120, 1, 50, 120, 1, 0, 60, 1, -50, 0, 1, 50, 0, 1, -50, -120, 180, 50, -120, 180],
    [-50, 120, 1, 50, 120, 1, 0, 60, 1, -50, 0, 1, 50, 0, 1, 0, -60, 180, -50, -120, 180, 50, -120, 180],
    [-50, 120, 1, 50, 120, 1, -50, 50, 1, 50, 50, 1, 0, 0, 1, -50, -50, 180, 50, -50, 180, -50, -120, 180, 50, -120, 180],
    [-50, 120, 1, 50, 120, 1, 0, 70, 1, -50, 40, 1, 50, 40, 1, -50, -40, 180, 50, -40, 180, 0, -70, 180, -50, -120, 180, 50, -120, 180]]
    if card[1] == 'S' or card[1] == 'C':
        color = 'black'
    else:
        color = 'red'
    t.pencolor('BLACK')
    if back == 1:
        t.fillcolor('black')
    else:
        t.fillcolor('white')
    t.pensize(4)
    t.penup()
    t.goto(x + -125 * m.cos(a) - 175 * m.sin(a), y + -175 * m.cos(a) + 125 * m.sin(a))
    t.begin_fill()
    t.pendown()
    t.goto(x + 125 * m.cos(a) - 175 * m.sin(a), y + -175 * m.cos(a) - 125 * m.sin(a))
    t.goto(x + 125 * m.cos(a) + 175 * m.sin(a), y + 175 * m.cos(a) - 125 * m.sin(a))
    t.goto(x + -125 * m.cos(a) + 175 * m.sin(a), y + 175 * m.cos(a) + 125 * m.sin(a))
    t.goto(x + -125 * m.cos(a) - 175 * m.sin(a), y + -175 * m.cos(a) + 125 * m.sin(a))
    t.penup()
    t.end_fill()
    if back == 0:
        if card[0] == '1':
            c.create_text(x + -95 * m.cos(-a) - 140 * m.sin(-a), -y + -140 * m.cos(-a) + 95 * m.sin(-a), text = 'A', angle = -angle, font=("Arial", int(65 - len(card[0]) * 15), "normal"), fill = color)
            c.create_text(x + 95 * m.cos(-a) + 140 * m.sin(-a), -y + 140 * m.cos(-a) - 95 * m.sin(-a), text = 'A', angle = 180 - angle, font=("Arial", int(65 - len(card[0]) * 15), "normal"), fill = color)
        else:
            c.create_text(x + -95 * m.cos(-a) - 140 * m.sin(-a), -y + -140 * m.cos(-a) + 95 * m.sin(-a), text = card[0], angle = -angle, font=("Arial", int(65 - len(card[0]) * 15), "normal"), fill = color)
            c.create_text(x + 95 * m.cos(-a) + 140 * m.sin(-a), -y + 140 * m.cos(-a) - 95 * m.sin(-a), text = card[0], angle = 180 - angle, font=("Arial", int(65 - len(card[0]) * 15), "normal"), fill = color)
        if card[1] == 'S':
            for i in range(0, len(pattern[int(card[0])]), 3):
                draw_spade(x + pattern[int(card[0])][i] * m.cos(a) + pattern[int(card[0])][i + 1] * m.sin(a), y + pattern[int(card[0])][i + 1] * m.cos(a) - pattern[int(card[0])][i] * m.sin(a), 25, pattern[int(card[0])][i + 2] + angle)
            draw_spade(x + -95 * m.cos(a) + 95 * m.sin(a), y + 95 * m.cos(a) + 95 * m.sin(a), 10, angle)
            draw_spade(x + 95 * m.cos(a) - 95 * m.sin(a), y + -95 * m.cos(a) - 95 * m.sin(a), 10, 180 + angle)
        if card[1] == 'H':
            for i in range(0, len(pattern[int(card[0])]), 3):
                draw_heart(x + pattern[int(card[0])][i] * m.cos(a) + pattern[int(card[0])][i + 1] * m.sin(a), y + pattern[int(card[0])][i + 1] * m.cos(a) - pattern[int(card[0])][i] * m.sin(a), 25, pattern[int(card[0])][i + 2] + angle)
            draw_heart(x + -95 * m.cos(a) + 95 * m.sin(a), y + 95 * m.cos(a) + 95 * m.sin(a), 10, angle)
            draw_heart(x + 95 * m.cos(a) - 95 * m.sin(a), y + -95 * m.cos(a) - 95 * m.sin(a), 10, 180 + angle)
        if card[1] == 'D':
            for i in range(0, len(pattern[int(card[0])]), 3):
                draw_diamond(x + pattern[int(card[0])][i] * m.cos(a) + pattern[int(card[0])][i + 1] * m.sin(a), y + pattern[int(card[0])][i + 1] * m.cos(a) - pattern[int(card[0])][i] * m.sin(a), 25, pattern[int(card[0])][i + 2] + angle)
            draw_diamond(x + -95 * m.cos(a) + 95 * m.sin(a), y + 95 * m.cos(a) + 95 * m.sin(a), 10, angle)
            draw_diamond(x + 95 * m.cos(a) - 95 * m.sin(a), y + -95 * m.cos(a) - 95 * m.sin(a), 10, 180 + angle)
        if card[1] == 'C':
            for i in range(0, len(pattern[int(card[0])]), 3):
                draw_club(x + pattern[int(card[0])][i] * m.cos(a) + pattern[int(card[0])][i + 1] * m.sin(a), y + pattern[int(card[0])][i + 1] * m.cos(a) - pattern[int(card[0])][i] * m.sin(a), 25, pattern[int(card[0])][i + 2] + angle)
            draw_club(x + -95 * m.cos(a) + 95 * m.sin(a), y + 95 * m.cos(a) + 95 * m.sin(a), 10, angle)
            draw_club(x + 95 * m.cos(a) - 95 * m.sin(a), y + -95 * m.cos(a) - 95 * m.sin(a), 10, 180 + angle)
deck = 6
AllHand = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
AllSuit = ['S', 'H', 'D', 'C']
orient = [-50, -30, -10, 10, 30, 50]
horizontal = [-125, -75, -25, 25, 75, 100]
vertical = [-25, 5, 2, -2, -15, -50, 0]
t.tracer(0, 0)
def main(counter):
    hand = []
    for i in range(deck):
        hand.append(r.randint(1, 10))
    suits = 'SCHD'
    suit = []
    for i in range(deck):
        suit.append(suits[r.randint(0, 3)])
    c.delete('all')
    t.clear()
    if counter == 0:
        c.delete('all')
        t.clear()
    for i in range(len(hand)):
        draw_card([str(hand[i]), suit[i]], horizontal[i], vertical[i], orient[i], 0)
        # draw_card([str(hand[i]), suit[i]], r.randint(-300, 300), r.randint(-300, 300), orient[i], 0)
        # draw_card([str(hand[i]), suit[i]], r.randint(-500, 500), r.randint(-300, 300), r.randint(0, 360), 0)
        t.ontimer(t.update(), 100)
counter = 0
# Uncomment this to have infinite random cards
# while True:
#     draw_card([AllHand[r.randint(0, 9)], AllSuit[r.randint(0, 3)]], r.randint(-500, 500), r.randint(-300, 300), r.randint(0, 360), 0)
#     t.ontimer(t.update(), 100)
main(counter)
t.mainloop()