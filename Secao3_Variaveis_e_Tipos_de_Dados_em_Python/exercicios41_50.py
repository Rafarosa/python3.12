""" 
41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
hora_trabalhada = float(input('Informe o valor da hora trabalhada (R$): '))
horas_trab_mes = int(input('Quantas horas você trabalhou este mês: '))

valor_bruto = hora_trabalhada*horas_trab_mes
valor_adicional = valor_bruto + (valor_bruto*0.1)

print(f'O valor do trabalho esse mês foi de R${valor_bruto}, foi criditado 10% a mais, sendo depositado R${valor_adicional}')

42. Recebao salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
salario_base = float(input('Informe o salário base do funcionario: '))

gratificacao = salario_base*0.05

imposto = salario_base*0.07

salario_l = salario_base + gratificacao - imposto

print(f'O Salário base do funcionário é R${salario_base:.2f}, sua gratificação é de RS{gratificacao},o recolhimento de imposto foi de R${imposto:.2f}')
print(f'O salário Liquido do funcionário é de R${salario_l}')

43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

-  o total a pagar com desconto de 10%;

- o valor de cada parcela, no parcelamento de 3x sem juros;

- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des-
conto)

- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
valor_venda = float(input('Informe o valor total da venda para ver as opções de pagamento: '))

valor_a_vista = valor_venda - (valor_venda*0.1)

parcelado = valor_venda / 3

comissao_a_vista = valor_a_vista*0.05

comossao_parcelado = valor_venda*0.05

print(f'Valor toral a vista fica em R${valor_a_vista}, já com 10% de\nSe desejar pagar parcelado, o valor da parcela é de R${parcelado:.2f}')
print(f'Se a venda for a vista, a comissão do vendedor é de R${comissao_a_vista}')
print(f'Se a venda for parcelada, a comissão para o vendedor será de R${comossao_parcelado}')

44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
degral_h = float(input('Informe a altura dos degraus da sua escada: '))
altura = float(input('Informe a alturaque deseja chegar: '))

qt_degraus = int(altura/degral_h)

print(f'para chegar a altura de {altura}m, com degraus a {degral_h}m, você deve subir {qt_degraus} degraus')

45. Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema.
letra = str(input('Informe a letra em maiúsculo:'))

# retorna o valor unicode do str
mai_ascii = ord(letra)
# retorna o str do valor unicode
min_ascii = chr(mai_ascii + 32)

print(f'Convetendo para minúscula: {min_ascii}')

46. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:

NúmeroLido = 123
NúmeroGerado = 321.

num_int = int(input('Informe um numero inteiro de 3 digitos (entre 100 a 999): '))
num_str=str(num_int)

print(f'O número invertido fica {num_str[::-1]}')


47. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
num_int4= int(input('Informe um numero inteiro de 4 digitos (entre 1000 a 9999): '))
num_str4=str(num_int4)

print(f'{num_str4[0]}\n{num_str4[1]}\n{num_str4[2]}\n{num_str4[3]}\n')


48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
segundos = int(input('Informe o valor em segundos para descobrir quantas horas, minutos e segundos tem: '))

horas = segundos // 3600
print(horas)
segundos_restantes = segundos % 3600
print(segundos_restantes)
minutos = segundos_restantes // 60
print(minutos)
segundos_restantes = segundos_restantes % 60
print(segundos_restantes)

print(f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}")

49. Faça um programa para leia o horário (hora, minuto e segundo) de início e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma.
"""

"""
50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual.

""" 