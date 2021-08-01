class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Conta: código {} saldo {}".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def debita_taxa(self, taxa):
        self._saldo -= taxa


class ContaPoupanca(Conta):
    def rendimento_taxa(self, taxa):
        self._saldo *= 1.01
        self._saldo -= taxa


minha_conta = ContaCorrente(1000)
minha_conta.deposita(100)
print(minha_conta)

outra_conta = ContaPoupanca(2000)
outra_conta.deposita(200)
print(outra_conta)

contas = [minha_conta, outra_conta]
print(contas)

for conta in contas:
    print(conta)

# criado tuplas - não permiste mudancas na lista (inclusão ou remocão de itens)
contas_tupla = (minha_conta, outra_conta)

for conta_tupla in contas_tupla:
    print(conta_tupla)