import pygame
import time

#Initialization
pygame.font.init()

#Creating some colors
titleScreen_colour = (169,169,169)

#Setting up the window
win_x = 800
win_y = 600
window = pygame.display.set_mode(size=(win_x, win_y), flags=0, display=0, vsync=0)
pygame.display.set_caption('Battle Jack')
pygame.display.set_mode((win_x, win_y))
window.fill(titleScreen_colour)
pygame.display.flip()

#Sets the while loop
running = True
while running:

	#Checks and processes any pending event
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
        	running = False

    #Title Screen Banner
    title_font = pygame.font.SysFont('arial', 32)
    text = title_font.render('Battle Jack', False, (0,0,0))
    window.blit(text, (win_x/2,0))


    #Title screen Buttons
    pygame.draw.rect(window,(0,0,0),[(win_x/2)-50,(win_y*0.65)-20,100,40])
    pygame.draw.rect(window,(0,0,0),[(win_x/2)-50,(win_y*0.80)-20,100,40])

    pygame.display.update()

