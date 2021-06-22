# Gera uma sequencia de fibonacci

# declaração de variáveis
primeiro_valor = 1
segundo_valor = 1
valor_final = primeiro_valor + segundo_valor
numero_iteracoes = 5

# imprime os valores
print("sequeência", primeiro_valor, segundo_valor, valor_final)

# lopp pelo número de iterações
while(numero_iteracoes > 0):
    primeiro_valor = segundo_valor
    segundo_valor = valor_final
    valor_final = primeiro_valor + segundo_valor

    numero_iteracoes = numero_iteracoes - 1
    print("sequência", primeiro_valor, segundo_valor, valor_final)