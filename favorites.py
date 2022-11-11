import random
inventory =[" ", " ", " "]

def FloorFall():
    num = random.randrange(0,100)
    if inventory[0]=="lucky rock":
        if num < 5:
            print("you fell through the floor and died")
            return 1
        elif num < 25:
            print("you found a small whole that gets you out of the cave")
            return 2
        else:
            print("the floor creaks")
            return 3
    else:
        if num < 10:
            print("you fell through the floor and died")
            return 1
        elif num < 20:
            print("you found a small whole that gets you out of the cave")
            return 2
        else:
            print("the floor creaks")
            return 3  

room = 1
doExist = False
#-----------------------------------------------------------------------
while doExist == False:
    if room == 1:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 2:
        choice = input("you are in room 2, you can go (w)est or (s)outh")
        choice = input("you notice a mysterious rock on the wall")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 1
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 3
        elif choice == 'rock' or choice == 'grab rock':
            inventory[0]="lucky rock"
    if room == 3:
        choice = input("you are in room 3, you can go (n)orth or (s)outh")
        result = FloorFall() 
        if result == 1:
            doExist = True
            splat = True
        elif result == 2:
            doExist = True
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 4
#---------------------------------------------------------------------
if splat == True:
    print("you lost")
else:
    print("you're alive boo")
#animation------------------------------------------------------------
import pygame
pygame.init()
pygame.display.set_caption("sprite sheet")
screen = pygame.display.set_mode((800, 800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

Link = pygame.image.load('link.png')
Link.set_colorkey((255, 0, 255))

#player vari
xpos = 500
ypos = 200
vx = 0
keys = [False, False, False, False]

#animation variable
frameWidth = 64
frameHeight = 96
RowNum = 0
frameNum = 0
ticker = 0

while not gameover:
    clock.tick(60)
#INPUT SECTION-------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            keys[0]=True 
        elif event.key == pygame.K_RIGHT:
            keys[1]=True
        
    #left movement
    if keys[0]==True:
        vx=-10

    #righth movement
    elif keys[1] == True:
        vx = 10
    #turn off velocity
    else:
        vx = 0 #MO: this isn't stopping velocity, which is why your dude runs off the screen :)
        
        
#MO: stuff below this wasn't tabbed over, so it wasn't *in* your game loop
#in other words, your game loop ended here!
    xpos+=vx
#render------------------------------------------------------------------------------------------------------
    #left animation
    #MO: You don't have your if statements nested properly, check this against the slides :)
    if vx < 0:
        ticker+=1
    if ticker%10==0:
        frameNum+=1
    if frameNum>7:
        frameNum = 0
        

    screen.fill((0,0,0))
    #MO: you also speed screen wrong (you had "screeen")
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    pygame.display.flip()
#end game loop-----------------------------------------------------------------------------------------------
pygame.quit()
