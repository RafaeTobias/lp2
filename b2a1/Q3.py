<<<<<<< HEAD
file = open("sequencia.txt","r")
file.seek(0,0)
transforma = list(file.read())#resposta:len 15
"".join(transforma).replace(" ","")
file.seek(0,0)
for i in range(0, len(transforma)):
    if transforma[i] == "A":
        transforma[i] = 'U'
    else:
        if transforma[i] == 'T':
            transforma[i] = 'A'
        else:
            if transforma[i] == 'G':
                transforma[i] = 'C'
            else:
                transforma[i] = 'G'

print("Sequencia:", " ".join("".join(file.read()).split()), "\nTranscrição para RNA:", "".join(transforma))
file.close()
=======
file = open("sequencia.txt","r")
file.seek(0,0)
transforma = list(file.read())#resposta:len 15
"".join(transforma).replace(" ","")
file.seek(0,0)
for i in range(0, len(transforma)):
    if transforma[i] == "A":
        transforma[i] = 'U'
    else:
        if transforma[i] == 'T':
            transforma[i] = 'A'
        else:
            if transforma[i] == 'G':
                transforma[i] = 'C'
            else:
                transforma[i] = 'G'

print("Sequencia:", " ".join("".join(file.read()).split()), "\nTranscrição para RNA:", "".join(transforma))
file.close()
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
