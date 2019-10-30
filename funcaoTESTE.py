#funcaoTESTE


def g(x, y) :
    return 20 * x + y ** 3

x = (int) (input("Digite um valor: "))
y = (int) (input("Digite um valor: "))

resultado = g(x, y)

print(resultado)

##fuçao2 v1

def g(x, y) :
    if (x < 0):
        x = 1
    
    return 20 * x + y ** 3

x = (int) (input("Digite um valor: "))
y = (int) (input("Digite um valor: "))

resultado = g(x, y)

print(resultado)