""" 
11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
emkm/h e M em m/s.
"""
metros_s = float(input('Informe sua velociade dem metros por segundo(m/s): '))

kms = metros_s*3.6

print(f'Sua velocidade em Km/h é {kms}')

"""
12. Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1,61 * M, sendo K a distância em quilômetros e 1 em milhas.
"""
milhas = float(input('Informe a distância em milhas para converção: '))

km = 1.61 * milhas
print(f'A distância em KM é igual a {km:.2f}')

"""
13. Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é: M = £,, sendo K a distância em quilômetros e M em milhas.
"""
km = float(input('Informe a distância em quilômetros para converção: '))

milhas = km/1.61

print(f'A sua distância em Milhas é {milhas:.2f}')

"""
14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R=G*7/180, sendo G o ângulo em graus e R em radianos e x = 3.14.
"""
angulo = float(input('Informe o angulo em graus para apresentar em radianos: '))

radianos = angulo * (3.14/180)

print(f'O Angulo de {angulo} é igual a {radianos:.2f} Radianos')

"""
15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R*+180/7, sendo G o ângulo em graus e R em radianos e x = 3.14.
"""
radianos = float(input('Informe o ângulo em Radianos para apresentar em graus: '))

graus = radianos * (180/3.14)

print(f'{radianos} Radianos é igual a {graus:.2f} graus')

"""
16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P +2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""
polegadas = float(input('Informe o comprimento em polegadas para conversão em centímetros: '))

centimetros = polegadas * 2.54

print(f'{polegadas} Polegadas, é igual a {centimetros} centímetos')

"""
17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
AA fórmula de conversão é: P = &,, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""
centimetros = float(input('Informe o comprimento em centímetros para converter em polegadas: '))

polegadas = centimetros/2.45

print(f'{centimetros} centimetros em polegadas são {polegadas:.2f}')

"""
18. Leia um valor de volume em metros cúbicos nº e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 + M, sendo L o volume em litros e M o volume em
metros cúbicos.
"""
metros_3 = float(input('Informe o volume em Metros Cúbicos(m³) para transformar em Litors: '))

litros = 1000 * metros_3

print(f'{metros_3}m³ são exatameto {litros}L')

"""
19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m*. A
fórmula de conversão é: M = 7é5, sendo L o volume em litros e M/ o volume em metros
cúbicos.
"""
litros = float(input('Informe o volume em litros para converter em M³: '))

metros_3 = litros/1000

print(f'{litros}litros é igual a {metros_3}M³')

"""
20. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é: L = 7£;, sendo K a massa em quilogramas e L a massa em libras.
.
"""
kg = float(input('Informe a massa em Kilograms para converter em libras: '))

libra = kg/0.45

print(f'{kg}Kg correspondem a {libra:.2f} Libras')