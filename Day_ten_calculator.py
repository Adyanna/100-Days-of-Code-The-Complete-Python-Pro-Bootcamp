import day_nine_art

def add(n1: int|float,n2:int|float) ->int|float:
    result=n1+n2
    #return(f"{n1} + {n2} = {result}")
    return result

def multiply(n1: int|float,n2:int|float) ->int|float:
    result=n1*n2
    #return(f"{n1} * {n2} = {result}")
    return result

def rest(n1: int|float,n2:int|float) ->int|float:
    result = n1 - n2
    #return(f"{n1} - {n2} = {result}")
    return result


def divide(n1: int|float,n2:int|float) ->int|float:
    result = n1 / n2
    #return(f"{n1} / {n2} = {result}")
    return result

operation = {
    "+":add,
    "/":divide,
    "*":multiply,
    "-":rest         
}

def calculator():
    status=True
    result=0
    while status:
        if result==0:
            print(day_nine_art.logo_d10)
            n_one = float(input("What's the first number?:  "))
        print ("+\n- \n* \n? \n")
        operation_signal=input("Pick an operation:  ")
        n_two = float(input("What's the next number?"))
        
        result= operation[operation_signal](n_one,n_two)
        
        #todo esto me evito utilizando el diccionario
        #ya que tambien se puede amacenar funciones
        """
            if operation == "*":
            result = multiply(n_one,n_two)
        elif operation == "/":
            result = divide(n_one,n_two)
        elif operation == "+":
            result = add(n_one,n_two)
        elif operation == "-":
            result = rest(n_one,n_two)
        """

        print(f"{n_one} {operation_signal} {n_two} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ")
        if cont=='n':
            print("\n" *20)
            calculator()
        elif cont=='y':
            n_one=result
        else:
            status=False
        

calculator()




