__author__ = 'Trenton'

import pygame

import graphics
import units

graphics.init()

import event


# back = graphics.load("stars.png")
temp = graphics.load("Easy Maze.png")
graphics.background =  pygame.transform.scale(temp, ( 1200,  600))
#graphics.load("Easy Maze.png")
#obstacle = pygame.transform.scale(graphics.background, ( 1200,  600))

george = units.George(45, 375)
george.facing = "s_down"
#george2 = units.George(100, 25)
#george2.speed = 0.4
#george2.facing = "left"

graphics.register(george)
#graphics.register(george2)

def quit(e):
	global run
	if e.type == pygame.QUIT:
		run = False
	elif e.type == pygame.KEYUP:
		if ((e.key == pygame.K_F4) and
		   (e.mod and pygame.KMOD_ALT)):
			run = False

event.register(george.handler)
event.register(quit)

clock = pygame.time.Clock()
run = True
frame = 0

while (run):


	clock.tick(30)

	event.update()
	george.update()
	#george2.update()
	graphics.update()

pygame.display.quit()