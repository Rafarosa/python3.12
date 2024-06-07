""" 
Tipo Float
Tipo real ou Decimal

Casas decimais

OBS: O separador de casas decimais na programação é ponto
"""

# errado (Considera como tupla)
valor = 1,44
print(valor)
print(type(valor))


# certo (Considerado valor float)
valor = 1.44
print(valor)
print(type(valor))

# Podemos convertar float para int
""" Ao realizar a conversão, perdemos as casas de precissão"""
res = int(valor)
print(res)
print(type(res))