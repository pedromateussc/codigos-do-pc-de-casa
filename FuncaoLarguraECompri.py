def terreno(largura, comprimento):
    a = largura * comprimento
    print("A área de um terreno", largura, "x", comprimento, " é", a,"m²")

print("== Largura de um terreno ==")

largura = (float)(input("Digite a largura: "))
comprimento = (float)(input("Digite o comprimento: "))
terreno(largura, comprimento)