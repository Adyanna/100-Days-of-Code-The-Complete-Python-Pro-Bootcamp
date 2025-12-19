import random
import day_seven_hangman_art
import day_seven_hangman_words

print(day_seven_hangman_art.logo)
#instanciamos la lista de las palabras para el juego
word_list=day_seven_hangman_words.words
#ecogemos una palabra aleatoriamente
word_game = random.choice(word_list)
#mostramos los lugares con la misma longitud que la palabra
placeholder=""
for i in range(len(word_game)):
    placeholder+="_"
print(placeholder)
game_over= False
correct_letters=[]
count=0
man = day_seven_hangman_art.HANGMANPICS
while not game_over and count<len(man):
    #solicitaoms la letra a adivinar
    guess = input("Guess a letter: \n").lower()
    #iteramos el mismo para verificar si la letra ingresada se encuentra en la palabra
    display=""
    for char in word_game:
        if guess == char:
            display +=char
            correct_letters.append(char)
        elif char in correct_letters:
            display +=char
        else:
            display += "_"
    print(display)
    
    if guess not in correct_letters:
        print(man[count])
        count += 1

    if "_" not in display:
        game_over=True
        print(day_seven_hangman_art.WINNER)
    
    if count==len(man):
        print(day_seven_hangman_art.loser)
    
    

