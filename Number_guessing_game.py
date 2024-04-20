import random

#define the min and max range for the guess
upper_bound = 100
lower_bound = 1
max_attempts = 10

# generate the secret number
secret_number = random.randint(lower_bound, upper_bound);
#print(secret_number) #for debugging

# to collect the correct guess
def user_guess():
    while True:
        try:
            guess = int(input(f"enter a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print( "Invalid guess")
        except:
            print( "Invalid guess")
        
    
# check if the guess is correct 
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "CORRECT"
    elif guess < secret_number:
        return "Too low, Try again"
    else:
        return "Too high, Try again"
    
# Function to play the game
def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = user_guess()
        result = check_guess(guess, secret_number)
        
        if result == "CORRECT":
            print( f"YOU WIN! The secret number is {secret_number}")
            won = True
            break
        else:
            print(f" {result}")
        
    if won == False:
        return f"You lose, The secret number is {secret_number}"
        
play_game()    