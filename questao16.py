
lista = input("Digite os números da lista: ").split()

soma = 0

for i in lista:
    if int(i) % 2 == 0:
        soma += int(i)

print("Soma dos números pares são: ",soma)
