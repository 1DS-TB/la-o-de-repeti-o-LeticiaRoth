num = int(input("Digite um número inteiro: "))
som = 0

if num < 0:
    print("INVALIDO")
else:
    num +=1
    while num > 1:
        num -= 1
        som+= num
print(som)
