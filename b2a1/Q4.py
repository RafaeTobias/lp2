<<<<<<< HEAD
file = open("sequencia.txt","r")

#TRANSCRIÇÂO
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
transforma = "".join(transforma)
file.seek(0,0)

#INICIALIZAÇÃO DE VAR 
str_file = transforma


#FORMATAÇÂO DA ENTRADA
seq = str_file
file.seek(0,0)
ini = "AUG"
aux = []

seq = seq[seq.find(ini): len(seq)]
Qtd = len(seq)//3
x=0

for i in range(0, Qtd):
    aux.append(seq[x: x+3]) 
    x = x + 3

aminoacidos = {
    'AUG' : 'Metionina',
    'UUU' : 'Fenilanina',
    'UUC' : 'Fenilanina',
    'UUA' : 'Leucina',
    'UUG' : 'Leucina',
    'CUU' : 'Leucina',
    'CUC' : 'Leucina',
    'CUA' : 'Leucina',
    'AUA' : 'Leucina',
    'AUU' : 'Isoleucina',
    'AUC' : 'Isoleucina',
    'AUA' : 'Isoleucina',
    'GUU' : 'Valina',
    'GUC' : 'Valina',
    'GUA' : 'Valina',
    'GUG' : 'Valina',
    'UCU' : 'Serina',
    'UCC' : 'Serina',
    'UCA' : 'Serina',
    'UCG' : 'Serina',
    'CCU' : 'Prolina',
    'CCC' : 'Prolina',
    'CCA' : 'Prolina',
    'CCG' : 'Prolina',
    'ACU' : 'Treonina',
    'ACC' : 'Treonina',
    'ACA' : 'Treonina',
    'ACG' : 'Treonina',
    'GCU' : 'Alanina',
    'GCC' : 'Alanina',
    'GCA' : 'Alanina',
    'GCG' : 'Alanina',
    'UAU' : 'Tirosina',
    'UAC' : 'Tirosina',
    'UAA' : 'STOP CODON',
    'UAG' : 'STOP CODON',
    'CAU' : 'Histidina',
    'CAC' : 'Histidina',
    'CAA' : 'Glutamina',
    'CAC' : 'Glutamina',
    'AAU' : 'Asparagina',
    'AAC' : 'Asparagina',
    'AAA' : 'Lisina',
    'AAG' : 'Lisina',
    'GAU' : 'Ácido Aspártico',
    'GAC' : 'Ácido Aspártico',
    'GAA' : 'Ácido Glutômico',
    'GAG' : 'Ácido Glutômico',
    'UGU' : 'Cysteine',
    'UGC' : 'Cysteine',
    'UGA' : 'STOP CODON',
    'UGG' : 'Tryptophan',
    'CGU' : 'Arginina',
    'CGC' : 'Arginina',
    'CGA' : 'Arginina',
    'CGG' : 'Arginina',
    'AGU' : 'Serina',
    'AGC' : 'Serina',
    'AGA' : 'Arginina',
    'AGG' : 'Arginina',
    'GGU' : 'Glicina',
    'GGC' : 'Glicina',
    'GGA' : 'Glicina',
    'GGG' : 'Glicina'
}

try:
    str_file = transforma
    file.seek(0,0)
    print("Sequencia:", file.read(), "\nAminoácidos correspondentes:")
    for i in range(0, len(aux)):
        print("Aminoácido:", aminoacidos[aux[i]], "(" + aux[i] + ")")
    file.close()
except:
=======
file = open("sequencia.txt","r")

#TRANSCRIÇÂO
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
transforma = "".join(transforma)
file.seek(0,0)

#INICIALIZAÇÃO DE VAR 
str_file = transforma


#FORMATAÇÂO DA ENTRADA
seq = str_file
file.seek(0,0)
ini = "AUG"
aux = []

seq = seq[seq.find(ini): len(seq)]
Qtd = len(seq)//3
x=0

for i in range(0, Qtd):
    aux.append(seq[x: x+3]) 
    x = x + 3

aminoacidos = {
    'AUG' : 'Metionina',
    'UUU' : 'Fenilanina',
    'UUC' : 'Fenilanina',
    'UUA' : 'Leucina',
    'UUG' : 'Leucina',
    'CUU' : 'Leucina',
    'CUC' : 'Leucina',
    'CUA' : 'Leucina',
    'AUA' : 'Leucina',
    'AUU' : 'Isoleucina',
    'AUC' : 'Isoleucina',
    'AUA' : 'Isoleucina',
    'GUU' : 'Valina',
    'GUC' : 'Valina',
    'GUA' : 'Valina',
    'GUG' : 'Valina',
    'UCU' : 'Serina',
    'UCC' : 'Serina',
    'UCA' : 'Serina',
    'UCG' : 'Serina',
    'CCU' : 'Prolina',
    'CCC' : 'Prolina',
    'CCA' : 'Prolina',
    'CCG' : 'Prolina',
    'ACU' : 'Treonina',
    'ACC' : 'Treonina',
    'ACA' : 'Treonina',
    'ACG' : 'Treonina',
    'GCU' : 'Alanina',
    'GCC' : 'Alanina',
    'GCA' : 'Alanina',
    'GCG' : 'Alanina',
    'UAU' : 'Tirosina',
    'UAC' : 'Tirosina',
    'UAA' : 'STOP CODON',
    'UAG' : 'STOP CODON',
    'CAU' : 'Histidina',
    'CAC' : 'Histidina',
    'CAA' : 'Glutamina',
    'CAC' : 'Glutamina',
    'AAU' : 'Asparagina',
    'AAC' : 'Asparagina',
    'AAA' : 'Lisina',
    'AAG' : 'Lisina',
    'GAU' : 'Ácido Aspártico',
    'GAC' : 'Ácido Aspártico',
    'GAA' : 'Ácido Glutômico',
    'GAG' : 'Ácido Glutômico',
    'UGU' : 'Cysteine',
    'UGC' : 'Cysteine',
    'UGA' : 'STOP CODON',
    'UGG' : 'Tryptophan',
    'CGU' : 'Arginina',
    'CGC' : 'Arginina',
    'CGA' : 'Arginina',
    'CGG' : 'Arginina',
    'AGU' : 'Serina',
    'AGC' : 'Serina',
    'AGA' : 'Arginina',
    'AGG' : 'Arginina',
    'GGU' : 'Glicina',
    'GGC' : 'Glicina',
    'GGA' : 'Glicina',
    'GGG' : 'Glicina'
}

try:
    str_file = transforma
    file.seek(0,0)
    print("Sequencia:", file.read(), "\nAminoácidos correspondentes:")
    for i in range(0, len(aux)):
        print("Aminoácido:", aminoacidos[aux[i]], "(" + aux[i] + ")")
    file.close()
except:
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
    print("\n******** ALGO DEU ERRADO ********\nPor favor, entre com uma sequência válida\n")