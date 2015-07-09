import pygame #imports pygame
import time #imports time for use in time.sleep, etc
import random #import random!

pygame.init() #initializes pygame

display_width = 800 #set surface width as variable
display_height = 600 #set surface height as variable

#color definitions not defined by default, must be added in manually with RGB map
black = (0,0,0) #define black in RGB, lowest range
white = (255,255,255) #same, highest range

red = (200,0,0) #example range for red
green = (0,200,0) #general green definition

bright_red = (255,0,0) #color defined for button hover
bright_green= (0,255,0) #same

block_color = (53,115,255) #defines color of block as blue

car_width = 58 #defines width of car as number

gameDisplay = pygame.display.set_mode((display_width,display_height)) #changed to var so that width and height can be used instead of a constant
pygame.display.set_caption('Raceblox') #changes window name/caption
clock = pygame.time.Clock() #define clock for FPS, capital C is necessary

carImg = pygame.image.load('car.png') #var = image load, must be in same directory unless fullpath is defined

pause = False
#crash = True

def things_dodged(count): #every time a box is reset/redrawn, add 1 to count
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: '+str(count), True, black) #displays Dodged, plus count converted into string, then antialiasing check, and font color
    gameDisplay.blit(text,(0,0)) #draws text, text location 

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

    
    largeText = pygame.font.Font('freesansbold.ttf',115) #reuses text defined in message_display, better to define text and different sizes/types earlier in code (temporary)
    TextSurf, TextRect = text_objects("You Crashed", largeText) 
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white) #keep outside for loop, within while loop
        

        button("Play Again?",150,450,100,50,green,bright_green,game_loop) #remember, x,y,w,h,ic,ac game_loop is called to begin game
        button("Quit",550,450,100,50,red,bright_red,quitgame) #yay, reusing functions! quitgame is defined above

        pygame.display.update()
        clock.tick(15) #tick for 15 seconds

def button(msg,x,y,w,h,ic,ac,action=None): #button message(msg), param locations(x,y), width(w), height(h), inactive color(ic), active color(ac)
    #buttons to begin game
    mouse = pygame.mouse.get_pos() #obtain position of mouse, defined
    click = pygame.mouse.get_pressed() #checks to see if mouse clicks, left right and middle buttons
    #print(click)

    
    if x+w > mouse[0] > x and y+h > mouse[1] > y: #inbetween x + xwidth and inbetween y + ywidth
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h)) #draw, color, coordinates, with bright_green instead of green
        if click[0] == 1 and action != None: #if click is measured, and if action does not equal none
            action() 
        #highlight + alt+3 = multiline comment, alt+4 to uncomment
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
                
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h)) #normal green when not

    #adds and centers text**
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) ) #center on x first (x + xwidth / 2)
    gameDisplay.blit(textSurf, textRect) #should center 'GO!' over button

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    

def paused(): #Pause Screen loop

    largeText = pygame.font.Font('freesansbold.ttf',115) #reuses text defined in message_display, better to define text and different sizes/types earlier in code (temporary)
    TextSurf, TextRect = text_objects("Paused", largeText) 
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white) #keep outside for loop, within while loop
        

        button("Continue",150,450,100,50,green,bright_green,unpause) #remember, x,y,w,h,ic,ac game_loop is called to begin game
        button("Quit",550,450,100,50,red,bright_red,quitgame) #yay, reusing functions! quitgame is defined above

        pygame.display.update()
        clock.tick(15) #tick for 15 seconds

def game_intro(): #runs once, applies well to adding menus (controls, volume) in PauseScreen, etc

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white) #keep outside for loop, within while loop
        largeText = pygame.font.Font('freesansbold.ttf',115) #reuses text defined in message_display, better to define text and different sizes/types earlier in code (temporary)
        TextSurf, TextRect = text_objects("DODGE, BRO", largeText) 
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop) #remember, x,y,w,h,ic,ac game_loop is called to begin game
        button("Quit?",550,450,100,50,red,bright_red,quitgame) #yay, reusing functions! quitgame is defined above

        pygame.display.update()
        clock.tick(15) #tick for 15 seconds
    



def game_loop():
    global pause
    
    #defines starting location of car
    x = (display_width * 0.45) #x begins at left, goes right as increase
    y = (display_height * 0.8) #Y begins at top, goes down as increase

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600 #starts box 600px off screen
    thing_speed = 4 #speed of box travel
    thing_width = 100 #defines box width,
    thing_height = 100 #and height

    thingCount = 1 #!CHALLENGE MODIFIER! use for loop? OR for thing in range thingCount

    dodged = 0 #starting score

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
                if event.key == pygame.K_RIGHT:
                    x_change = 5 #change movement of x, + 5
                if event.key == pygame.K_p: #if the key 'p' is pressed,
                    pause = True
                    paused()


            if event.type == pygame.KEYUP: #if key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #if key is either left or right but released, then
                    x_change = 0
                    

        x += x_change #changes value of car position x depending on right or left    
    # ! draw order is necessary !
        gameDisplay.fill(white) #draw/fill background with (255,255,255) ! must come before car(), important to keep it as bottom layer

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color) #remember, color is now block_color
        thing_starty += thing_speed #adds 7 to thingy after drawn, adds 7 every time redrawn
        car(x,y) #modulate car position
        things_dodged(dodged) #calculates score, make sure it's drawn last

        #logic handling
        if x > display_width - car_width or x < 0: #defines boundary of crash minus car_width
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height #brings back box
            thing_startx = random.randrange(0,display_width) #further randomizes box relocation
            dodged += 1 #computes score
            thing_speed += 1 #adds 1 speed to box after score is added
            thing_width += (dodged * 1.2) #makes box wider as score is added
        
        if y < thing_starty+thing_height: #if topleft of box + height of box (lowest lineof box) passes car,
            #print('y crossover')

            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width: #essentially draws the boundaries for which the car can have the possibility of crashing, all 4 sides of box are defined and top two sides (upright, upleft) of car are defined.
                #print('x crossover')
                crash()
                
        pygame.display.update() #updates display, or use pygame.display.flip | with no parameters, updates all. flip updates all always, update has the possibility of single updates in ()
        clock.tick(60) #directly equals FPS, tied directly to x_change, y_change

game_intro()
game_loop()
pygame.quit() #quit with pygame
quit() #quit in IDE
