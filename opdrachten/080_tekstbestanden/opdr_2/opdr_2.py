# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random


def rand_int():
    random_int = random.randint(1, 100)
    return random_int


def guessing(random_int, tries):
    print(f"ATTEMPT {tries}:")
    guess = input("Guess the number between 1 and 100: ")

    if guess.lower() == "stop":
        print("Stopping the game.")
        return 0, 0

    if guess.lower() == "show":
        print(f"The target number is {random_int}")
        return True, 0

    try:
        int(guess)
    except ValueError:
        print("That is not a number I recognise. Try again!")
        return True, 1

    if int(guess) == random_int:
        print("You guessed right!")
        if tries > 1:
            print(f"It took you {tries} tries.")
        else:
            print(f"It took you {tries} try.")
        return 0, 0

    elif int(guess) < random_int:
        print("The number you guessed is lower than the target number. Try again!")
        return True, 1

    elif int(guess) > random_int:
        print("The number you guessed is higher than the target number. Try again!")
        return True, 1

    elif int(guess) > 100:
        print("The number you guessed is higher than 100. Try again!")
        return True, 1

    elif int(guess) < 1:
        print("The number you guessed is lower than 1. Try again!")
        return True, 1


def main():
    check = True
    trying = 1
    random_int = rand_int()

    while check:
        results = guessing(random_int, trying)
        trying += results[1]
        check = results[0]
    exit()


if __name__ == '__main__':
    # executes the main() function when the quiz.py file is executed.
    main()
