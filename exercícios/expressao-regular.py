import re # Expressão Regular -- RegEx

# buscar o CEP dentro de um endereço
#formato do CEP = 5 dígitos + hífen (opcional) + 3 dígitos

endereco = "Rua Botelho, 155 apto 131 - CEP: 04313200 - São Paulo - SP"

# usar o método compile para formatação
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) # Match
if busca:
	cep = busca.group()
	print(cep) 
