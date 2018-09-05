#!/usr/bin/python
import pygame
from pygame.locals import *

pygame.init()

display_width = 250
display_height = 250

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Maze Game')

# Define the colors we will use in RGB format
BLACK = (0,0,0)
WHITE = (255,255,255,255)
BGROUND = (11,79,74,255)
TURTLE = (50,229,98,255)
ROCK = (132,91,95,255)
CHEST = (142,140,4,255)

# Starting position of TURTLE
x = 25
y = 25

def event_handler():
    
    global x
    global y
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if (keys[K_ESCAPE] or keys[K_q]):
            pygame.quit()
            quit()
        if (keys[K_w]):
            #print("W was hit")
            #print(sorted(game_display.get_at((x, y-25))))
            #print(sorted(BGROUND))
            #print(sorted(CHEST))
            if y <= 0 or ((sorted(game_display.get_at((x, y-25))) != sorted(BGROUND)) and (sorted(game_display.get_at((x, y-25))) != sorted(CHEST))):
                print("This is an invalid move")
            else:
                pygame.draw.rect(game_display, BGROUND, [x, y, 25, 25])
                y -= 25
                pygame.draw.rect(game_display, TURTLE, [x, y, 25, 25])
        if (keys[K_s]):
            #print("S was hit")
            if y >= 250 or ((sorted(game_display.get_at((x, y+25))) != sorted(BGROUND)) and (sorted(game_display.get_at((x, y+25))) != sorted(CHEST))):
                print("This is an invalid move")
            else:
                pygame.draw.rect(game_display, BGROUND, [x, y, 25, 25])
                y += 25
                pygame.draw.rect(game_display, TURTLE, [x, y, 25, 25])
        if (keys[K_a]):
            #print("A was hit")
            if x <= 0 or ((sorted(game_display.get_at((x-25, y))) != sorted(BGROUND)) and (sorted(game_display.get_at((x-25, y))) != sorted(CHEST))):
                print("This is an invalid move")
            else:
                pygame.draw.rect(game_display, BGROUND, [x, y, 25, 25])
                x -= 25
                pygame.draw.rect(game_display, TURTLE, [x, y, 25, 25])        
        if (keys[K_d]):
            #print("D was hit")
            #if x >= 250 or get_Maze_Pos() != 2:
            if x >= 250 or ((sorted(game_display.get_at((x+25, y))) != sorted(BGROUND)) and (sorted(game_display.get_at((x+25, y))) != sorted(CHEST))):
                print("This is an invalid move")
            else:
                pygame.draw.rect(game_display, BGROUND, [x, y, 25, 25])
                x += 25
                pygame.draw.rect(game_display, TURTLE, [x, y, 25, 25])

def create_map():
    # 1 = ROCK | 2 = BG | 3 = TURTLE | 4 = CHEST
    maze = [ 1,1,1,1,1,1,1,1,1,1,
             1,3,2,2,2,2,2,2,1,1,
             1,1,1,1,2,1,1,1,1,1,
             1,2,2,2,2,1,1,1,2,1,
             1,2,1,1,1,1,2,2,2,1,
             1,2,2,2,2,2,2,1,2,1,
             1,2,2,1,1,1,2,1,2,1,
             1,2,1,2,2,1,2,1,2,1,
             1,2,2,2,1,1,2,1,4,1,
             1,1,1,1,1,1,1,1,1,1,]
    #pygame.draw.rect(game_display, TURTLE, [0, 0, 25, 25])
    mazeX = 0
    mazeY = 0
    for i in maze:
        #mazeX = 0
        #mazeY = 0
        #print("Value is {}".format(i))
        if mazeX >= 250:
            #print("jump")
            mazeX = 0
            mazeY += 25
        if i == 1:
            pygame.draw.rect(game_display, ROCK, [mazeX, mazeY, 25, 25])
        elif i == 3:
            pygame.draw.rect(game_display, TURTLE, [mazeX, mazeY, 25, 25])
        elif i == 4:
            pygame.draw.rect(game_display, CHEST, [mazeX, mazeY, 25, 25])
        mazeX = mazeX + 25

def maze():
    maze = [ 1,1,1,1,1,1,1,1,1,1,
             1,3,2,2,2,2,2,2,1,1,
             1,1,1,1,2,1,1,1,1,1,
             1,2,2,2,2,1,1,1,2,1,
             1,2,1,1,1,1,2,2,2,1,
             1,2,2,2,2,2,2,1,2,1,
             1,2,2,1,1,1,2,1,2,1,
             1,2,1,2,2,1,2,1,2,1,
             1,2,2,2,1,1,2,1,4,1,
             1,1,1,1,1,1,1,1,1,1,]

def getMazePos():
    return 1

def main():
    game_display.fill(BGROUND)
    create_map()

    bool flag = True

    while flag:
        event_handler()
        pygame.display.update()
        if (x == 200 and y == 200):
            print("You have won this turtle game!!")
            pygame.quit()
            quit()
            flag = False


main()
