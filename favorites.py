import random
inventory =[" ", " ", " "]

def FloorFall():
    num = random.randrange(0,100)
    if inventory[0]=="lucky rock":
        if num < 5:
            print("")
            return 1
        elif num < 25:
            print("")
            return 2
        else:
            print("")
            return 3
    else:
        if num < 10:
            print("")
            return 1
        elif num < 20:
            print("")
            return 2
        else:
            print("")
            return 3  

room = 1
doExist = False
#-----------------------------------------------------------------------
while doExist == False:
    if room == 1:
        choice = input("you are in room 1 you can go south or east")
        if choice == 'south':
            room = 2
        elif choice == 'east':
            room = 12
    if room == 2:
        choice = input("")
        if choice == 'north':
            room = 1
        elif choice == 'west':
            room = 3
    if room == 3:
        choice = input("")
        if choice == 'east':
            room = 2
        elif choice == 'south':
            room = 4
     if room == 4:
        choice = input("")
        if choice == 'north':
            room = 3
        elif choice == 'south':
            room = 5          
    if room == 5:
        choice = input("")
        if choice == 'north':
            room = 4
        elif choice == 'east':
            room = 6            
    if room == 6:
        choice = input("")
        if choice == 'west':
            room = 5
        elif choice == 'east':
            room = 7
    if room == 7:
        choice = input("")
        if choice == 'west':
            room = 6
        elif choice == 'east':
            room = 8           
    if room == 8:
        choice = input("")
        if choice == 'west':
            room = 7
        elif choice == 'north':
            room = 9            
    if room == 9:
        choice = input("")
        if choice == 'south':
            room = 8
        elif choice == 'east':
            room = 10      
     if room == 10:
        choice = input("")
        if choice == 'west':
            room = 9
        elif choice == 'east':
            room = 11    
            
    if room == 11:#FINAL BOSS make text red and black
        choice = input("")
        if choice == '':
            room = 
        elif choice == '':
            room =
            
    if room == 12:
        choice = input("")
        if choice == 'west':
            room = 1
        elif choice == 'east':
            room = 13      
    if room == 13:
        choice = input("")
        if choice == 'west':
            room = 12
        elif choice == 'north':
            room = 14            
    if room == 14:
        choice = input("")
        if choice == 'south':
            room = 13
        elif choice == 'east':
            room = 15       
    if room == 15:
        choice = input("")
        if choice == 'west':
            room = 14
        elif choice == 'east':
            room = 16            
    if room == 16:
        choice = input("")
        if choice == 'west':
            room = 15
        elif choice == 'south':
            room = 17
    if room == 17:
        choice = input("")
        if choice == 'north':
            room = 16
        elif choice == 'south':
            room = 18
    if room == 18: 
        choice = input("")
        if choice == 'north':
            room = 17 
        elif choice == 'south':
            room = 11      
            
            
            
            
    if room == 2:
        choice = input("")
        choice = input("")
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
    if room == 4:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
#---------------------------------------------------------------------
if splat == True:
    print("you lost")
else:
    print("you're alive boo")

