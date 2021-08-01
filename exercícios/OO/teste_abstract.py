from abc import ABCMeta, abstractmethod


class Pai(metaclass=ABCMeta):
    def __init__(self, atributo1):
        self._atributo1 = atributo1

    @property
    def atributo1(self):
        return self._atributo1

    @atributo1.setter
    def atributo1(self, atributo1):
        self._atributo1 = atributo1

    @abstractmethod
    def metodo_abstrato(self):
        print("Este eh o metodo abstrato da classe pai")


class Filho(Pai):
    def __init__(self, atributo1, atributo2):
        super().__init__(atributo1)
        self._atributo2 = atributo2

    @property
    def atributo2(self):
        return self._atributo2

    @atributo2.setter
    def atributo2(self, atributo2):
        self._atributo2 = atributo2

    def metodo_abstrato(self):
        print("Este eh o metodo da classe filha")


filho = Filho("atributo1", "atributo2")
filho.metodo_abstrato()