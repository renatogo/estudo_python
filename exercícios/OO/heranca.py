class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @ano.setter
    def ano(self, ano):
        self._ano = ano


class Filme (Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    def __str__(self):
        return "O filme {} foi lançado em {} e tem {} minutos de duração".format(self.nome, self.ano, self.duracao)


class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas

    def __str__(self):
        return "A serie {} foi lançada em {} e tem {} temporadas".format(self.nome, self.ano, self.temporadas)

class PlayList:
    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas

    @property
    def listagem(self):
        return self.__programas

    @property
    def tamanho(self):
        return len(self.__programas)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def programas(self):
        return self.__programas

    @programas.setter
    def programas(self, programas):
        self.__programas = programas

    # possibilita tornar a playlist iterável (comportamento de list)
    def __getitem__(self, item):
        return self.programas[item]

    def __len__(self):
        return len(self.__programas)


# iniciando os testes
filme = Filme("De volta para o futuro", 1985, 120)
serie = Serie("Rebels", 2008, 4)

programas = [filme, serie]

playlist = PlayList("favoritos", programas)

print("Minha playlist {} possui {} programas".format(playlist.nome, len(playlist)))

for programa in playlist:
    print(programa)
