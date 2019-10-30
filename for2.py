#Imprimir os 10 primeiros n naturais

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numeros:
    print(i)


#Facilitando a msm idea com a fun range
print("========")
soma = 0
for i  in range(7):
    
    if (i %2 == 0):
        soma = soma + i
print(soma)