#!/usr/bin/python
import pygame
from pygame.locals import *

pygame.init()

display_width = 250
display_height = 250

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Maze Game')

# Define the colors we will use in RGBA (Alpha) format
WHITE = (255,255,255,255)
# Background Ocean water is great
BGROUND = (11,79,74,255)
# Brave fella looking for good coin
TURTLE = (50,229,98,255)
# Rocks are not good for turtle.
ROCK = (132,91,95,255)
#The great good of the sea
CHEST = (142,140,4,255)

# Starting position of TURTLE
x = 25
y = 25

# Handles keyboard controls
def event_handler():
    
    global x
    global y
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if (keys[K_ESCAPE] or keys[K_q]):
            pygame.quit()
            quit()
        if (keys[K_w]):
        	# If the next square is not the background or the chest then it is an invalid location
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

# Creates this beautiful map
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
    
    # Don't want to use global values
    mazeX = 0
    mazeY = 0

    for i in maze:
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

# Main method my dude! This will create the map and then wait for keyboard controls until you enter the chest 
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
