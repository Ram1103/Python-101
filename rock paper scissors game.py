
import random


print("Winning Rules of the Rock paper scissor game as follows: \n"
	+ "Rock vs paper->paper wins \n"
	+ "Rock vs scissor->Rock wins \n"
	+ "paper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")

	choice = int(input("User turn: "))
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
 
  
    print("user choice is: " + choice_name)
    print("\n Now its computer turn")    