
lista = input("Digite os números da lista: ").split()

maiorde10 = []

for i in lista:
    if int(i) > 10:
        maiorde10.append(i)

if maiorde10:
    print("Os números maiores de 10 são:")
    for i in maiorde10:
        print("",i)

else:
    print("Não há numeros maiores de 10")