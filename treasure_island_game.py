print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

first_step = input("Hello to you. Which side do you choose? Left or Right?\n").lower()

if first_step == "left":
  print("Good, you go to the next step!")
  
  second_step = input("For this step you have to 'swim' or you have to 'wait'.\nWhat is your choice?\n ").lower()
  
  if second_step == "wait":
    print("Good choice again! You go to the final step!")

    third_step = input("Your final question is?\nWhat is your favorite colour?\n").lower()

    if third_step == "red":
     print("X - Game over buddy, you are burned by fire! TRY AGAIN!")
    elif third_step == "yellow":
     print("Congratulations, you WIN the Treasure Island Game!")
     print('''*******************************************************************************
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
 /______/______/______/______/______/______/______/______/______/______/_______/
 ****************************************************************************''')
    else:
     print("X - Game over buddy, wrong answer! You were so close! TRY AGAIN!")
  else:
    print("X - Game over buddy, wrong answer! TRY AGAIN!")
else:
  print("X - Game over buddy, wrong answer! TRY AGAIN!")
