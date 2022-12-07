#text-based game final 10 rooms, 2 functions, 5 items, and win or lose
import random
#import time
inventory =[" ", " ", " ", " ", " ", " "]
PlayerHealth = 100

def BossBattle(PlayerHealth): #This is my function for my battle system for path 1 and final boss
    RobotHealth = 50
    while PlayerHealth > 0 and RobotHealth > 0:
        if inventory[1]=="laser arm": #This is the item in my inventory that will increase my attack to fight robot
            damage = random.randrange(10,41)
        else:#withouth it I would do this amount of damage 
            damage = random.randrange(5,11)
        print("You hit the robot for", damage, "HP")
        RobotHealth -= damage
        damage = random.randrange(10, 41)
        print("The robot attacks back for", damage, "HP")
        PlayerHealth -= damage
        
        print("you have now", PlayerHealth, "HP left, the robot has", RobotHealth, "HP left ")
        choice = input("press h for hyper elixir or press b for butter finger, any other key to continue")
        if choice == "h":
            if inventory[2]=="hyper elixir":
                print("drinking noises, ahhh, (xp+40)")
                PlayerHealth +=40
                inventory[2]= " "
            else:
                print("sorry in canadian accent, you haven no potion")
        if choice == "b":
            if inventory[0]=="butter finger":
                print("you pull out a butter finger and throw it at Greg, they catch it and an alien apperas ripping it to shreds leaving nothing behind but a mangaled machine and leaves saying, no one puts a finger on my butter finger")
                RobotHealth = 0
            else:
                print("the robot does not catch the butter finger and smacks you to the wall")
                PlayerHealth = 0
        print()
    if PlayerHealth <=0:
        print("you died")
    else:
        print("you deafeated the robot")
        
    return PlayerHealth
#Rock Paper Scissors-----------------------------
import random
humanPoints = 0


def RockPaperScissors(humanPoints):
    print("Ready to play rock paper scissors?")
    print("Type rock paper or scissors now:")
    choice = input()
    num = random.randrange(1,4)
    #--------------------------------------------------
    if num == 1: print("i got rock")
    elif num == 2: print("I got paper")
    elif num == 3: print("i got scissors")
    else: print("no")
    #--------------------------------------------------
    if choice == "rock" and num ==1:
        print("it's a tie")
    if choice == "paper" and num ==2:
        print("it's a tie")
    if choice == "scissors" and num ==3:
        print("it's a tie")
    #--------------------------------------------------
    if num == 1 choice == "scissors":
        print("rock beats scissors, Greg wins a point")
        humanPoints-=1
    if num == 2 and choice == "rock":
        print("paper beats rock, Greg wins a point")
        humanPoints-=1
    if num == 3 and choice == "paper":
        print("scissors beats paper, Greg wins a point")
        humanPoints-=1
    #--------------------------------------------------
    if choice == "rock" and num == 3:
        print("rock beats scissors, you win a point!")
        humanPoint+=1
    if choice == "scissors" and num == 2:
        print("scissors beats paper, you win a point!")
        humanPoint+=1
    if choice == "paper" and num == 1:
        print("paper beats rock, you win a point!")
        humanPoint+=1
    return humanPoints
        
while True:
    humanPonts = RPS(humanPoints)
    print("Your humanpoints", humanPoints)
