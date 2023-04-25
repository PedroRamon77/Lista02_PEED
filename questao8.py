
lista = input("Digite os números da lista: ").split()

maiorValor = -100000000

for num in lista:
    if int(num) > maiorValor:
        maiorValor = int(num)

print("\nMaior valor:", maiorValor)
