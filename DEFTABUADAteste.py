def divisao(n):
     for i in range(10):
         print(n*(1+i), "/", n, "=", (i+1))
def tabuada(n):
    print("Tabuada do", n)
    print("==========")
    divisao(n)
valor = (int) (input("Digite um numero inteiro pra tabuada: "))
tabuada(valor)    