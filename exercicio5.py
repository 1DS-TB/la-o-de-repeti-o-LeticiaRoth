numero = int(input("Digite um número: "))
print("OK")  # Primeira linha esperada sempre

if numero <= 1:
    print("OK")  # Segunda linha esperada para número <= 1
else:
    divisor = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisor += 1

    if divisor == 2:
        print("OK")  # Número primo
    else:
        print("INVALIDO")  # Número composto
