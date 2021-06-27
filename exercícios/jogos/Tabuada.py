# Imprime tabuada dos números entre 1 e 10

valor_inicial: int = 1
valor_final: int = 10
tabuada_inicial: int = 1
tabuada_final: int = 10

# loop até a tabuada final
while tabuada_inicial <= tabuada_final:
    # realiza um loop até o valor final
    while valor_inicial <= valor_final:
        print(tabuada_inicial, " * ", valor_inicial, " = ", tabuada_inicial * valor_inicial, end="\n")
        valor_inicial = valor_inicial + 1

    print("", end="\n")
    valor_inicial = 1
    tabuada_inicial = tabuada_inicial + 1
