
lista = input("Digite os números da lista: ").split()

for i in range(len(lista)):
    lista[i]=int(lista[i])
for i in lista:
    lista.sort(reverse=True)

print(" Ordem Decrescente")
print("",lista)