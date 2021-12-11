<<<<<<< HEAD
def somaNum(a,b):
    return a+b
try: 
    a = int(input("entre com um valor inteiro para a: "))
    b = int(input("entre com um valor inteiro para b: "))
    if somaNum(a, b) > 1000:
        raise OverflowError("A soma ultrapassou o intervalo obrigatório.")
    else:
        print("Soma =", somaNum(a, b))
except ValueError: 
    print("Por favor, entre com um número inteiro.")
=======
def somaNum(a,b):
    return a+b
try: 
    a = int(input("entre com um valor inteiro para a: "))
    b = int(input("entre com um valor inteiro para b: "))
    if somaNum(a, b) > 1000:
        raise OverflowError("A soma ultrapassou o intervalo obrigatório.")
    else:
        print("Soma =", somaNum(a, b))
except ValueError: 
    print("Por favor, entre com um número inteiro.")
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
