numero = int(input("Digite um número: "))
divisor = 0

for i in range(1, numero +1):
    if numero % i == 0 and numero >= 1:
        divisor +=1

if divisor == 2:
    print(f"{numero} é primo")
elif divisor <1:
    print("INVALIDO")
else:
    print(f"{numero}não é primo")