#inventory--------------------------------------
#import random
#inventory = ["laser arm", "hyper elixir", "hover boots", "fire exilir" , "butter finger"]
#PlayerHealth = 100

        
#DoExit = False
#room = 1
#while DoExit == False and PlayerHealth>0: #see if it works without and playerhealth
    #print("--------------------")
    #print("your health is", PlayerHealth)
    #print("your inventory:", end = " ")
    #for i in range (len(inventory)):
        #print(inventory[i], end = " ")
    #print()
    
    #if room == 1:
        #choice = input("hello human, my name is Greg, your friends thought it would be funny to put you in a robotic death chamber whileyou were asleep. The only way to get is through one of the two pathways. Once you get to the final room you need to defeat me. You can go south or east Good Luck!")
        #if inventory[0]!="laser arm": #if you only want them to get one
            #inventory[0]="laser arm"
            #print("you got a laser arm boo hoo")
        #if choice == 'south':
            #room = 2
    #if room == 2:
        #choice = input("you are in room 2 you can go north or west")
        #choice = input("theres a crate with a unique design in the middle")
        #if choice == 'open crate':
            #print("there's a hyper elixir *the sauce* inside")
            #inventory[1]="hyper elixir"
        #elif choice == 'north':
            #room = 1
        #elif choice == 'west':
            #room = 3
    #if room == 3:
        #print("you can go east")
        #choice = input()
        #if choice == "East":
            #if inventory[1]=="bomb":
                #print("you blew up the door to room 4")
                #room = 4
                #inventory[1] = " "
                
    #if room == 4:
        #print("A robot has emerged from the floor")
    
    #if PlayerHealth <= 0:
        #print("You lost")
    #else:
        #print("You survived")
           
    
#--------------------------------------------
def RoomRandimizer():
    chance = random.randrange(1,100)
    if chance < 50:
        num = random.randrange(12, 17)
        print("you're warped to room", num)
        return num
#---------------------------------------------
def FloorFall():
    num = random.randrange(0,100)
    if inventory[1]=="hover boots":
        if num < 50:
            print("you fell and died")#add player health so game ends when you die
            return 1
        elif num < 40:
            print("the floor is jammed and you proceed forward")
            return 2
        else:
            print("nothing happened")
            return 3
    else:
        if num < 70:
            print("you fell and died")
            return 1
        elif num < 10:
            print("the florr is jammed and you proceed forward")
            return 2
        else:
            print("nothing happened")
            return 3  
#----------------------------------------
#import time
#start = time.time()
#room = 1
#TimeLeft = 100

#while TimeLeft > 0:
    #print()
    #newTime = time.time()
    #timeElapsed = start -newTime
    #print(int(timeElapsed*-1), "seconds have passed.")
    #TimeLeft += timeElapsed
    #print("you have", int(TimeLeft), "seconds left to complete the game")
    
    #if room ==1:
        #choice = input("you are in room 1, you can go south")
        #if choice == "south":
            #room = 2
    #if room ==2:
        #choice = input("you are in room 2, you can go north")
        #if choice == "north":
            #room = 1
    
    

