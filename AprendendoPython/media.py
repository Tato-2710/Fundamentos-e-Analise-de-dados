nota = []
while(len(nota) != 3):
    num = int(input("Insira sua nota: \n"))

    if num < 0 or num > 10:
        print("Nota invalida")
    else:
        nota.append(num)

soma = sum(nota)
qtd = len(nota)

media = soma/qtd

print("Sua media e: ", media)
    
def denovo():
    