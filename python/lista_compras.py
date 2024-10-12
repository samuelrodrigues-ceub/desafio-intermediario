'''
Faça um lista de compras
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
'''
import os

lista = []

while True:
    entrada_inicio = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: ').lower()

    if entrada_inicio.startswith('i'):
        lista.append(input('Qual item deseja adicionar? '))

    elif entrada_inicio.startswith('a'):
        entrada_indice = input('Escolha o índice para apagar: ')

        try:
            int_entrada_indice = int(entrada_indice)
            del lista[int_entrada_indice]
            
        except:
            print('Não foi possível excluir o item do índice indicado.\n')
            continue

    elif entrada_inicio.startswith('l'):
        for indice, item in enumerate(lista):
            print(indice, item)
        continue

    else:
        print('Selecione uma opção válida\n')
        continue

    os.system('cls')