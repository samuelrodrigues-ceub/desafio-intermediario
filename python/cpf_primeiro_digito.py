"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '78664276153'
nove_digitos = cpf[:9]
########### Soma dos 9 primeiros dígitos
resultado = 0
regressiva = 10


for digito in nove_digitos:
    
    resultado += (int(digito) * regressiva)
    regressiva -= 1

resultado = (resultado * 10) % 11


primeiro_digito = resultado if resultado > 9 else 0

if resultado > 9:
    primeiro_digito = 0

else:
    primeiro_digito = resultado


print(f'O primeiro dígito do CPF {cpf} deve ser {primeiro_digito}.')
