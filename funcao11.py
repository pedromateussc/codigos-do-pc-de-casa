def OcorrenciaDeLetra(palavra, letra):
    total = 0
    for a in palavra:
        if a == letra:
            total = total + 1

    return total 
palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

ocorrencia = OcorrenciaDeLetra(palavra, letra)

print("A letra", letra, "possui", ocorrencia, "ocorrencias na palavra", palavra)
