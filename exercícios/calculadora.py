import sys


class Calculadora:
    def __init__(self, valor1, valor2, operador):
        self.__valor1 = float(valor1)
        self.__valor2 = float(valor2)
        self.__operador = operador

    @property
    def valor1(self):
        return self.__valor1

    @property
    def valor2(self):
        return self.__valor2

    @property
    def operador(self):
        return self.__operador

    @operador.setter
    def operador(self, operador):
        self.__operador = operador

    @valor1.setter
    def valor1(self, valor1):
        self.__valor1 = valor1

    @valor2.setter
    def valor2(self, valor2):
        self.__valor2 = valor2

    def inicia_calculo(self):
        return self.verifica_operacao()

    def verifica_operacao(self):
        if self.__operador == '+':
            return self.chama_somatoria()
        elif self.__operador == '-':
            return self.chama_subtracao()
        elif self.__operador == '*' or self.__operador == 'x':
            return self.chama_multiplicacao()
        elif self.__operador == '/':
            return self.chama_divisao()
        else:
            raise ValueError("Operador inválido")

    def chama_somatoria(self):
        return round((self.__valor1 + self.__valor2), 2)

    def chama_subtracao(self):
        return round((self.__valor1 - self.__valor2), 2)

    def chama_multiplicacao(self):
        return round((self.__valor1 * self.__valor2), 2)

    def chama_divisao(self):
        return round((self.__valor1 / self.__valor2), 2)


calculadora = Calculadora(10.2, 3.44, '+')
print(calculadora.inicia_calculo())
