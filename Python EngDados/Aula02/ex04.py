# 4. Faça um programa que peça dois números inteiros 
# e imprima a divisão inteira do primeiro pelo segundo.

tipo_numero01 = str
while tipo_numero01 != int:
    numero01 = input('Digite o 1o número: ')
    try:
        tipo_numero01 = type(int(numero01))
    except ValueError:
        print('Somente número.')

tipo_numero02 = str
while tipo_numero02 != int:
    numero02 = input('Digite o 2o número: ')
    try:
        tipo_numero02 = type(int(numero02))
    except ValueError:
        print('Somente número.')

divisao_inteira = int(numero01) // int(numero02)
print(f'Número {numero01} divido pelo {numero02} tem inteiro {divisao_inteira}.')