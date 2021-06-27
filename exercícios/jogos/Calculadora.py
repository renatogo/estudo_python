print("*****************************")
print("*********Calculadora*********")
print("*****************************")

# declaracão das variáveis
resultado: float
executar_calculadora: bool = True

# verifica qual é o operador escolhido e aplica o mesmo nos números informados

while executar_calculadora:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    operador = input("Digite o operador matemático ou e para sair: ")

    if operador == "+":
        resultado = valor1 + valor2
    elif operador == "-":
        resultado = valor1 - valor2
    elif operador == "*":
        resultado = valor1 * valor2
    elif operador == "/":
        resultado = valor1 / valor2
    elif operador == "e":
        exit(0)
    else:
        print("Operador inválido")
        exit(0)

    print("Resultado da operacão ", resultado)

print("*********Fim da Calculadora**")
