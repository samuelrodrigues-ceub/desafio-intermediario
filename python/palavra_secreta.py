"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    
    letra_digitada = input('Digite apenas uma letra: ')

    tentativas += 1

    if len(letra_digitada) > 1 or len(letra_digitada) == 0:
        print('Você digitou nenhuma ou mais de uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    print(palavra_formada)

############################# Final
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'VOCÊ GANHOU, PARABÉNS!!\n'\
              f'A palavra era: {palavra_secreta}\n'\
                f'Tentativas: {tentativas}')
        break