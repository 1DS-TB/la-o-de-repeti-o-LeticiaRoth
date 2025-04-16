numero = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a, b = 0, 1 #Inicia os dois primeiros termos
i = 0
fibonacci = []

if numero < 1:
    print("INVALIDO")
else:
    while i < numero:
        fibonacci.append(a)
        a, b = b, a + b
        i += 1
    print(fibonacci)




