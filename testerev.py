print(" == Valor do imposto ==")
salario = (float) (input("Qual o valor do seu salario? "))

if salario <= 1556.61:
    print("Nao ha imposto")
elif salario >= 1556.62 and salario <= 2347.85:
    imposto = 0.075* salario
    print("Valor de imposto retido: R${:.2f} ".format (imposto), "reais") 
elif salario >= 2347.86 and salario <= 3130.51:
    imposto = 0.15 * salario
    print("Valor de imposto redito: R${:.2f}".format (imposto), "reais")
elif salario >= 3130.52 and salario <= 3911.63:
    imposto = 0.225 * salario
    print("Valor de imposto redito: R${:.2f}".format (imposto), "reais")  
else:
    imposto = 0.275 * salario
    print("Valor de imposto retido: R${:.2f}".format (imposto), "reais")           