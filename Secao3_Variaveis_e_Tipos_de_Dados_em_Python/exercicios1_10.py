""" 
1 Faça um programa que leia um número inteiro e o imprima.
""" 
num_int = int(input('Informe um número inteiro: '))
print(f'O número informado foi {num_int}')
""" 
2 - Faça um programa que leia um número real e o imprima.
""" 
num_real = float(input('Informe um número real: '))
print(f'O número informado foi {num_real}')
""" 
3 -  Peça ao usuários para digitar três numero inteiro e imprima a soma deles
""" 
num_1_3 = float(input('Informe o primeiro número: '))
num_2_3 = float(input('Informe o segundo número: '))
num_3_3 = float(input('Informe o terceiro número: '))

soma_3 = num_1_3 + num_2_3 + num_3_3

print(f'A soma dos números informado é {soma_3}')
""" 
4. Leia um número real e imprima o resultado do quadrado desse número.
""" 
num_1_4 = float(input('Informe um numero real para saber o seu quadrado: '))
num_quadrado = num_1_4**2

print(f'O quadrado do valor {num_1_4} é {num_quadrado}')

""" 
5. Leia um número real e imprima a quinta parte deste número.
""" 
num_1_5 = float(input('Informe um numero real para sua quinta parte: '))
quinta_parte = num_1_5 / 5

print(f'A quinta parte de {num_1_5} é {quinta_parte:.2f}')
""" 
6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C+(9.0/5.0)--32.0, sendo F a temperatura em Fahrenheit
e C atemperatura em Celsius.
""" 

celsius = float(input('Informe a temperatura em graus Celsius:'))
fahrenheit = celsius * (9.0/5.0) + 32

print(f'A temperatura em Fahrenheit é {fahrenheit}°F')
""" 
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 + (F — 32.0)/9.0, sendo C a temperatura em Celsius
e F atemperatura em Fahrenheit.
""" 
fahrenheit = float(input('Informe a temperatura em graus Fahrenheit:'))
celsius = 5.0 * (fahrenheit - 32.0)/9.0

print(f'A temperatura em Celsius é {celsius}°C')
""" 
8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
fórmula de conversão é: C = K — 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin
""" 
kelvin = float(input('informe a temperatura em grau Kelvin: '))
celsius = kelvin - 273.15

print(f'A temperatura em Graus Celsius é {celsius:.2f}')

""" 
9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. À
fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
""" 
celsius = float(input('Informe a temperatura em graus Celsius:'))
kelvin = celsius + 273.15

print(f'A temperatura em Graus Kelvin é {kelvin:.2f}')

""" 
10. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em ms.
"""
kmh = float(input('Informe a sua velocidade em Km/h: '))

metros_s = kmh/3.6

print(f'Sua velocidade em Metros por segundo é {metros_s:.2f} m/s')