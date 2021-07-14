url="https://bytebank.com/cambio?moedaOrigem=real&moedaDEstino=dolar&quantidade=100"
print(url)

url_base=url[0:27]
print(url_base)

url_parametro_moeda_origem=url[28:44]
print(url_parametro_moeda_origem)

# utilizando o método find
indice_interrogacao = url.find("?")

url_base=url[0:indice_interrogacao]
print(url_base)

url_parametro_moeda_origem=url[indice_interrogacao+1:44]
print(url_parametro_moeda_origem)