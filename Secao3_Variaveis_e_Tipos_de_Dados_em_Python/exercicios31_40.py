""" 
31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""
num_int = int(input('Informe um número inteiro para mostar seu antecessor e o seu sucessor: '))
ante = num_int - 1
suce = num_int + 1

print(f'O número informado foi {num_int}, seu antecessor é {ante} e seu sucessor {suce}')

"""
32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
seu dobro.
"""
num_int = int(input('Informe um número inteiro para mostar a soma do sucessor de seu triplo com o antecessor de seu dobro: '))

suce_trip = (num_int*3)+1
ante_drob = (num_int*2)-1
soma_total = suce_trip + ante_drob

print(f'A soma do sucessor de seu triplo com o antecessor de seu dobro é {soma_total}')

"""
33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
"""
lado = float(input('Informe o tamanho do lado do seu quadrado para gerar a sua área: '))

area_quadrado = lado*lado

print(f'O lado de seu quadrado mede {lado}, a área desse quadrado {area_quadrado} ')

"""
34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
AA área do circulo é 7 «+ raio?, considere x = 3.141592.
"""
raio = float(input('Informe o Raio do círculo para descobrir sua área: '))

circ_area = 3.14*(raio**2)

print(f'A área do círculo é igual a {circ_area}')

"""
35. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = √a² + b². Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""
cateto_a = float(input('Informe o Cateto "A" do triângulo: '))
cateto_b = float(input('Informe o Cateto "B" do triângulo: '))

hipotenusa = ((cateto_a**2)+(cateto_b**2))**0.5

print(f'O valor da hipotenuas é {hipotenusa:.2f}')

"""
36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = x «raio? + altura,
onde 7 = 3.141592.
"""
h_cilindro = float(input('Informe a altura do cilindro: '))
raio = float(input('Informe o raio do cilindro: '))

vol_cilindro = 3.14*(raio**2)*h_cilindro

print(f'O volume deste cilindro é de {vol_cilindro}m³ ')

"""
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%
"""
valor_produto = float(input('Informe o valor do produto: '))

valor_desconto = valor_produto*0.12
valor_venda = valor_produto-valor_desconto

print(f'O Valor do produto com desconto fica {valor_venda}')

"""
38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%.

"""
salario = float(input('Informe o salário do funcionário: '))

aumento_salarial = salario*0.25
novo_salario = salario + aumento_salarial

print(f'Parabéns!!! seu novo salário é de R${novo_salario}')

"""
39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:

 -  O primeiro ganhador receberá 46%;
 -  O segundo receberá 32%;
 -  O terceiro receberá o restante;

Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
importancia = 780000

primeiro_ganhador = importancia*0.42
segundo_ganhador = importancia*0.32
terceiro_ganhador = primeiro_ganhador + segundo_ganhador

print(f'A divisão do premido de R${importancia} ficom assim:\n primeiro ganhagor recebera R${primeiro_ganhador}\n Segundo ganhador recebera R${segundo_ganhador}\n e o terceiro ganhador recebera R${terceiro_ganhador}')

"""
40. Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""

valor_diaria_encanador = 30

dias_trabalhados = int(input('Informe quantos dias o encanador trabalhou na obra: '))

valor_pago = valor_diaria_encanador * dias_trabalhados

valor_liquido = valor_pago-(valor_pago*0.08)

print(f'O valor a ser pago por {dias_trabalhados} dias trabalhados é de R${valor_pago} sendo o valor liquido de R${valor_liquido} ')
