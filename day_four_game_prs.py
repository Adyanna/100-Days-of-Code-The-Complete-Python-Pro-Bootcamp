#GAME OF ROCK, PAPER, AND scissors.
import random
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
imagens=[rock, paper,scissor]
u_choose = int(input("what do you choose? type 0 for rock, 1 for Paper or 2 for Scissors \n"))

if u_choose>=0 and u_choose<3:
    print(imagens[u_choose])

c_choose = random.randrange(0,2)
print("compute chose: \n")
print(imagens[c_choose])


if (u_choose==0 and c_choose==2) or u_choose>c_choose:
    print("You Win!")
elif u_choose==c_choose:
    print("Is's a draw!")
elif u_choose>2 or u_choose<0:
    print("Your typed it's an invalid number! You lose!")
else:
    print("You lose!")
