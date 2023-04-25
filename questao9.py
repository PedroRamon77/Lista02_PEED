
lista = input("Digite os números da lista: ").split()

menorValor = 10000000

for num in lista:
    if int(num) < menorValor:
        menorValor = int(num)

print("\nMenor valor:", menorValor)
