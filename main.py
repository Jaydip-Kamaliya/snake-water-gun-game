import random

print(("=" * 36) + (" " * 3) + "Welcome to the Snake, Water, Gun Game" + (" " * 3) + ("=" * 36))
print("Notes: \n- Type 'quit' to quit the game. \n- The final score will be shown after quitting the game.")

guess = {
    1 : "snake",
    2 : "water",
    3 : "gun"
}

valid_guess = ["snake", "water", "gun"]

# Initialize scores and counters
compute_score = 0    # Score of the computer
user_score = 0       # Score of the user
totle_round = 0      # Total number of rounds played
draw = 0             # Number of draws

# Main game loop
while True:

    # Computer makes a random guess
    computer_int = random.randint(1, 3)
    computer_guess = guess[computer_int]

    user_guess = input("\nEnter your guess: ").strip().lower()

    # Check if the user wants to quit the game
    if user_guess == "quit":
        print(f"\nMy score = {compute_score} \nYour score = {user_score} \nDraw = {draw} \nTotal Rounds = {totle_round} \n")
        
        if compute_score > user_score:
            print("I think, I won")
        elif compute_score == 0 and user_score == 0:
            print("Play the game to get our final score")
        elif compute_score == user_score:
            print("We both did the same score...")
        else:
            print("congrates!! You won")
        break 
    
    # Check if the user input is valid
    elif user_guess not in valid_guess:
        print("Plese Enter valid guess")
        continue

    # Check who wins
    elif computer_guess == "snake" and user_guess == "water":
        print("I win")
        compute_score += 1
    elif computer_guess == "water" and user_guess == "gun":
        print("I win")
        compute_score += 1
    elif computer_guess == "gun" and user_guess == "snake":
        print("I win")
        compute_score += 1
    elif computer_guess == user_guess:
        print("It's Draw")
        draw += 1
    else:
        print("You win")
        user_score += 1
    totle_round += 1

    print(f"I guessed - {computer_guess}")