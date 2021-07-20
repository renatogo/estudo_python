from validador_placa_mercosul import ValidaPlacaMercosul

validador = ValidaPlacaMercosul("RIO2A18")
retorno = validador.is_valid()
if retorno:
    print("A Placa está no padrão: ", validador)
else:
    print("A Placa não está no padrão: ", validador)
