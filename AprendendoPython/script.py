
print("Seja bem vindo a minha indicadora de pares ou impares")
num = int(input("Insira um numero: "))

while (num != 0):
    if num%2 == 0:
        print("Seu numero e par, uhull!\n")
    else:
        print("Seu numero e impar, aaaah\n")
    
    print("Se deseja sair, insira o numero 0\n")
    num = int(input("Insira outro numero: "))  

