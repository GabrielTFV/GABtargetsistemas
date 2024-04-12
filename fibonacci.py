usrInput = input()
listFibo = [0, 1]

def fibo(usrInput):
    x = 0
    y = 1
    aux = 0
    if usrInput in listFibo:
        return print(f"O número {usrInput} pertence a Fibonacci")
        
    while y <= usrInput:
        aux = y
        y = y + x
        x = aux
        listFibo.append(y)

    if usrInput in listFibo:
        print(f"O número {usrInput} pertence a Fibonacci")
    else:
        print(f"O número {usrInput} NÃO pertence a Fibonacci")

fibo(int(usrInput))
        
