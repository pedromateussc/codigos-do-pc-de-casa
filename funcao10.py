def saudar(nome):
    print("Olá, " , nome)

def FuncaoLoka(x, y):
    x = 2 * y + x **(1/2)
    y = 3 * x + 2 * y

    return(x, y)

resultado = FuncaoLoka(4, 2)

print("x = ", resultado[0])
print("y = ", resultado [1])

saudar("pedrooo")
