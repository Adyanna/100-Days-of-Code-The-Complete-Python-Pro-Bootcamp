from day_nine_art import logo_d12
from random import randint

EASY_LEVEL=10
HARD_LEVEL=5

def selecct_number():
    """
    Pick a number between 1 and 100.
    """
    print("I'm thinking aof a number between 1 and 100")
    return randint(1,100)

def dificulty_game():
    """
        Assign a number of opportunities depending on the user’s selection:
        Hard: 5 opportunities
        Easy: 10 opportunities
    """
    choose = input("Choose a difficulty. Type 'easy' or 'hard' \n").lower()
    num = EASY_LEVEL if choose=='hard' else HARD_LEVEL
    return num

def guess_number(number):
    unum = int(input("Make a guess: "))
    resp = False
    if number ==unum:
        resp = True
    else:
        give_hint(unum,number)
    return resp

def give_hint(unum,number):
    resp = "Too low"
    if unum>number:
        resp = 'Too High'
    print(resp)

def loop_game():
    print(logo_d12)
    print("Welcolme to the Number Guessing Game!")
    number = selecct_number()
    dificulty = dificulty_game()
    count=0
    while dificulty>0:
        print(f"You have {dificulty} attempts remaining to guess the number")
        if guess_number(number):
            print("You guess the number! you won!")
            break
        else:
            print("Guess again")
            dificulty -=1



loop_game()