#-----------------------------------------------------------------------
DoExit = False
room = 1
while DoExit == False and PlayerHealth>0: #see if it works without and playerhealth
    print("--------------------")
    print("your health is", PlayerHealth)
    print("your inventory:", end = " ")
    for i in range (len(inventory)):
        print(inventory[i], end = " ")
    print()
  
    if room == 1:
        choice = input("hello human, my name is Greg, your friends thought it would be funny to put you in a robotic death chamber while you were asleep. The only way to get is through one of the two pathways. Once you get to the final room you need to defeat me. You can go south or east Good Luck!")
        print("there's a butter finger in your pocket, you decide to keep it, it may come in handy later on")
        inventory[0]!= "butter finger"
        inventory[0]="butter finger"
        if choice == 'south':
            room = 2
        elif choice == 'east':
            room = 12
    if room == 2:
        choice = input("You've chosen the first pathway, I guess this is a good time to mention that you will have to fight some deadly robots before you can reach me, you can go north or west")
        if choice == 'north':
            room = 1
        elif choice == 'west':
            room = 3
    if room == 3:
        print("you enter a dark and silent room, you can go east or south")
        print("a bright light appears from the ground a weapon has been granted to you")
        choice = input()
        if choice == 'grab weapon':
          print("you got a laser arm")
          inventory[1]="laser arm"
        if choice == 'east':
            room = 2
        elif choice == 'south':
            room = 4
    if room == 4:
        choice = input("you have entered a room where you notice the number of people who have been inside this death chamber, none have survived, you may proceed north or south")
        if choice == 'north':
            room = 3
        elif choice == 'south':
            room = 5          
    if room == 5:
        print("you have entered a room full of crates, go north or east")
        print("theres a crate with a unique design in the middle")
        choice = input()
        if choice == 'open crate':
            print("there's a hyper elixir *the sauce* inside")
            inventory[2]="hyper elixir"
        if choice == 'north':
            room = 4
        elif choice == 'east':
            room = 6    
          
    if room == 6:#Mini Boss 
      print("A robot has emerged from the floor")
      PlayerHealth =  BossBattle(PlayerHealth) 
      choice = input("you stand on top of the robot you have deafeated, the door opens, proceed west or east")
      if choice == 'west':
          room = 5
      elif choice == 'east':
          room = 7
      #break
    if room == 7:
        choice = input("Greg appears from the ceiling in shock, well you survived that well congrats it would definetly be a shame if another robot pops us, proceed west or east")
        if choice == 'west':
            room = 6
        elif choice == 'east':
            room = 8           
    if room == 8:
        choice = input("you enter a room similar to the one filled with all the last people who up to that point but in this room there is nothing, no one has made it this far, proceed west or north")
        if choice == 'west':
            room = 7
        elif choice == 'north':
            room = 9            
    if room == 9:#Mini Boss
        print("A robot has emerged from the floor")
        PlayerHealth =  BossBattle(PlayerHealth) 
        #break
        choice = input("Greg springs up filled with rage, NOO THAT CANT BE YOU SHOULD BE DEAD BY NOW, proceed south or east")
        if choice == 'south':
            room = 8
        elif choice == 'east':
            room = 10      
    if room == 10:
        choice = input("Greg sitll in the same spot as the other room, YOU WILL NOT SURVIVE AGAINST ME MARK MY WORDS HUMAN, proceed west or east")
        if choice == 'west':
            room = 9
        elif choice == 'east':
            room = 11    

          
    if room == 11:#Final Boss
      print("Greg with all his might appears in front of you ready to end you once and for all")
      PlayerHealth = BossBattle(PlayerHealth)
      break
        
            
    if room == 12:
        choice = input("You've chosen the second pathway, good choice this pathway is the least hardest if you're able to survive the death traps and random teleportation have fun, you may proceed west or east")
        if choice == 'west':
            room = 1
        elif choice == 'east':
            room = 13      
    if room == 13:
        print("you enter a dark and silent room, you can go west or north")
        print("the floor opens and smoke comes out, once cleared out you notice a pair of boots appear before you")
        choice = input()
        if choice == 'grab boots':
          print("you got hover boots")
          inventory[1]="hover boots"
        if choice == 'west':
            room = 12
        elif choice == 'north':
            room = 14            
    if room == 14:
      #print("a blue portal appears out of nowhere you are sucked into it")
      #RoomRandimizer()
      #choice = input()
        choice = input("you enter a room where you see all the people who have been inside this death chamber so far most have made it this far but their fate is still to be known, you may proceed south or east")
        if choice == 'south':
            room = 13
        elif choice == 'east':
            room = 15       
    if room == 15:
        choice = input("room 15 west or east")
        result = FloorFall() 
        if result == 1:
            doExist = True
            splat = True
        elif result == 2:
            doExist = True
        if choice == 'west':
            room = 14
        elif choice == 'east':
            room = 16            
    if room == 16:
        choice = input("room 16 west or south")
        result = FloorFall() 
        if result == 1:
            doExist = True
            splat = True
        elif result == 2:
            doExist = True
        if choice == 'west':
            room = 15
        elif choice == 'south':
            room = 17
    if room == 17:
        choice = input("Greg emergers in anger, HOW DID YOU SRVIVE THAT IT CANT BE, proceed north or south")
        if choice == 'north':
            room = 16
        elif choice == 'south':
            room = 18
    if room == 18: 
        choice = input("still outraged Greg screams, YOUR LUCK ENDS NOW HUMAN, proceed north or south")
        if choice == 'north':
            room = 17 
        elif choice == 'south':
            room = 11      
#-------------------------------------------------            
            
            
            
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
if PlayerHealth <= 0:
  print("You lost")
else:
  print("YOU WON, you have survived the death chamber")
