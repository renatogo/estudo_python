''' Realiza a validação de uma placa de carro no padrão mercosul
ou seja, 3 letras + 1 número + 1 letra + 2 números. Ex: RIO2A18 '''

import re


class ValidaPlacaMercosul:
    def __init__(self, placa):
        self.__placa = placa

    def is_valid(self):
        padrao = re.compile("[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}")
        valido = padrao.match(self.__placa)
        if valido:
            return True
        else:
            return False

    def __str__(self):
        return self.__placa
