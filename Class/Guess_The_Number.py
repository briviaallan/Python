import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print('sorry, too low\n.')
        elif guess > random_number:
            print('sorry, guess again. too high.\n')
    print('yay, congrats. You have guessed {random_number}!')            

def Computer_Guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = (input(f'Was {guess} too high (h), low (l), or correct (c)'))
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low == guess + 1

    print(f"yay, I guessed your number. {guess}")    

Computer_Guess(10)
guess(100)