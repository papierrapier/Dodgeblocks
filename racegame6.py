import pygame #imports pygame
import time #imports time for use in time.sleep, etc
import random #import random!

pygame.init() #initializes pygame

display_width = 800 #set surface width as variable
display_height = 600 #set surface height as variable

#color definitions not defined by default, must be added in manually with RGB map
black = (0,0,0) #define black in RGB, lowest range
white = (255,255,255) #same, highest range
red = (255,0,0) #example range for red

car_width = 58 #defines width of car as number

gameDisplay = pygame.display.set_mode((display_width,display_height)) #changed to var so that width and height can be used instead of a constant
pygame.display.set_caption('Raceblox') #changes window name/caption
clock = pygame.time.Clock() #define clock for FPS, capital C is necessary

carImg = pygame.image.load('car.png') #var = image load, must be in same directory unless fullpath is defined

def things(thingx, thingy, thingw, thingh, color): #x y params, width, height, color
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh]) #draw a rectangle, [] is location to draw

def car(x,y): #defines new var car(), provides location in range
    gameDisplay.blit(carImg,(x,y)) #draw to background, call parameter image directory (in this case, carImg)
        #since in car() the range is variable (for the car to move), must also be variable in blit (call same var)

def text_objects(text, font): #a third param for color can be added
    textSurface = font.render(text, True, black) #second param is for antialiasing True/False, then text color
    return textSurface, textSurface.get_rect()

def message_display(text): #message displayed in text
    largeText = pygame.font.Font('freesansbold.ttf',115) #font type, size
    TextSurf, TextRect = text_objects(text, largeText) #text surface and rectangle that contains it
    TextRect.center = ((display_width/2),(display_height/2)) #centers text, using display params
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2) #wait 2 seconds after displaying text

    game_loop()
    

#car crash/ending function
def crash():
    message_display('You crashed') #churns out a message when game is ended

def game_loop():
    #defines starting location of car
    x = (display_width * 0.45) #x begins at left? goes right as increase
    y = (display_height * 0.8) #Y begins at top, goes down as increase

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600 #starts obj 600px off screen
    thing_speed = 7 #each time it's redrawn there's a possibility of 7px difference
    thing_width = 100 #defines box width,
    thing_height = 100 #and height

    gameExit = False #game loop, only stopped by crash or quit command

    #event handling loop
    while not gameExit: #essentially keeps the game running as long as no bad event is called

        for event in pygame.event.get(): #obtains events, such as mouse, keyboard (event handling)
            if event.type == pygame.QUIT: #== instead of =, = is assignment, == is true equals
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: #check for key press
                if event.key == pygame.K_LEFT: #if left arrow key
                    x_change = -5 #change movement of x, - 5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5 #change movement of x, + 5


            if event.type == pygame.KEYUP: #if key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #if key is either left or right but released, then
                    x_change = 0
                    

        x += x_change #changes value of car position x depending on right or left    
    # ! draw order is necessary !
        gameDisplay.fill(white) #draw/fill background with (255,255,255) ! must come before car(), important to keep it as bottom layer

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed #adds 7 to thingy after drawn, adds 7 every time redrawn
        car(x,y) #modulate car position

        #logic handling
        if x > display_width - car_width or x < 0: #defines boundary of crash minus car_width
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height #brings back box
            thing_startx = random.randrange(0,display_width) #further randomizes box relocation

        
        if y < thing_starty+thing_height: #if topleft of box + height of box (lowest lineof box) passes car,
            print('y crossover')

            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width: #essentially draws the boundaries for which the car can have the possibility of crashing, all 4 sides of box are defined and top two sides (upright, upleft) of car are defined.
                print('x crossover')
                crash()
                
        pygame.display.update() #updates display, or use pygame.display.flip | with no parameters, updates all. flip updates all always, update has the possibility of single updates in ()
        clock.tick(60) #directly equals FPS, tied directly to x_change, y_change

game_loop()
pygame.quit() #quit with pygame
quit() #quit in IDE
