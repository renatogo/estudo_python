class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "Conta: código {} saldo {}".format(self.codigo, self.saldo)


minha_conta = ContaCorrente(1000)
minha_conta.deposita(100)
print(minha_conta)

outra_conta = ContaCorrente(2000)
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