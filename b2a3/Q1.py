qtd = 0

#NAO PERMITINDO OUTRA ENTRADA
while((qtd < 6 ) or qtd >= 800008):
    qtd = int(input("Por favor, informe a quantidade de Km: "))

aux = qtd+2

if qtd <= 6:
    print("1")
else:
    if aux%8 == 0:
        print("1")
    else:
        if qtd == 7:
            print("2")
        else:
            if aux%5 == 0:
                print("2")
            else:
                if qtd == 8:
                    print("3")
                else:
                    if qtd%8 == 0:
                        print("3")
                    else:
                        print("-")