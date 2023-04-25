
frase = input("Digite a frase: ").split()

maiorPalavra = ""

for palavra in frase:
    if len(palavra) > len(maiorPalavra):
        maiorPalavra = palavra

print("A palavra mais longa é: ",maiorPalavra)