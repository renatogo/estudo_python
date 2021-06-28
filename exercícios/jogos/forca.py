def jogar_forca():
    print("**********************************")
    print("****Bem vindo ao Joga da Forca****")
    print("**********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    # enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        print("jogando ...")

    print("Fim do Jogo")

# identifica se a classe está sendo chamada de outra classe (import) ou se está sendo chamada diretamente
if __name__ == "__main__":
    jogar_forca()