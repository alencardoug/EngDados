# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes
#  fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente
#  fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio
#  como entrada.

# 6
print(' Programa que soma números float. ')
tipo_numero01 = str
while tipo_numero01 != float:
    numero01 = input('Digite o 1o número: ')
    try:
        tipo_numero01 = type(float(numero01))
    except ValueError:
        print('Somente com decimal.')

tipo_numero02 = str
while tipo_numero02 != float:
    numero02 = input('Digite o 2o número: ')
    try:
        tipo_numero02 = type(float(numero02))
    except ValueError:
        print('Somente com decimal.')

soma = float(numero01) + float(numero02)
print(f'Número {numero01} somando ao {numero02} soma {soma}.')

# 7
print(' Programa que faz a média de números float. ')
tipo_numero01 = str
while tipo_numero01 != float:
    numero01 = input('Digite o 1o número: ')
    try:
        tipo_numero01 = type(float(numero01))
    except ValueError:
        print('Somente com decimal.')

tipo_numero02 = str
while tipo_numero02 != float:
    numero02 = input('Digite o 2o número: ')
    try:
        tipo_numero02 = type(float(numero02))
    except ValueError:
        print('Somente com decimal.')

soma = float(numero01) + float(numero02)
print(f'Número {numero01} somando ao {numero02} soma {soma}.')