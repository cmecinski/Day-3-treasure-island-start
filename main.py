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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction_1 = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()
if direction_1 == "left":
  direction_2 = input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n''').lower()
  if direction_2 == "wait":
    direction_3 = input('''You find a triangular obelisk with three doors. Type "Red" to enter the red door. Type "Blue" to enter the blue door. Type "Yellow to enter the yellow door.\n"''').lower()
    if direction_3 == "yellow":
      print('''You have found the hidden treasure chest! Inside there are two gold doubloons! You win!''')
    elif direction_3 == "red":
      print('''You enter the red door and find a room full of fire. Game over.''')
    elif direction_3 == "blue":
      print('''You enter the blue door and get sucked into a void. Game over.''')
    else:
        print('''You took too long and run out of rations. Game over.''')  
  else:
    print('''Oops! You were eaten by a Mosasaur from the Early Cretaceous period. Game over.''')
else:
  print('''You fell into a ravine! Game over.''')
  

