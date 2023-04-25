
frase = input("Digite a frase: ").split()

comecaA = []

for palavra in frase:
    if palavra.startswith('a') or palavra.startswith('A'):
        comecaA.append(palavra)

if comecaA:
    print("As palavras que começam com A são:")
for i in comecaA:
    print("",i)
    
else:
    print("Não possui palavras que comecem com a letra 'a'")