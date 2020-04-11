from random import randint
import sys

## HI EVERYONE IS THE COMPLETE RANDOM GUESSING GAME I MADE
## BASED ON ANDERI NEAGOIE
# I MADE EXIT CHOICE TO EXIT THIS GAME FROM WHILE LOOP.
# play it with terminal window
# generate a number 1 ~ 10
lower = int(sys.argv[1])
upper = int(sys.argv[2])

while True:
    # input guess
    answer = randint(lower, upper)
    guess_answer = input(f'Lets play. Enter your number {lower} ~ {upper}: ')
    if guess_answer == 'exit':
        print('Bye bye')
        break
    guess_answer = int(guess_answer)
    try:
        # check that input is a number 1 ~ 10
        if lower < guess_answer < upper:
            if guess_answer == answer:
                print('omg. why are you so smart!!! :D')
                continue
            else:
                print('uhm. It is so close. do you want to try again')
                continue
        else:
            print(f'omg. Enter your number {lower}~ {upper}:')
            continue
    except ValueError:
        print('oops. try enter right number in this game :')
        continue
