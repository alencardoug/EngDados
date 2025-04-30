# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
tipo_numero01 = str
while tipo_numero01 != int:
    numero01 = input('Digite o 1o número: ')
    try:
        tipo_numero01 = type(int(numero01))
    except ValueError:
        print('Somente número.')

quadrado = int(numero01)**2
print(f'Número {numero01} ao quadrado é {quadrado}.')