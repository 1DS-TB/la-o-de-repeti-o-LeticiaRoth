num = int(input("Digite um número:"))
fatorial = 1

while num > 0:
    fatorial *=  num
    num -= 1 #Vai diminuindo até chegar a um
print(f"Resultado:{fatorial}")