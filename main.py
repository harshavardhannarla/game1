import pygame
import sys
import random
import math
from pygame.locals import *
from config import *


pygame.init()
screen = pygame.display.set_mode((650, 770))

# tool bar

pygame.display.set_caption("ocean fighters")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('boy.png')
px = 250
py = 700
vel = 10


# ship
obstImg = []
sx = []
sy = []
sxc = []
num_of_enemies = 18

# score
score_value_1 = 0
score_value_2 = 0
score_value = 0

counter1 = 0
counter2 = 0

# placing obstacles in the particular positions

for i in range(num_of_enemies):
    if 0 <= i <= 9:
        obstImg.append(pygame.image.load('boat.png'))
    if 10 <= i <= 17:
        obstImg.append(pygame.image.load('skull.png'))
    sx.append(random.randint(0, 650))
    sxc.append(5)
    if 0 <= i <= 1:
        sy.append(70)
    elif 2 <= i <= 3:
        sy.append(210)
    elif 4 <= i <= 5:
        sy.append(350)
    elif 6 <= i <= 7:
        sy.append(490)
    elif 8 <= i <= 9:
        sy.append(630)
    elif 10 <= i <= 11:
        sy.append(140)
    elif 12 <= i <= 13:
        sy.append(280)
    elif 14 <= i <= 15:
        sy.append(420)
    elif 16 <= i <= 17:
        sy.append(560)

k = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def obst(x, y, p):
    screen.blit(obstImg[p], (x, y))


def whatthescoreis():
    global score_value
    if p % 2 == 1:
        if 630 <= py + 32 <= 770:
            score_value = 0
        if 560 <= py + 32 <= 630:
            score_value = 20
        if 490 <= py + 32 <= 560:
            score_value = 30
        if 420 <= py + 32 <= 490:
            score_value = 50
        if 350 <= py + 32 <= 420:
            score_value = 60
        if 280 <= py + 32 <= 350:
            score_value = 80
        if 210 <= py + 32 <= 280:
            score_value = 90
        if 140 <= py + 32 <= 210:
            score_value = 110
        if 70 <= py + 32 <= 140:
            score_value = 120
        if 0 <= py + 32 <= 70:
            score_value = 140

    if p % 2 == 0:
        if 700 <= py + 32 <= 770:
            score_value = 140
        if 630 <= py + 32 <= 700:
            score_value = 120
        if 560 <= py + 32 <= 630:
            score_value = 110
        if 490 <= py + 32 <= 560:
            score_value = 90
        if 420 <= py + 32 <= 490:
            score_value = 80
        if 350 <= py + 32 <= 420:
            score_value = 60
        if 280 <= py + 32 <= 350:
            score_value = 50
        if 210 <= py + 32 <= 280:
            score_value = 30
        if 140 <= py + 32 <= 210:
            score_value = 20
        if 0 <= py + 32 <= 140:
            score_value = 0


def show_score(x, y):

    score = font7.render("Round Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def show_level():

    if p == 1 or p == 2:
      l = 1
    if p == 3 or p == 4:
      l = 2
    if p == 5 or p == 6:
      l = 3
    level = font8.render("LEVEL:" + str(l), True, (0, 0, 0))
    screen.blit(level, (250, 0))


def isCollision(a, b, x, y):
    xdistance = math.fabs(a - x)
    ydistance = math.fabs(b - y)

    if xdistance <= 35 and ydistance <= 35:
        return True
    else:
        return False


def drawwin():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, sand, (0, 0, 650, 70))
    pygame.draw.rect(screen, water, (0, 70, 650, 70))
    pygame.draw.rect(screen, sand, (0, 140, 650, 70))
    pygame.draw.rect(screen, water, (0, 210, 650, 70))
    pygame.draw.rect(screen, sand, (0, 280, 650, 70))
    pygame.draw.rect(screen, water, (0, 350, 650, 70))
    pygame.draw.rect(screen, sand, (0, 420, 650, 70))
    pygame.draw.rect(screen, water, (0, 490, 650, 70))
    pygame.draw.rect(screen, sand, (0, 560, 650, 70))
    pygame.draw.rect(screen, water, (0, 630, 650, 70))
    pygame.draw.rect(screen, sand, (0, 700, 650, 70))
    pygame.draw.rect(screen, water, (0, 770, 650, 70))


p = 1
running = True
a = 1

while running:
    if a == 1:
        if p % 2 == 1:
            counter1 += 1
        else:
            counter2 += 1

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and px > vel:
            px -= vel
        if keys[pygame.K_RIGHT] and px < 650 - 32 - vel:
            px += vel
        if keys[pygame.K_UP] and py > vel:
            py -= vel
        if keys[pygame.K_DOWN] and py < 770 - 32 - vel:
            py += vel
        whatthescoreis()
        drawwin()
        player(px, py)
        show_score(0, 0)
        show_level()
        for i in range(num_of_enemies):
            if 0 <= i <= 9:
                sx[i] += sxc[i]

                if sx[i] >= 650:
                    sx[i] = 0
                obst(sx[i], sy[i], i)
            if 10 <= i <= 17:
                obst(sx[i], sy[i], i)

        for i in range(num_of_enemies):
            col = isCollision(px, py, sx[i] + 32, sy[i] + 32)
            if col:
                a = 0
                k = 0
        if p % 2 == 1 and py <= 20:
            a = 0
            k = 0
        if p % 2 == 0 and py >= 720:
            a = 0
            k = 0

    if a == 0:
        screen = pygame.display.set_mode((650, 770))
        screen.fill((0, 0, 0))
        if k == 0:
            if p % 2 == 1: score_value_1 += score_value
            if p % 2 == 0: score_value_2 += score_value
            k = 1
        screen.blit(font5.render("Round over", True, (255, 255, 255)), (200, 150))
        screen.blit(font6.render("Press F1 to continue", True, (255, 255, 255)), (150, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F1]:
            p += 1
            if p % 2 == 1:
                px = 250
                py = 720
                if p == 3:
                    for i in range(num_of_enemies):
                        sxc[i] = 10
                if p == 5:
                    for i in range(num_of_enemies):
                        sxc[i] = 15
            if p % 2 == 0:
                px = 250
                py = 0
                if p == 4:
                    for i in range(num_of_enemies):
                        sxc[i] = 10
                if p == 6:
                    for i in range(num_of_enemies):
                        sxc[i] = 15
            if p == 7:
                a = 2
            else:
                a = 1
    if a == 2:
        screen = pygame.display.set_mode((650, 770))
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if score_value_1 > score_value_2:
            fas = "Player 1 Won the game"
        elif score_value_1 < score_value_2:
            fas = "Player 2 Won the game"
        elif score_value_1 == score_value_2:
            if counter1 > counter2:
                fas = "Player 1 Won the game"
            else:
                fas = "Player 2 Won the game"


        screen.blit(font1.render("GAME OVER", True, (255, 255, 255)), (200, 150))
        screen.blit(font2.render("Player1", True, (255, 255, 255)), (100, 240))
        screen.blit(font2.render("Player2", True, (255, 255, 255)), (400, 240))
        screen.blit(font3.render("score:" + str(score_value_1), True, (255, 255, 255)), (100, 320))
        screen.blit(font3.render("score:" + str(score_value_2), True, (255, 255, 255)), (400, 320))
        screen.blit(font3.render(fas, True, (255, 255, 255)), (130, 420))
    pygame.display.update()
