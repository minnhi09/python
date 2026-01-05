print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome To Treasue Island !")
print("Your mission is to find the treusue. ")

choice1 = input("you\'re at a crossroad. where you want to go ? Type \"Left\" or \"Right\"\n").lower()

if choice1 == "left":
    choice2 = input("you\'re come to a lake. There is an island in the middle lake.\n Type \"Waite\" to waite to a boat or \"Swim\" to swim across.\n").lower()

    if choice2 == "waite":
        choice3 == input("you arrive at the island unhamed. "
                         "there is a house with 3 doors. "
                         "one red, one yellow, one blue. " 
                         "which color do you choose?\n").lower()
        if choice3 == "red":
            print("ITS A ROOM FULL OF RIERRR !!!. GAME OVER :\">")
        elif choice3 == "yellow":
            print("BRAVO !!! YOU FOUND THE TREASUE! ")
        elif choice3 == "blue":
            print("you enter a room of beasts. GAME OVER!")
        else:
            print("you choose a door that doesn\'t exist. GAME OVER!")
        
    else:
        print("you got attacked by an angry trout :> GAME OVER!")
else:
    print("You fell into a hole ;)) GAME OVER!")

