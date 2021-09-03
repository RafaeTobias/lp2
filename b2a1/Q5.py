<<<<<<< HEAD
import os
#ABERTURA DO ARQUIVO
file = open("sequencia.txt","r")
os.system("color a")

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

#INICIALIZAÇÃO DE VAR 
str_file = transforma
file.seek(0,0)
start = 0
pause = 0

#DICIONARIO
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

#LÓGICA PRINCIPAL
try:
    for i in aux:
        if i == 'AUG':
            break
        else:
            start = start + 1
    for i in aux:
        if i == 'UAA' or i == 'UAG' or i == 'UGA':
            break
        else:
            pause = pause + 1
    print("Sequencia Obtida:", file.read().rjust(43), "\nTranscrição para RNA: ", transforma, "\nAminoacidos sintetizados:")
    for i in range(0, pause):
        print("Aminoácido:", aminoacidos[aux[i]], "(" + aux[i] + ")")
    print("STOP CÓDON:", aux[pause], "(" + aux[pause] + ")")
except:
    print("\n******** ALGO DEU ERRADO ********\nPor favor, entre com uma sequência válida\n")
=======

import os

#ABERTURA DO ARQUIVO
file = open("sequencia.txt","r")
os.system("color a")

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

#INICIALIZAÇÃO DE VAR 
str_file = transforma
file.seek(0,0)
start = 0
pause = 0

#DICIONARIO
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

#LÓGICA PRINCIPAL
try:
    for i in aux:
        if i == 'AUG':
            break
        else:
            start = start + 1
    for i in aux:
        if i == 'UAA' or i == 'UAG' or i == 'UGA':
            break
        else:
            pause = pause + 1
    print("Sequencia Obtida:", file.read().rjust(43), "\nTranscrição para RNA: ", transforma, "\nAminoacidos sintetizados:")
    for i in range(0, pause):
        print("Aminoácido:", aminoacidos[aux[i]], "(" + aux[i] + ")")
    print("STOP CÓDON:", aux[pause], "(" + aux[pause] + ")")
except:
    print("\n******** ALGO DEU ERRADO ********\nPor favor, entre com uma sequência válida\n")
>>>>>>> 7c60400bde24298ea92d8c3c536e43bfff0df896
