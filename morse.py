# milena  ->  .- - .- .- 
lista = ['a', 'b']
lista_morse = ['.-', '-...']

#tupla = 

dicionario = {'a': '.-',
              'b': '-...'}

palavra = "milenab"

for caractere in list(palavra):
    for chave, valor in dicionario.items():    # for name, age in list.items():  (for Python 3.x)
        if chave == caractere:
            print (valor)

#estrutura.recuperar('a')  --> '.-'
#estrutura.recuperar('.-')  --> 'a'

#print ( dicionario.values() )
#print ( dicionario.keys() )
#print( list(dicionario.values()).index('.-') )
#print ( list(dicionario.keys())[list(dicionario.values()).index('.-')]  )
#palavra = input()
