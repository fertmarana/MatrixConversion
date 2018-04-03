from pygame import gfxdraw
import pygame
pygame.init()

#Set display configuration
disp = pygame.display.set_mode((400,400))  #resolution
disp.fill((1,1,1))						   #background color
pygame.display.flip() 					   #update display

#total of pixels
n_pixels = 0

#Symmetry
def CirclePoints(x, y, color):
	global n_pixels
	offset = 200 #used to plot in the center
	gfxdraw.pixel(disp, x + offset,  y + offset, color)
	gfxdraw.pixel(disp, x + offset, -y + offset, color)
	gfxdraw.pixel(disp, -x + offset,  y + offset, color)
	gfxdraw.pixel(disp, -x + offset, -y + offset, color)
	gfxdraw.pixel(disp,  y + offset,  x + offset, color)
	gfxdraw.pixel(disp, y + offset, -x + offset, color)
	gfxdraw.pixel(disp, -y + offset,  x + offset, color)
	gfxdraw.pixel(disp, -y + offset, -x + offset, color)
	n_pixels = n_pixels + 8
	pygame.display.flip() 					#update display
	print(n_pixels)

#Middle Point Circunference
def MidPointCirc(r, color):
	x = 0
	y = r
	d = 5 / 4 - r

	CirclePoints(x, y, color)
	while (y > x):
		if (d < 0):
			# Select E
			d = d + 2 * x + 3
			x = x + 1
		else:
			#Select SE
			d = d + 2 * (x - y) + 5
			x = x + 1
			y = y - 1
		CirclePoints(x,y,color)

pygame.display.flip()				        #update display

MidPointCirc(10,(255,255,255))

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: pygame.display.quit()   #quit display window