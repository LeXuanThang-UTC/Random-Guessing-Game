from random import randint
import sys
## HI EVERYONE IS THE COMPLETE RANDOM GUESSING GAME I MADE
## BASED ON ANDERI NEAGOIE
# I MADE EXIT CHOICE TO EXIT THIT GAME FROM WHILE LOOP.
# play it with terminal window
# generate a number 1 ~ 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
# input guess
    guess_answer = input('Lets play. Enter your number 1 ~ 10: ')
    if guess_answer == 'exit':
        print('Bye bye')
        break
    guess_answer = int(guess_answer)
    try:
        # check that input is a number 1 ~ 10
        if 0 < guess_answer < 11:
            if guess_answer == answer:
                print('omg. why are you so smart!!! :D')
                continue
            else:
                print('uhm. It is so close. do you want to try again')
                continue
    except ValueError:
            print('opps. try enter right number in this game :')
            continue
