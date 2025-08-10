import random

computer_points = 0
user_points = 0

while user_points < 2 and computer_points < 2:
    options = ["Rock","Paper","Scissors"]
    print("Let's play Rock, Paper, Scissors.")

    x = random.choice(options)
    user_option = None

    while user_option not in options:
        user_option = input("Pick your option (Rock, Paper, Scissors): ")


    if user_option == x:
        print(f"The computer chose {x}. It is a draw.")
    elif user_option == "Rock":
        if x == "Paper":
            print(f"The computer chose {x}. You lose.")
            computer_points += 1
        elif x == "Scissors":
            print(f"The computer chose {x}. You win.")
            user_points += 1
    elif user_option == "Paper":
        if x == "Scissors":
            print(f"The computer chose {x}. You lose.")
            computer_points += 1
        elif x == "Rock":
            print(f"The computer chose {x}. You win.")
            user_points += 1
    elif user_option == "Scissors":
        if x == "Rock":
            print(f"The computer chose {x}. You lose.")
            computer_points += 1
        elif x == "Paper":
            print(f"The computer chose {x}. You win.")
            user_points += 1

    print(f"You have {user_points}")
    print(f"The computer has {computer_points}")