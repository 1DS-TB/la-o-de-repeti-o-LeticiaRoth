num = int(input("Digite um número: "))

if num < 1:
    print("INVALIDO")
else:
    for ponto in range(1, num + 1):  #Começa em 1 e vai adicionando mais um até o número
        linhas = "*" * ponto #Falo que a linha é multiplicado peloa quantidade de ponto
        print(linhas)



        

