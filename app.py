import random
wins = 0
#pc choice
while True :
    List = ["rock", "paper", "scissors"]

    pc_choice = random.choice(List)
    #print(pc_choice)

    #user choice
    my_choice = input("rock, paper, scissors? ").lower()


    #game logic

    def game():

        global wins 
        if pc_choice == my_choice:
            print("It's a tie!")
        elif pc_choice == "rock" and my_choice == "scissors":
            print("You lose!")
        elif pc_choice == "paper" and my_choice == "rock":
            print("You lose!")
        elif pc_choice == "scissors" and my_choice == "paper":
            print("You lose!")
        elif pc_choice == "rock" and my_choice == "paper":
            print("You win!")
            wins += 1
        elif pc_choice == "paper" and my_choice == "scissors":
            print("You win!")
            wins += 1
        elif pc_choice == "scissors" and my_choice == "rock":
            print("You win!")
            wins += 1


    if my_choice != "rock" and my_choice != "paper" and my_choice != "scissors":
        print("Please choose a valid option")
    else:
        game()

    if input("Do you want to play again? (y/n) ").lower() == "y":
        my_choice = ""
        game()
    else:
        print("You won " + str(wins) + " times.")
        print("Thanks for playing!")
        break
