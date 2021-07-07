

class Jogador:

    def __init__(self, nome, num_camisa, posicao):
        self.__nome = nome
        self.__num_camisa = num_camisa
        self.__posicao = posicao

    @property
    def nome(self):
        return self.__nome

    @property
    def num_camisa(self):
        return self.__num_camisa

    @property
    def posicao(self):
        return self.__posicao

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @num_camisa.setter
    def num_camisa(self, num_camisa):
        self.__num_camisa = num_camisa

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    def __str__(self):
        return "Jogador {} camisa {} que joga na posição{} ".format(self.__nome, self.__num_camisa, self.__posicao)