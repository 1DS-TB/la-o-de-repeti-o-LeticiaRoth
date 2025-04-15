numero = int(input("Digite um número inteiro: "))
soma = 0

if numero < 0:
    print("INVALIDO")
else:
    numero +=1
    while numero > 1:
        numero -= 1
        soma += numero
print(soma)
