# Realiza a leitura de um arquivo em disco

def inicia_leitura():
    linhas_arquivo = []
    arquivo = open("teste.txt", "r")
    for linha in arquivo:
        linhas_arquivo.append(linha.strip())
    arquivo.close()

    print(linhas_arquivo)

if __name__ == "__main__":
   inicia_leitura()
