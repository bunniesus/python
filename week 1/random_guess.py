#Guess the number (Computer)
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number betwwen 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Guess again. Too low..')
        elif guess > random_number:
            print('Sorry , Guess again. Too high..')
    print("Yayyyy! You guessed the correct number.")


guess(100)