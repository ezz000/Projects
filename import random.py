import random

# Import the random module for generating random numbers.

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    # Display a welcome message to the user.

def get_valid_range():
    while True:
        try:
            lower_limit = int(input("Enter the lower limit of the range: "))
            upper_limit = int(input("Enter the upper limit of the range: "))
            
            if lower_limit >= upper_limit:
                print("Invalid range. The lower limit should be less than the upper limit.")
                continue

            return lower_limit, upper_limit
            # Get and return a valid range from the user.
        except ValueError:
            print("Invalid input. Please enter valid integers for the range.")
            # Handle exceptions if the user enters non-integer values.

def generate_secret_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)
    # Generate a random secret number within the specified range.

def display_range(lower_limit, upper_limit):
    print(f"I have selected a random number between {lower_limit} and {upper_limit}.")
    # Inform the user about the selected range and that a secret number has been chosen.

def make_guess(secret_number):
    attempts = 0

    while True:
        try:
            user_guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        attempts += 1

        if user_guess < secret_number:
            print("The secret number is higher. Try again.")
        elif user_guess > secret_number:
            print("The secret number is lower. Try again.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
            break
            # Compare the user's guess to the secret number and provide feedback.

if __name__ == "__main__":
    display_welcome_message()
    lower_limit, upper_limit = get_valid_range()
    secret_number = generate_secret_number(lower_limit, upper_limit)
    display_range(lower_limit, upper_limit)
    make_guess(secret_number)
