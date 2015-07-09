import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)



#refrence and redefine exact pixels

#pixel array
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green #paints 1 green pixel in the x coordinate of 10 and the y coordinate of 20

#!DRAW ORDER APPLIES!
pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5) #start point, end point as tuples, then thickness of line drawn

pygame.draw.rect(gameDisplay, red, (400,400,50,25)) #specify position from topleft (x,y) then width and height

pygame.draw.circle(gameDisplay, white, (150,150), 75) #specify center, then the radius, also can specify edge width

pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540))) #tuples within tuple defines each mark of polygon, first tuple is first point, etc. X THEN Y


while True: #'Game Loop'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
