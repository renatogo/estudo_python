def jogar_forca():
    print("**********************************")
    print("****Bem vindo ao Joga da Forca****")
    print("**********************************")

    palavra_secreta = "banana".upper()
    # letras_acertadas = ["_","_","_","_","_","_"]
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        print(letras_acertadas)
        chute = input("Qual letra? ")
        chute = chute.strip().upper()  # retira os espaços em branco do início e fim da string

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.lower() == letra.lower():
                    letras_acertadas[index] = letra
                    #  print("Encontrado a letra {} no indiex {}".format(chute, index))
                index += 1
        else:
            erros += 1
    enforcou = erros == len(palavra_secreta)
    acerto = "_" not in letras_acertadas

    if acertou:
        print("Você acertou!!!")
    else:
        print("Você errou!!!")

    print("Fim do Jogo")

# identifica se a classe está sendo chamada de outra classe (import) ou se está sendo chamada diretamente
if __name__ == "__main__":
    jogar_forca()
