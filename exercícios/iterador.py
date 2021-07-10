class IteradorFamilia:
    def __init__(self):
        self.arquivo = open("arquivo_familia", "r")
        self.membro_familia = ""

    def __iter__(self):
        return self

    def __next__(self):
        self.membro_familia = self.arquivo.readline()
        while self.membro_familia != ' ':
            return self.membro_familia
            exit(0)



iterador = IteradorFamilia()

for membro in iterador:
    print(membro, end="")
