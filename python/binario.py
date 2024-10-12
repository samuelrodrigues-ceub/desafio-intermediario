# Obejtivo: tranformar número de decimal para binário
numero = input('Insira um número inteiro para ser convertido em binário: ')
int_numero = 0

try:
    int_numero = int(numero)
except:
    print('Número inválido.')


numero_binario = ''
resultante = int_numero

while resultante != 0:
    if resultante % 2 == 0:
        numero_binario += '0'

    elif resultante % 2 ==1:
        numero_binario += '1'

    else:
        print('Um erro inesperado ocorreu.')

    resultante //= 2

print(f'O número {int_numero} em binário é igual a {numero_binario[::-1]}.')