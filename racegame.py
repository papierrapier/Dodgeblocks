import pygame #imports pygame

pygame.init() #initializes pygame
gameDisplay = pygame.display.set_mode((800,600)) #self explanatory
pygame.display.set_caption('A bit Racey') #changes window name/caption
clock = pygame.time.Clock() #define clock for FPS, capital C is necessary

crashed = False #game loop, only stopped by crash or quit command

while not crashed:

    for event in pygame.event.get(): #obtains events, such as mouse, keyboard
        if event.type == pygame.QUIT: #== instead of =, = is assignment, == is true equals
            crashed = True #temporary loop break, quits game

        print(event) #prints events tracked

    pygame.display.update() #updates display, or use pygame.display.flip | with no parameters, updates all. flip updates all always, update has the possibility of single updates in ()
    clock.tick(60) #directly equals FPS

pygame.quit() #quit with pygame
quit() #quit in python
