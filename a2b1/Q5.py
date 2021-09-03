<<<<<<< HEAD
n = int(input("Por favor entre com um numero: "))
vet = []
for cont in range(1, n+1):
    t = 0
    for i in range(1, cont+1):
        if cont%i == 0:
            t = t + 1
    if(t == 2):
        vet.append(i)
print(vet)
=======
n = int(input("Por favor entre com um numero: "))
vet = []
for cont in range(1, n+1):
    t = 0
    for i in range(1, cont+1):
        if cont%i == 0:
            t = t + 1
    if(t == 2):
        vet.append(i)
print(vet)
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
