
lista = input("Digite os números da lista: ").split()

menorde5 = []

for i in lista:
    if int(i) < 5:
        menorde5.append(i)

if menorde5:
    print("Os números menores de 5 são:")
    for i in menorde5:
        print("",i)

else:
    print("Não há numeros menores de 5")