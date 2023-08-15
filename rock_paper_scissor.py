import random

user_choice=int(input("Enter your choice: Type 0 for Rock, 1 for paper , 2 for scissors\n "))
if user_choice > 3 or user_choice < 0:
    print("you Entered an invalid number, you lose ")
else: 
    computer_choice=random.randint(0,2)
    print("computer chose: ")
    print(computer_choice)
    if computer_choice == user_choice: 
        print("Match Drawn")
    if user_choice < computer_choice:
        if user_choice == 0 and computer_choice == 2:
            print("You win")
        else:
            print("You Lose") 
    if user_choice > computer_choice:
        if(user_choice == 2 and computer_choice == 0):
            print("You Lose")
        else:
            print("You Win")