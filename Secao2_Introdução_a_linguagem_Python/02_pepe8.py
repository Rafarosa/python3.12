""" 
Import this
O Zen do Python, de Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aninhado.
Esparso é melhor que denso.
A legibilidade conta.
Casos especiais não são especiais o suficiente para quebrar as regras.
Embora a praticidade supere a pureza.
Os erros nunca devem passar silenciosamente.
A menos que seja explicitamente silenciado.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deveria haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
Embora essa forma possa não ser óbvia à primeira vista, a menos que você seja holandês.
Agora é melhor do que nunca.
Embora nunca seja melhor do que *agora*.
Se a implementação for difícil de explicar, é uma má ideia.
Se a implementação for fácil de explicar, pode ser uma boa ideia.
Namespaces são uma ótima ideia - vamos fazer mais deles!

"""
## PeP 8
## https://peps.python.org/pep-0008/

"""
[1] -  Utilize Camel Case para nomes de classes;
"""


class Calculadora:
    pass

"""
[2] -  Utilize nomes em minúsculo, separados pro underline para funções ou variáveis 
"""

def soma():
    pass


class soma_dois():
    pass


""" 
[3] - Utilize 4 espaços para identação!
"""

if 'a' in 'banana':
    print('Tem')

"""
[4] - Linhas em branco
- Separar funções e definições de classe cm duas linhas em branco;
- Métodos dentro de uma classe deve ser separados com uma unica linha em branco
"""


class Class:
    pass


class clsass:
    pass

""" 
[5] -  Imports

- Imports deve sempre ser feitos em linhas Separadas

Errado
import sys, os

Certo
import Sys
import os

- Não há problema em utilizar:
from types import StringType, ListTyps

- Caso tenha muitos imports de um mesmo pacote, recomendamos fazer:

from types import (
    Stringtype,
    ListTipe,
    SetType,
    OutroType
)

- Imports devem ser colocados no topo do topo do arquivo, logo depois de qualquer comentário ou docstring
- Antes de constantes ou variáveis globais

[6] - Espaços em expressões e instruções 
"""
# Não faça
fucao( algo[ 1 ], { outro: 2 })
dict ['chave'] = lsita [ indice]

# Faça
funcao(algo[1], {outro: 2})
dict['chave'] = lsita[indice]

""" 
[7] - termine uma instrução sempre com uma nova linha
"""
