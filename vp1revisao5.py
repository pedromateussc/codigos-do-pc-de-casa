print(" == Diferenca pelo maior e menor ==")
n1 = (float) (input("Qual o primeiro valor?  "))
n2 = (float) (input("Qual o segundo valor?  "))

if n1> n2: 
    maior = n1 - n2
    print("Diferenca entre eles: ", maior)
elif n2>n1:
    maior = n2 - n1
    print("Diferenca entre eles: ", maior)
else:
    print("Operacao invalida")
            
