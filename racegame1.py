import pygame #imports pygame

pygame.init() #initializes pygame

display_width = 800 #set surface width as variable
display_height = 600 #set surface height as variable

#color definitions not defined by default, must be added in manually with RGB map
black = (0,0,0) #define black in RGB, lowest range
white = (255,255,255) #same, highest range
red = (255,0,0) #example range for red

gameDisplay = pygame.display.set_mode((display_width,display_height)) #changed to var so that width and height can be used instead of a constant
pygame.display.set_caption('A bit Racey') #changes window name/caption
clock = pygame.time.Clock() #define clock for FPS, capital C is necessary

carImg = pygame.image.load('car.png') #var = image load, must be in same directory unless fullpath is defined

def car(x,y): #defines new var car(), provides location in range
    gameDisplay.blit(carImg,(x,y)) #draw to background, call parameter image directory (in this case, carImg)
        #since in car() the range is variable (for the car to move), must also be variable in blit (call same var)

#defines starting location of car
x = (display_width * 0.45) #x begins at left? goes right as increase
y = (display_height * 0.8) #Y begins at top, goes down as increase


crashed = False #game loop, only stopped by crash or quit command

while not crashed: #essentially keeps the game running as long as no bad event is called

    for event in pygame.event.get(): #obtains events, such as mouse, keyboard (event handling)
        if event.type == pygame.QUIT: #== instead of =, = is assignment, == is true equals
            crashed = True #temporary loop break, quits game

# ! draw order is necessary !
    gameDisplay.fill(white) #draw/fill background with (255,255,255) ! must come before car(), important to keep it as bottom layer
    car(x,y) #modulate car position
    
    pygame.display.update() #updates display, or use pygame.display.flip | with no parameters, updates all. flip updates all always, update has the possibility of single updates in ()
    clock.tick(60) #directly equals FPS

pygame.quit() #quit with pygame
quit() #quit in IDE
