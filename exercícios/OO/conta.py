

class Conta:

    codigo_banco = "001" # este atributo é estático pois está definido fora do construtor __init__

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo R$ {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        print("Saldo atualizado após o depósito R$ {}".format(self.__saldo))

    def sacar(self, valor):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite da conta {}".format(valor, self.__numero))
        print("Saldo atualizado após o saque R$ {}".format(self.__saldo))

    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite

    def set_saldo(self, saldo):
        self.__saldo =  saldo

    def set_titular(self, titular):
        self.__titular = titular

    def set_numero(self, numero):
        self.__numero = numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return Conta.condigo_banco

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Itau':'301'}


