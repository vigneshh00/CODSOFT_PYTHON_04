import random as rand

moves = ["rock","paper","scissors"]
round = 1
user_score = 0
computer_score = 0
next_round = True

print("======Rock-Paper-Scissors Game======")

while next_round:
    print(f"\nRound {round}\n")
    print("Select one of the following moves: \n"
          "1.Rock\n"
          "2.Paper\n"
          "3.Scissors\n")
    x = True
    while x:  
        choice = int(input("Enter your choice (corresponding number of your move): "))
        if choice>=1 and choice<=3:
            x = False

    computer_move = rand.choice(moves)
    user_move = moves[choice-1]

    print(f"Your move : {user_move}\nComputer's move : {computer_move}\n")

    if computer_move == user_move:
        print("It's a tie! (No score)\n")
    elif ( (user_move == "rock" and computer_move == "scissors") or
           (user_move == "scissors" and computer_move == "paper") or
           (user_move == "paper" and computer_move == "rock") ):
        print("You win!\n")
        user_score+=1
    else:
        print("You lose!\n")
        computer_score+=1

    print(f"Score after Round {round}\n"
          f"Your score : {user_score}\n"
          f"Computer score : {computer_score}\n")
    round+=1

    next_round = input("Do you want to play another round?\n"
                       "Type 'y' for 'Yes' or any character for 'No'\n"
                       "Your choice(y/n): ").lower() == 'y'

print("Thanks for playing!")
