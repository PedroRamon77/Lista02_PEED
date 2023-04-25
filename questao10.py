
lista = input("Digite os números da lista: ").split()

soma=0

for i in lista:
    soma += int(i)

media = soma / len(lista)

print("\nA média é: ",media)