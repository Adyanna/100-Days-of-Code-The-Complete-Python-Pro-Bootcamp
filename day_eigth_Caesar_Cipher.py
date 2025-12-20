# cifrado de palabra con el metodo Cesar
import string
alphabet=list(string.ascii_lowercase)
logo = '''
:'######:::::'###::::'########::'######:::::'###::::'########::
'##... ##:::'## ##::: ##.....::'##... ##:::'## ##::: ##.... ##:
 ##:::..:::'##:. ##:: ##::::::: ##:::..:::'##:. ##:: ##:::: ##:
 ##:::::::'##:::. ##: ######:::. ######::'##:::. ##: ########::
 ##::::::: #########: ##...:::::..... ##: #########: ##.. ##:::
 ##::: ##: ##.... ##: ##:::::::'##::: ##: ##.... ##: ##::. ##::
. ######:: ##:::: ##: ########:. ######:: ##:::: ##: ##:::. ##:
:......:::..:::::..::........:::......:::..:::::..::..:::::..::
:'######::'####:'########::'##::::'##:'########:'########::    
'##... ##:. ##:: ##.... ##: ##:::: ##: ##.....:: ##.... ##:    
 ##:::..::: ##:: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:    
 ##:::::::: ##:: ########:: #########: ######::: ########::    
 ##:::::::: ##:: ##.....::: ##.... ##: ##...:::: ##.. ##:::    
 ##::: ##:: ##:: ##:::::::: ##:::: ##: ##::::::: ##::. ##::    
. ######::'####: ##:::::::: ##:::: ##: ########: ##:::. ##:    
:......:::....::..:::::::::..:::::..::........::..:::::..::   
'''
print(logo)
#creamos la funcion para encryptar y desencriptar
def pro_selected(sentence,num,dir):
    new_cipher = ""
    if dir == 'decode':
        num *= -1
    for i in sentence:
        if i not in alphabet:
            new_cipher += i
        else: 
            loc = alphabet.index(i)+num
            print(loc,num)
            loc %= len(alphabet)
            new_cipher += alphabet[loc]

    print(f"Here is the {dir}d result: {new_cipher}")

resp = True
while resp:
    direccion = input("Type 'Encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your massage:\n").lower()
    shift = int(input("Type your shift number: \n"))
    pro_selected(text,shift,direccion)
    resp2 = input(print("Would you like continue?\n"))
    if resp2=="No":
        resp=False


