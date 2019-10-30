# Escreva uma função que receba uma lista de inteiros
# de 16 posições e que retorne a soma dos quadrados
# dos números  ímpares contidos na lista
# Teste o funcionamento da funcao no final do codigo

def quadradoDosPares(inteiros) :
    total = 0
    for valor in inteiros: 
        if (valor % 2 == 0) :
            total = total + valor ** 2
    
    return total

numeros1 = [10, 20, 30, 40]
numeros2 = [3, 4, 7]
numeros3 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7]

total1 = quadradoDosPares(numeros1)
total2 = quadradoDosPares(numeros2)
print(quadradoDosPares(numeros3))

print(total1)
print(total2)