def preencher_zeros_esquerda(string, tamanho):
    return string.zfill(tamanho) 

def decimal_para_binario(numero):
    resto = ''  
    while (numero >= 1) :
        resto += str(numero%2)
        numero //= 2

    resto = resto[::-1]
    resto = preencher_zeros_esquerda(resto, tamanho_byte)
    return resto

def binario_para_decimal(binario):
    binario = binario[::-1]

    multiplo_2 = 0
    soma = 0
    for caractere in list(binario):
        soma += int(caractere) * 2 ** multiplo_2 
        multiplo_2 += 1

    return soma

decimal = 125
tamanho_byte = 8

print(binario_para_decimal(decimal_para_binario(decimal)))