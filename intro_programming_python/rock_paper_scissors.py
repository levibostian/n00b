from random import randint

user_move = input("What is your move? Rock, paper, or scissors? ")

print("You chose " + user_move)

computer_move = randint(0,3)

print("Computer's move is: " + str(computer_move))

if (computer_move == 0):
    computer_move = "rock"
elif (computer_move == 1):
    computer_move = "paper"
else:
    computer_move = "scissors"

print("Computer's move NOW is: " + computer_move)

if (computer_move == user_move):
    print("You both tied! You both picked: " + computer_move)
elif (computer_move == "rock" and user_move == "paper"):
    print("Paper covers rock, user wins!")
elif (computer_move == "rock" and user_move == "scissors"):
    print("Rock crushes scissors, computer wins!")
elif (computer_move == "paper" and user_move == "rock"):
    print("Paper covers rock, computer wins!")
elif (computer_move == "paper" and user_move == "scissors"):
    print("Scissors cuts paper, user wins!")
elif (computer_move == "scissors" and user_move == "rock"):
    print("Rock crushes scissors, user wins!")
elif (computer_move == "scissors" and user_move == "paper"):
    print("Scissors cuts paper, computer wins!")



    







    





    




    




