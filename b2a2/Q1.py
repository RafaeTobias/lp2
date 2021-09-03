<<<<<<< HEAD
try:
    #ABRINDO ARQUIVO
    file = open("pontos.csv", "r")
    file.seek(0,0)

    #VARIAVEIS
    mod = []
    aux = file.readlines()
    file.seek(0,0)
    cont = len(file.read().split())
    file.seek(0,0)
    str_file = file.read()
    file.seek(0,0)
    junta = []
    vet = []
    j = 0
    aux_medias = []
    soma = []

    #GUARDANDO NOME DOS JOGADORES
    for i in range(0, cont, 6):
        vet.append(file.read().split()[i])
        file.seek(0,0)
        muda = "".join(vet[j])
        str_file = str_file.replace(muda, "")
        file.seek(0,0)
        j = j+1

    #RETIRANDO MAIORES E MENORES NOTAS
    for i in range(0, j):
        aux_maxmin = aux[i].replace(vet[i], "").replace(",","").split()
        maximo = max(aux_maxmin)
        minimo = min(aux_maxmin)
        mod.append(aux[i].replace(maximo, "").replace(minimo, ""))

    #RETIRANDO NOMES DUPLICADOS:
    vet_aux = vet
    vet = sorted(set(vet))

    #JUNTANDO NOMES IGUAIS:
    for i in range(0, len(vet)):
        for j in range(0, len(mod)):
            if vet[i] in mod[j]:
                junta.append(mod[j])

    #CALCULANDO MÉDIAS:
    aux_medias = "".join(junta)
    for i in range(0, len(vet)):
        aux_medias = aux_medias.replace(vet[i],"")
    split_aux = aux_medias.replace(",","").split()
    for i in range(0, len(split_aux), 3):
        somador = 0
        for j in range(i, i+3):
            somador = float(split_aux[j]) + somador
        soma.append(round(somador/3, 2))

    vet_aux = sorted(vet_aux)

    teste = []
    #JUNTANDO MEDIAS:
    teste = []
    var_media = []
    assistente = []
    for i in range(0, len(vet_aux)):
        testando = vet_aux[i], soma[i]
        teste.append(testando)
    teste = list(teste)
    for i in range(0, len(vet)):
        for j in range(0, len(teste)):
            if vet[i] in teste[j]:
                var_media.append(teste[j][1])
            if j == len(teste)-1:
                var_media.append("\n")
    for i in range(0, len(var_media)):
        lista = [str(i) for i in var_media]
    var_media = " ".join(lista).split("\n")

    #RETIRANDO A MAIOR E MENOR MEDIA:
    final = 0
    k = 0
    teste.clear()
    for i in range(0, len(var_media)-1):
        var_media[i] = sorted(var_media[i].split())[len(var_media[i].split())-2:len(var_media[i].split())]
    #SAIDA:
        final = 0
        for j in range(0,len(var_media[i])):
            final = float(var_media[i][j]) + final
        if i != len(var_media)-1:
            print("NOTA FINAL", "".join(vet[k]).replace(",", ":"), round(final, 2))
        k = k+1
except IndexError:
    print("\n\n                    Algo deu errado  :(")
=======
try:
    #ABRINDO ARQUIVO
    file = open("pontos.csv", "r")
    file.seek(0,0)

    #VARIAVEIS
    mod = []
    aux = file.readlines()
    file.seek(0,0)
    cont = len(file.read().split())
    file.seek(0,0)
    str_file = file.read()
    file.seek(0,0)
    junta = []
    vet = []
    j = 0
    aux_medias = []
    soma = []

    #GUARDANDO NOME DOS JOGADORES
    for i in range(0, cont, 6):
        vet.append(file.read().split()[i])
        file.seek(0,0)
        muda = "".join(vet[j])
        str_file = str_file.replace(muda, "")
        file.seek(0,0)
        j = j+1

    #RETIRANDO MAIORES E MENORES NOTAS
    for i in range(0, j):
        aux_maxmin = aux[i].replace(vet[i], "").replace(",","").split()
        maximo = max(aux_maxmin)
        minimo = min(aux_maxmin)
        mod.append(aux[i].replace(maximo, "").replace(minimo, ""))

    #RETIRANDO NOMES DUPLICADOS:
    vet_aux = vet
    vet = sorted(set(vet))

    #JUNTANDO NOMES IGUAIS:
    for i in range(0, len(vet)):
        for j in range(0, len(mod)):
            if vet[i] in mod[j]:
                junta.append(mod[j])

    #CALCULANDO MÉDIAS:
    aux_medias = "".join(junta)
    for i in range(0, len(vet)):
        aux_medias = aux_medias.replace(vet[i],"")
    split_aux = aux_medias.replace(",","").split()
    for i in range(0, len(split_aux), 3):
        somador = 0
        for j in range(i, i+3):
            somador = float(split_aux[j]) + somador
        soma.append(round(somador/3, 2))

    vet_aux = sorted(vet_aux)

    teste = []
    #JUNTANDO MEDIAS:
    teste = []
    var_media = []
    assistente = []
    for i in range(0, len(vet_aux)):
        testando = vet_aux[i], soma[i]
        teste.append(testando)
    teste = list(teste)
    for i in range(0, len(vet)):
        for j in range(0, len(teste)):
            if vet[i] in teste[j]:
                var_media.append(teste[j][1])
            if j == len(teste)-1:
                var_media.append("\n")
    for i in range(0, len(var_media)):
        lista = [str(i) for i in var_media]
    var_media = " ".join(lista).split("\n")

    #RETIRANDO A MAIOR E MENOR MEDIA:
    final = 0
    k = 0
    teste.clear()
    for i in range(0, len(var_media)-1):
        var_media[i] = sorted(var_media[i].split())[len(var_media[i].split())-2:len(var_media[i].split())]
    #SAIDA:
        final = 0
        for j in range(0,len(var_media[i])):
            final = float(var_media[i][j]) + final
        if i != len(var_media)-1:
            print("NOTA FINAL", "".join(vet[k]).replace(",", ":"), round(final, 2))
        k = k+1
except IndexError:
    print("\n\n                    Algo deu errado  :(")
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
    print("***********POR FAVOR, INSIRA 5 NOTAS POR JUÍZ***********")