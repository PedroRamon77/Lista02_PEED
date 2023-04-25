
lista = input("Digite os números da lista: ").split()

produto = 1

for i in lista:
    produto *= int(i)

print("O produto dos números digitados: ",produto)