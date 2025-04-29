# Inteiros
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
tipo_numero01 = str
while tipo_numero01 != int:
    numero01 = input('Digite o 1o número: ')
    try:
        tipo_numero01 = type(int(numero01))
    except ValueError:
        print('Somente número inteiro.')

tipo_numero02 = str
while tipo_numero02 != int:
    numero02 = input('Digite o 2o número: ')
    try:
        tipo_numero02 = type(int(numero02))
    except ValueError:
        print('Somente número inteiro.')

soma = int(numero01) + int(numero02)
print(f'Número {numero01} somando com {numero02} é {soma}.')