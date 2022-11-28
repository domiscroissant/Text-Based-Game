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
    if room == 4:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 5:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 6:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 7:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 8:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 9:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 10:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 11:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 12:
        choice = input("you are in room 1, you can go (e)ast")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
#---------------------------------------------------------------------
if splat == True:
    print("you lost")
else:
    print("you're alive boo")

