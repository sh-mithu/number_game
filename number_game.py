import random
green="\033[92m"
reset="\033[0m"
red="\033[91m"
def guess_the_number():
    print(green,"\n\t\tAssalamualaikum, Welcome to the Guess the Number game!",reset)
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("\nChoice the number: "))
            attempts += 1

            if user_guess < secret_number:
                print(red,"Too low! Try again.😔",reset)
            elif user_guess > secret_number:
                print(red,"Too high! Try again.😔",reset)
            else:
                print(green,"Congratulations 😊! You've guessed the number",red,secret_number,green,"in",red,attempts,green,"attempts.",reset)
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
