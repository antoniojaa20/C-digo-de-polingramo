frase = input('Digite uma frase: ')
fraseInv = frase[::-1]
if frase == fraseInv:
    print('A frase é um palindromo')
elif frase != fraseInv:
    print('A frase não é um palindromo')