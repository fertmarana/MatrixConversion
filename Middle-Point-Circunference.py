from pygame import gfxdraw
import pygame
pygame.init()

#Set display configuration
disp = pygame.display.set_mode((700,400))  #resolution
disp.fill((1,1,1))						   #background color 
pygame.display.flip() 					   #update display

#total of pixels
n_pixels = 0

#Symmetry
def CirclePoints(x, y, color): 
	gfxdraw.pixel(disp, x,  y, color)
	gfxdraw.pixel(disp, x, -y, color)
	gfxdraw.pixel(disp, -x,  y, color)
	gfxdraw.pixel(disp, -x, -y, color)
	gfxdraw.pixel(disp,  y,  x, color)
	gfxdraw.pixel(disp, y, -x, color)
	gfxdraw.pixel(disp, -y,  x, color)
	gfxdraw.pixel(disp, -y, -x, color)
	n_pixels = n_pixels + 8
	pygame.display.flip() 					#update display

#Middle Point Circunference
def MidPointCirc(r, color): 
	x = 0
	y = r
	d = 1 - r

	CirclePoints(x, y, color);
	while (y > x):
		if (d < 0):
			#Select E 
			d = d + 2 * x + 3
			x = x + 1
		else:
			#Select  SE 
			d = d + 2 * (x - y) + 5
			x = x + 1
		CirclePoints(x, y, color)

pygame.display.flip()				        #update display
