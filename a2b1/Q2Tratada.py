<<<<<<< HEAD
import random

vet = []
try:
    for i in range(0, 4):
        vet.append(random.randrange(0, 200))

    n = int(input("Escolha uma posição (De 0 a 4) para ver qual número foi sorteado: "))
    print(vet[n])
except IndexError: 
    print("Por favor, escolha uma posição entre 0 e 4.")
    
=======
import random

vet = []
try:
    for i in range(0, 4):
        vet.append(random.randrange(0, 200))

    n = int(input("Escolha uma posição (De 0 a 4) para ver qual número foi sorteado: "))
    print(vet[n])
except IndexError: 
    print("Por favor, escolha uma posição entre 0 e 4.")
    
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
