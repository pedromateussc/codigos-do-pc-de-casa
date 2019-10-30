# Escreva uma função que recebe uma lista com o
# preço de 10 produtos e que exibe os preços dos
# produtos reajustados em 15%
# Teste o funcionamento da funcao no final do codigo
def reajustar(lista) :
    for item in lista :
        reajuste = item + item * 0.15
        print(reajuste)


produtos = [100.0, 50, 45, 35, 4050, 230.0, 250, 200, 1200, 600]

reajustar(produtos)
