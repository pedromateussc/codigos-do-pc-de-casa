def ParesQuadrado(inteiros):
    total = 0
    for valor in inteiros:
        if (valor % 2 == 0):
            total = total + valor**2
    return total

lista1 = [2,3,5,4,3,6,7,4,3,2,2]
lista2 = [2,3,3,1,44]
lista3 = [2,2]

print(ParesQuadrado(lista1))
print(ParesQuadrado(lista2))
print(ParesQuadrado(lista3))