print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

# declaração das variáveis
numero_secreto = 42
numero_tentativas = 3
total_tentativas = numero_tentativas
chute = 0
rodada = 1

# testes cíclicos
while (numero_tentativas > 0):
    print("Tentativa {} de {}:".format(rodada, total_tentativas))
    # recupera o valor digitado na tela
    chute = input("Digite o seu número: ")
    print("Você digitou: ", chute)

    # declaração de variáveis associadas a operações
    acertou = numero_secreto == int(chute)
    maior = int(chute) > numero_secreto
    menor = int(chute) < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número correto")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto")

    numero_tentativas = numero_tentativas - 1
    rodada = rodada + 1

print("Fim do jogo Renato!")
