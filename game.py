import random

def number_guessing_game(player_name="Player"):
    print("=" * 50)
    print("    PLAYER vs COMPUTER NUMBER GUESSING GAME")
    print("=" * 50)
    print()
    
    # Computer picks a secret number
    computer_secret = random.randint(1, 100)
    print("Computer has picked a secret number between 1-100!")
    print()
    
    # Player enters their secret number
    print(f"{player_name}, enter your secret number (1-100)")
    print("(Computer won't see it!)")
    print()
    
    while True:
        try:
            player_secret = int(input(f"{player_name}, enter your secret number: "))
            if 1 <= player_secret <= 100:
                break
            else:
                print("Please enter a number between 1 and 100!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print("\n" * 3)
    print("=" * 50)
    print("        GAME STARTS - TAKE TURNS GUESSING")
    print("=" * 50)
    print()
    
    round_num = 1
    player_found = False
    computer_found = False
    computer_guesses = set()  # Track computer's guesses to avoid repeats
    
    # Game loop
    while not player_found and not computer_found:
        print(f"--- ROUND {round_num} ---\n")
        
        # Player's turn to guess
        print(f"{player_name}'s turn to guess Computer's number")
        while True:
            try:
                player_guess = int(input(f"{player_name}, what's your guess? "))
                if 1 <= player_guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100!")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        print(f"{player_name} says: {player_guess}")
        
        if player_guess == computer_secret:
            print(f"{player_name} FOUND IT! The number was {computer_secret}!")
            player_found = True
        elif player_guess < computer_secret:
            print(f"Computer responds: My number is HIGHER than {player_guess}.")
        else:
            print(f"Computer responds: My number is LOWER than {player_guess}.")
        
        print()
        
        if player_found:
            break
        
        # Computer's turn to guess
        print(f"Computer's turn to guess {player_name}'s number")
        
        # Computer makes a smart guess (avoiding repeated guesses)
        while True:
            computer_guess = random.randint(1, 100)
            if computer_guess not in computer_guesses:
                computer_guesses.add(computer_guess)
                break
        
        print(f"Computer says: {computer_guess}")
        
        if computer_guess == player_secret:
            print(f"Computer FOUND IT! The number was {player_secret}!")
            computer_found = True
        elif computer_guess < player_secret:
            print(f"{player_name} responds: My number is HIGHER than {computer_guess}.")
        else:
            print(f"{player_name} responds: My number is LOWER than {computer_guess}.")
        
        print()
        round_num += 1
    
    print("=" * 50)
    if player_found:
        print(f"{player_name} WINS!")
    else:
        print(f"Computer WINS!")
    print("=" * 50)


def main():
    print("Welcome to the Number Guessing Game!")
    print()
    
    # Get player name
    player_name = input("Enter your name (default: Player): ").strip() or "Player"
    
    while True:
        print("\n" * 2)
        number_guessing_game(player_name)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
