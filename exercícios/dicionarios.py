#criando um dicionário de dados
telefones = {"Renato":"984377726", "Bene":"975258914", "Rafael":"984775588", "Vovô":"985166330"}
# imprime diretamente o dicionario
print(telefones)

# imprime um item do dicionario
print(telefones["Renato"])
# outra maneira de recuperar dados do dicionario
print(telefones.get("Renato", "Contato náo encontrado")) # segundo parametro é retornado caso a chave não seja localizada
print(type(telefones))

# verificar se uma determinada chave está no dicionário
print("Nome encontrado" if "Bella" in telefones else "Nome não encontrado")

# busca pelo número do telefone no dicionário (values)
print("Número encontrado" if "984377725" in telefones.values() else "Número não encontrado")

# adicionando valores no dicionário
telefones["Novo contado"] = "988885555"

print(telefones["Novo contado"])

# removendo itens do dicionário
telefones.pop("Novo contato", "Contato não encontrado")
print(telefones)