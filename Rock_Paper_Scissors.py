import random

choice = "None"
input_valid = False
player = "Player wins, congratulations!"
computer = "Computer wins, nice try!"
winner1 = False
winner2 = False

def write_to_terminal(choice):
    Rock = False
    Paper = False
    Scissors = False
    Rock = True if choice == "Rock" else False
    Paper = True if choice == "Paper" else False
    Scissors = True if choice == "Scissors" else False

    if Rock:
        print("Rock")
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

    # Paper
    if Paper:
        print("Paper")
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

    # Scissors
    if Scissors:
        print("Scissors")
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
        
def check_input(choice):
    global input_valid
    input_valid = True if choice == "Rock" or choice == "Paper" or choice == "Scissors" else False

def determine_winner(choice, random_selection):
    global winner1, winner2
    if choice == "Paper" and random_selection == "Rock":
        winner1 = True 
    elif choice == "Rock"  and random_selection == "Scissors":
        winner1 = True 
    elif choice == "Scissors" and random_selection == "Paper":
        winner1 = True 
    if choice == "Rock" and random_selection == "Paper":
        winner1 = True 
    elif choice == "Scissors"  and random_selection == "Rock":
        winner2 = True 
    elif choice == "Paper" and random_selection == "Scissors":
        winner1 = True 

print("Welcome to Rock, Paper, Scissors!")

choice = input("To play the game write your selection(Rock, Paper or Scissors):\n")

check_input(choice)

if input_valid:
    print("Your selection:")
    write_to_terminal(choice)

    options = ["Rock", "Paper", "Scissors"]
    random_selection = random.choice(options)
    print("Computer's choice:")
    write_to_terminal(random_selection)

    determine_winner(choice, random_selection)
    if winner1:
        print(player)
    elif winner2:
        print(computer)
    else:
        print("It's a draw! Better luck next time!")
else:
    print("Wrong input! Check for misspels and try again!")