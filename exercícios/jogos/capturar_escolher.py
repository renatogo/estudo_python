# exercício considerando captura de dados na tela e escolha

import random

# gera um número randômico entre 1 e 30 para escolha
numero_gerado = random.randrange(1, 30+1)
acertou = False

while(not acertou):
    escolha = int(input("Digite um número: "))

    if (escolha < numero_gerado):
        print("Você escolheu um número menor do que o gerado")

    elif(escolha > numero_gerado):
        print("Você escolheu um número maior do que o gerado")

    else:
        print("Você acertou")
        acertou = True
