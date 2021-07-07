

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # definindo uma método como @property, permite que ele seja chamado no lugar do atributo direto, mesmo chamando diretamente o atributo
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title() # retorna a primeira letra em maiusculo

    @nome.setter
    def nome(self, nome):
        print("chamando o setter")
        self.__nome = nome

if __name__ == "__main__":
    cliente = Cliente("renato")
    # exemplo de chamada de um método property
    print(cliente.nome)
    cliente.nome = "Bene"
    print(cliente.nome)
