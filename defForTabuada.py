def multiplicacao(n):
    for i in range(11):
        print(n, "x", i, "=", (n*i))
def soma(n):
    for i in range (11):
        print(n, "+", i, "=", (n+i))
def subtracao(n):
    for i in range(20):
        print(i+n, "-", n, "=", (i))
def divisao(n):
     for i in range(10):
         print(n*(1+i), "/", n, "=", (i+1))
def tabuada(n):
    print("Tabuada do", n)
    print("==========")
    soma(n)
    print("==========")
    subtracao(n)
    print("==========")
    multiplicacao(n)
    print("==========")
    divisao(n)
valor = (int) (input("Digite um numero inteiro pra tabuada: "))
tabuada(valor)    
