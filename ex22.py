print("==== Maquina de operacoes ===")
operando1 = (float) (input("Digite o primeiro operando: "))
operando2 = (float) (input("Digite o segundo operando: "))
operacao = input("Qual a operacao vc quer fazer?")
if (operacao == "+"):
    print(operando1 + operando2) 
elif (operacao == "-"):
    print(operando1 - operando2)
elif (operacao == "*"):
    print(operando1*operando2)    
elif (operacao == "/"):
    if( operando2 == 0):
        print("Nao eh possivel efetuar divisao por zero")
    else:
        print(operando1/operando2)
else:
    print("Operacao invalida")                   
