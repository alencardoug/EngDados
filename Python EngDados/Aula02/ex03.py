# 3. Desenvolva um programa que multiplique dois números
# fornecidos pelo usuário e mostre o resultado.
tipo_numero01 = str
while tipo_numero01 != float:
    numero01 = input('Digite o 1o número: ')
    try:
        tipo_numero01 = type(float(numero01))
    except ValueError:
        print('Somente número.')

tipo_numero02 = str
while tipo_numero02 != float:
    numero02 = input('Digite o 2o número: ')
    try:
        tipo_numero02 = type(float(numero02))
    except ValueError:
        print('Somente número.')

produto = float(numero01) * float(numero02)
print(f'Número {numero01} multiplicado com {numero02} é {produto}.')