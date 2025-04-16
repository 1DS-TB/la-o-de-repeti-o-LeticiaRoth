num = int(input("Digite um número: "))
divisores = 0

if num <= 1:
    print("OK")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        print("OK")
    else:
        print("INVALIDO")
