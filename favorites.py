import random
inventory = ["laser arm", "potion", "butter finger"]
Player Health = 100

def BossBattle(PlayerHealth):
    RobotHealth = 100
    while PlayerHealth > 0 and RobotHealth > 0:
        if inventory[0]=="laser arm":
            damage = random.randrange(10,41)
        else:
            damage = random.randrange(5,11)
        print("You hit the robot for", damage, "HP")
        RobotHealth -= damage
        damage = random.randrange(10, 21)
        print("The robot attacks back for", damage, "HP")
        PlayerHealth -= damage
        
        print("you have now", PlayerHealth, "HP left, the robot has", RobotHealth, "HP left ")
        choice = input("press p for potion, any other key to continue")
        if choice == "p":
            if inventory[1]=="potion":
                print("drinking noises, ahhh, (xp+20)")
                PlayerHealth +=20
                inventory[1]= "epmty"
            else:
                print("sorry in canadian accent, you haven no potion")
        if choice == "f":
            if inventory[2]=="butter finger":
                print("you pull out a butter finger and throw it at the robot, they catch it and an alien apperas ripping it to shreds and leaves saying, no one puts a finger on my butter finger")
                RobotHealth = 0
            else:
                print("the robot")
                PlayerHealth = 0
        print()
    if PlayerHealth <=0:
        print("you died")
    else:
        print("you deafeated the robot")
        
    return PlayerHealth
        
DoExit = False
room = 1
while DoExit == False:

    if room == 1:
        choice = input("hello human, my name is Greg, your friends thought it would be funny to put you in a robotic death chamber whileyou were asleep. The only way to get is through one of the two pathways. Once you get to the final room you need to defeat me. You can go south or east Good Luck!")
        if choice == 'south':
            room = 2
    if room == 2:
        choice = input("you are in room 2 you can go north or west")
        if choice == 'north':
            room = 1
        elif choice == 'west':
            room = 3
    if room == 3:
        print("A robot has emerged from the floor")
        PlayerHealth =  BossBattle(PlayerHealth) 
        break
    
    if PlayerHealth <= 0:
        print("You lost")
    else:
        print("You survived")

def RoomRandimizer():
    chance = random.randrange(1,100)
    if chance < 10:
        num = random.randrange(1, 9)
        print("you're warped to room", num)
        return num

def FloorFall():
    num = random.randrange(0,100)
    if inventory[0]=="":
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
def RockPaperScissors():
    
    
room = 1
doExist = False
#-----------------------------------------------------------------------
while doExist == False:
    if room == 1:
        choice = input("hello human, my name is Greg, your friends thought it would be funny to put you in a robotic death chamber whileyou were asleep. The only way to get is through one of the two pathways. Once you get to the final room you need to defeat me. You can go south or east Good Luck!")
        if choice == 'south':
            room = 2
        elif choice == 'east':
            room = 12
    if room == 2:
        choice = input("You've chosen the first pathway, you can go north or west")
        if choice == 'north':
            room = 1
        elif choice == 'west':
            room = 3
    if room == 3:
        choice = input("room 3 east or south")
        if choice == 'east':
            room = 2
        elif choice == 'south':
            room = 4
    if room == 4:
        choice = input("room 4 north or south")
        if choice == 'north':
            room = 3
        elif choice == 'south':
            room = 5          
    if room == 5:
        choice = input("room 5 north or east")
        if choice == 'north':
            room = 4
        elif choice == 'east':
            room = 6            
    if room == 6:
        choice = input("room 6 west or east")
        if choice == 'west':
            room = 5
        elif choice == 'east':
            room = 7
    if room == 7:
        choice = input("room 7 west or east")
        if choice == 'west':
            room = 6
        elif choice == 'east':
            room = 8           
    if room == 8:
        choice = input("room 8 west or north")
        if choice == 'west':
            room = 7
        elif choice == 'north':
            room = 9            
    if room == 9:
        choice = input("room 9 south or east")
        if choice == 'south':
            room = 8
        elif choice == 'east':
            room = 10      
    if room == 10:
        choice = input("room 10 west or east")
        if choice == 'west':
            room = 9
        elif choice == 'east':
            room = 11    
            
    if room == 11:#FINAL BOSS make text red and black
        choice = input("room 11 west or north")
        if choice == 'west':
            room = 10
        elif choice == 'north':
            room = 18
            
    if room == 12:
        choice = input("You've chosen the second pathway  west or east")
        if choice == 'west':
            room = 1
        elif choice == 'east':
            room = 13      
    if room == 13:
        choice = input("room 13 west or north")
        if choice == 'west':
            room = 12
        elif choice == 'north':
            room = 14            
    if room == 14:
        choice = input("room 14 south or east")
        if choice == 'south':
            room = 13
        elif choice == 'east':
            room = 15       
    if room == 15:
        choice = input("room 15 west or east")
        if choice == 'west':
            room = 14
        elif choice == 'east':
            room = 16            
    if room == 16:
        choice = input("room 16 west or south")
        if choice == 'west':
            room = 15
        elif choice == 'south':
            room = 17
    if room == 17:
        choice = input("room 17 north or south")
        if choice == 'north':
            room = 16
        elif choice == 'south':
            room = 18
    if room == 18: 
        choice = input("room 18 north or south")
        if choice == 'north':
            room = 17 
        elif choice == 'south':
            room = 11      
            
            
            
            
    #if room == 2:
     #   choice = input("")
      #  choice = input("")
       # if choice == 'w' or choice == 'W' or choice == 'west':
            #room = 1
        #elif choice == 's' or choice == 'S' or choice == 'south':
            #room = 3
        #elif choice == 'rock' or choice == 'grab rock':
           # inventory[0]="lucky rock"
    #if room == 3:
        #choice = input("you are in room 3, you can go (n)orth or (s)outh")
        #result = FloorFall() 
        #if result == 1:
            #doExist = True
            #splat = True
        #elif result == 2:
            #doExist = True
        #if choice == 'n' or choice == 'N' or choice == 'north':
        #    room = 2
        #elif choice == 's' or choice == 'S' or choice == 'south':
         #   room = 4
    #if room == 4:
        #choice = input("you are in room 1, you can go (e)ast")
        #if choice == 'e' or choice == 'E' or choice == 'east':
         #   room = 2
#---------------------------------------------------------------------
if splat == True:
    print("you lost")
else:
    print("you're alive boo")

