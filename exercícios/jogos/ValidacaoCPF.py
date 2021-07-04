# Realiza a validação de um determinado CPF utilizando o algorítmo módulo 11
# Referência para o algorítmo: https://www.somatematica.com.br/faq/cpf.php

# declaração do CPF a validar
cpf = "25899770856"
# declaracao de tupla com multiplicadores
fatores_multiplicacao_primeiro_digito = (10, 9, 8, 7, 6, 5, 4, 3, 2)
fatores_multiplicacao_segundo_digito = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
# declaracao dos digitos
primeiro_digito = 0
segundo_digito = 0

def cpfvalido():
    # calculo do primeiro digito
    somatoria = 0
    indice = 0
    # realiza um loop aplicando a multiplicação em casa dígito do CPF
    for fator in fatores_multiplicacao_primeiro_digito:
        somatoria += (int(cpf[indice]) * fatores_multiplicacao_primeiro_digito[indice])
        indice += 1

    # calcula o primeiro dígito verificador
    resto = somatoria % 11
    if resto == 0 or resto == 1:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    # calculo do segundo digito
    somatoria = 0
    indice = 0
    # realiza um loop aplicando a multiplicação em casa dígito do CPF
    for fator in fatores_multiplicacao_segundo_digito:
        somatoria += (int(cpf[indice]) * fatores_multiplicacao_segundo_digito[indice])
        indice += 1

        # calcula o segundo dígito verificador
        resto = somatoria % 11
        if resto == 0 or resto == 1:
            segundo_digito = 0
        else:
            segundo_digito = 11 - resto

    # verifica se o CPF informado é válido, de acordo com os dígitos verificadores calculados
    if int(cpf[len(cpf) - 2]) == primeiro_digito and int(cpf[len(cpf)-1])  == segundo_digito:
        print("CPF Válido !!!")
    else:
        print("CPF inválido !!!")

# realiza a chamada para o método de cálculo
if __name__ == "__main__":
    cpfvalido()
