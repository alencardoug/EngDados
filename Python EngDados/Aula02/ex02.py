# 2. Crie um programa que receba um número do usuário e calcule
# o resto da divisão desse número por 5.
tipo_numero01 = str
while tipo_numero01 != int:
    numero01 = input('Digite o número do usuario: ')
    try:
        tipo_numero01 = type(int(numero01))
    except ValueError:
        print('Somente número inteiro.')
numero01 = int(numero01)
resto = numero01 % 5
print(resto)