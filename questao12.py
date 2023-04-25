
lista = input("Digite os números da lista: ").split()

numImpar = []

for i in lista:
    if int(i) % 2 != 0 :
        numImpar.append(i)

if numImpar:
    print("Os números impares são: ")
    for i in numImpar:
        print("",i)

else:
        print("Não há numeros ímpares")
