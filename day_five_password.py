#generamos un password aleatorio
import string
import random

letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
nrL = int(input("How many letters would you like in you password? \n"))
nrN = int(input("How many nunmbers would you like? \n"))
nrS = int(input("How many symbols would you like? \n"))

#my version
cL= 0
cN = 0
cS = 0
password = ""
count = 0
while count < nrL+nrN+nrS:
    #print(cL,cN,cS)
    nselc = random.randint(0,2)
    if nselc == 0 and cL < nrL:
        password += letters[random.randint(0,len(letters)-1)]
        cL +=1
        count += 1
    elif nselc == 1 and nrN >cN:
        password += numbers[random.randint(0,len(numbers)-1)] 
        #random.choice(numbers)
        cN +=1
        count += 1
    elif nselc == 2 and nrS > cS:
        password += symbols[random.randint(0,len(symbols)-1)] 
        #random.choice(symbols)
        cS += 1
        count += 1

print(f"Your password is: {password}")

passwordv2=list()
#version de la clase
for n in range (0,nrL):
    passwordv2.append(random.choice(letters))

for n in range (0,nrN):
     passwordv2.append(random.choice(numbers))

for n in range (0,nrS):
     passwordv2.append(random.choice(symbols))

random.shuffle(passwordv2)

passv2=""
for char in passwordv2:
    passv2 += char

print(f"Your password is: {passv2}")