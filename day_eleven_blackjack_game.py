#PROYECT BLACK JACK
from random import choice
from day_nine_art import logo_d11

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_cards():
    """
    Returns a random card form the deck
    """
    return choice(cards)

def deck_assing(total,cards):
    """
    Assing a number of cards of te deck
    """
    for _ in range(total):
        cards.append(deal_cards())

def calculate_score(cards):
    """
    Take a list of card and return a sum
    """
    resp = 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    if sum(cards)==21 and len(cards)==2:
        resp = 0
    else:
        resp = sum(cards)

    return resp

def game_over(human_score,computer_score):
    if human_score==0 or computer_score==0 or human_score>21:
        return True
def compare(human_score,computer_score):
    resp=""
    if human_score==computer_score:
        resp="Draw =P"
    elif computer_score==0:
        resp="Lose, opponent has Blackjack O.O"
    elif human_score==0:
        resp="Win with a BlackJack O.o"
    elif human_score>21:
        resp="You went over. You lose T.T"
    elif computer_score>21:
        resp="Opponet wnet over. You win! :D"
    elif human_score>computer_score:
        resp="You Win :)"
    else: resp = "You lose :V"
    return resp


def loop_game():
    computer_cards = []
    human_cards =[]
    is_game_Over = False
    print(logo_d11)
    deck_assing(2,human_cards)
    deck_assing(2,computer_cards)
    while not is_game_Over:
        print(f"Your cards: {human_cards}, current score: {calculate_score(human_cards)}")
        print(f"Computer's firts card: {computer_cards[0]} ")
       
        if game_over(calculate_score(human_cards),calculate_score(computer_cards)):
            is_game_Over=True
        else:
            another_card=input("Type 'y' to get another card, type 'n' to pass: \n")
            if another_card=='y':
                deck_assing(1,human_cards)
            else:
                is_game_Over=True
    c_score = calculate_score(computer_cards)
    while c_score!=0 and c_score<17:
        deck_assing(1,computer_cards)
        c_score=calculate_score(computer_cards)
        #print(computer_cards)

    result = compare(calculate_score(human_cards),calculate_score(computer_cards))
    print(result)



loop_game()
    









