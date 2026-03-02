from day_fourteen_art import logo,vs
from day_fourteen_game_data import celebrities
from random import randint

#Display art

#Generate a random account from the game data
def select_celebrities(cel_data):
    num = randint(0, len(cel_data))
    return cel_data[num]

#Format the account dara into printable format
def celebrity(num,cel_data):
    return [f"compare {num}: {cel_data["name"]}, a {cel_data["description"]}, from {cel_data["country"]}.",cel_data["follower_count"]]

#ask user for a guess
def user_guess():
    resp = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    return resp
#check is user is correct
def check_followers(u_resp,celebrity_a,celebrity_b):
    #cel_a = data[celebrity_a]
    #cel_b = data[celebrity_b]
    if u_resp=='A' and celebrity_a>celebrity_b:
        return True
    elif u_resp =='B' and celebrity_b>celebrity_a:
        return True
    else:
        return False
        


def game_loop ():
    print(logo)
    cel_a = select_celebrities(celebrities)
    score = 0
    #make the game reapeatable
    while True:
        data_cel_a = celebrity('A',cel_a)
        print(data_cel_a[0])
        #print("pista: ",data_cel_a[1])
        print(vs)
        cel_b = select_celebrities(celebrities)
        data_cel_b=celebrity('B',cel_b)
        print(data_cel_b[0])
        #print("pista: ",data_cel_b[1])
        resp_u = user_guess()
        if(check_followers(resp_u,data_cel_a[1],data_cel_b[1])):
            # Making account at position b become the next account at position a
            cel_a=cel_b
            #score keeping
            score +=1
            #give user feedback on theirguess
            print('\n'*20)
            print(logo)
            print(f"You're rigth! Current score: {score}")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    

   

game_loop()




