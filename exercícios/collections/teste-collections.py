idades = [9, 15, 45, 48]

print(type(idades))
print(len(idades))
print(idades)

idades.append(1)

print(idades)

# exemplo de for que já atualiza uma lista gerando uma nova
print([(idade+1) for idade in idades])