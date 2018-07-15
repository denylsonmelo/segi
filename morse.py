from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def criptografar(caminho_arquivo):
    texto_criptografado = ''
    arquivo = open(caminho_arquivo, 'r', encoding='utf8')

    for linha in list(arquivo.readlines()):
        for caractere in list(remover_acentos(linha.lower())):
            for chave, valor in dicionario.items():
                if chave == caractere:
                    texto_criptografado = texto_criptografado + valor + ' '

    arquivo_criptografado = open('arquivo-criptografado', 'w', encoding='utf8')
    arquivo_criptografado.write(texto_criptografado)
    arquivo.close()
    arquivo_criptografado.close()
    return arquivo_criptografado


def decriptografar(arquivo):
    texto_decriptografado = ''
    arquivo_criptografado = open(arquivo.name, 'r', encoding='utf8')

    for linha in list(arquivo_criptografado.readlines()):
        for caractere in list(linha.split()):
            for chave, valor in dicionario.items():
                if valor == caractere:
                    texto_decriptografado = texto_decriptografado + chave

    arquivo_decriptografado = open('arquivo-decriptografado', 'w', encoding='utf8')
    arquivo_decriptografado.write(texto_decriptografado)
    arquivo_criptografado.close()
    arquivo_decriptografado.close()
    return arquivo_decriptografado


dicionario = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', ' ': '(/)', '(': '-.--.', ')': '-.--.-', '/': '-..-.', ':': '---...', ';': '-.-.-.', '-': '-....-', '\n': '.-.-'
}

decriptografar(criptografar("arquivo"))
