print(" == Horas trabalhadas == ")

horas_trab = (float) (input("Horas de trabalho: "))
valor_da_hora = (float) (input("Digite o valor da hora trabalhada: "))
desconto = (float) (input("Desconto no imposto de renda: "))

salario = horas_trab * valor_da_hora
salario_liquido =  salario - (salario * (desconto/100))

print("Seu salario liquido eh de: ", salario_liquido)