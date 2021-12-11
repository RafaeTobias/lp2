<<<<<<< HEAD
try:
    n = int(input("Por favor, entre com um valor inteiro para calcular o fatorial do mesmo: "))
    fat = 0
    for i in range(n, 1, -1):
        if i == n:
            fat = n*(n-1)
        else:
            fat = fat*(i-1)
    print("Fatorial de", n, "=", fat)
except ValueError:
    print("Por favor, entre com um valor inteiro.")
=======
try:
    n = int(input("Por favor, entre com um valor inteiro para calcular o fatorial do mesmo: "))
    fat = 0
    for i in range(n, 1, -1):
        if i == n:
            fat = n*(n-1)
        else:
            fat = fat*(i-1)
    print("Fatorial de", n, "=", fat)
except ValueError:
    print("Por favor, entre com um valor inteiro.")
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
