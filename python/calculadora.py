'''
Calculadora com while
'''

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')
    
    # Variáveis definidas fora do bloco por questão de boas práticas e para evitar transtornos.
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Ao menos um dos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###
    
    soma = num_1_float + num_2_float
    subtracao = num_1_float - num_2_float
    multiplicacao = num_1_float * num_2_float
    divisao = num_1_float / num_2_float


    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {soma}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {subtracao}')
    elif operador == '*':
        print(f'{num_1_float} x {num_2_float} = {multiplicacao}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {divisao}')
    else:
        print('Nunca deverua chegar aqui.')

    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break