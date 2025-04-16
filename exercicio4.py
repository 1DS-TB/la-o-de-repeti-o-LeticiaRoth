num = int(input("Digite um número:"))

if num < 0:
    print("Números primos não podem ser negativos")
else:
    fatorial = 1
    while num > 0:
        fatorial *= num
        num -= 1
    print(f"Resultado: {fatorial}")
