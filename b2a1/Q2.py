<<<<<<< HEAD
file = open("sequencia.txt","r")
file.seek(0,0)
str_file = list(file.read())#resposta:len 15
file.seek(0,0)
for i in range(0, len(str_file)):
    if str_file[i] == "A":
        str_file[i] = 'T'
    else:
        if str_file[i] == 'T':
            str_file[i] = 'A'
        else:
            if str_file[i] == 'G':
                str_file[i] = 'C'
            else:
                str_file[i] = 'G'
print("Sequencia Obtida:", file.read(), "\nFita complementar:", "".join(str_file))
file.close
=======
file = open("sequencia.txt","r")
file.seek(0,0)
str_file = list(file.read())#resposta:len 15
file.seek(0,0)
for i in range(0, len(str_file)):
    if str_file[i] == "A":
        str_file[i] = 'T'
    else:
        if str_file[i] == 'T':
            str_file[i] = 'A'
        else:
            if str_file[i] == 'G':
                str_file[i] = 'C'
            else:
                str_file[i] = 'G'
print("Sequencia Obtida:", file.read(), "\nFita complementar:", "".join(str_file))
file.close
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
