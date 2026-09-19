def denovo():
    n = int(input("Digite 1 se quer calcular suas notas\nDigite 0 se quer encerrar o programa\n"))
    if n != 1 and n != 0:
        print("Invalido!a")    
    return n


while denovo() == 1:
    nota = []
    while(len(nota) != 3):
        num = float(input("Insira sua nota: \n"))

        if num < 0 or num > 10:
            print("Nota invalida")
        else:
            nota.append(num)
            
    soma = sum(nota)
    qtd = len(nota)

    media = soma/qtd

    print("Sua media e: ", media)
    if media >= 7:
        print("Parabens, você passou de ano!")
    elif media < 7 and media > 5:
        print("Por pouco! Voce esta de recuperacao")
    else:
        print("Reprovado")
    