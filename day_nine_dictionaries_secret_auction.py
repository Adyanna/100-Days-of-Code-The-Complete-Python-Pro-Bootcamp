# puja de

import day_nine_art

print(day_nine_art.logo)

def find_higtest_bidding(bids_d):
    inicio = 0
    nombre = ""
    for name in bids_d:
        if bids_d[name]>inicio:
            inicio = bids_d[name]
            nombre = name
    print(f"The winner ir {nombre} with a bid of ${inicio}")

bidders = {}
continue_p = True 
while continue_p=="yes":
    name = input("What's your name?:   ")
    bid = int(input("What's your bid?:   $"))
    bidders[name]=bid
    resp = input("Are there any other bidders? Type 'yes' or 'no':   ").lower()
    if continue_p=='no':
        continue_p= False
        find_higtest_bidding(bidders)
    else:
        print("\n" *20)




