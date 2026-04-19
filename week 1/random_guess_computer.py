import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c' :
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high lol
        feedback = input(f'Is {guess} too High (H), or too Low (L), or Correct (C)?? : ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yayyyy! the Computer guessed the number {guess} Correctly.')

computer_guess(100)
