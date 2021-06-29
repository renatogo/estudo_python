def jogar_forca():
    print("**********************************")
    print("****Bem vindo ao Joga da Forca****")
    print("**********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip() # retira os espaços em branco do início e fim da string

        index = 0
        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                print("Encontrado a letra {} no indiex {}".format(chute, index))
            index = index + 1

    print("Fim do Jogo")

# identifica se a classe está sendo chamada de outra classe (import) ou se está sendo chamada diretamente
if __name__ == "__main__":
    jogar_forca()