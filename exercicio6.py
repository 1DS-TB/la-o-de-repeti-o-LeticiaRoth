<<<<<<< HEAD
num = int(input("\nDigite um número:"))

if num >= 0: # Verificar se ele é positivo e declarar variáveis
    soma = 0
    i = 1

    while i <= num: #Laço para somar os números de 1 até NUM
        soma += i
        i += 1

    print(f"A soma de 1 a {num} é: {soma}")

else:
    print("INVALIDO")
=======
numero = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

a, b = 0, 1 #Inicia os dois primeiros termos

i = 0

print("Sequência de Fibonacci:")
while i < numero:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
>>>>>>> f2747d953f3aa011d969c39c12d3beaa7cecdd31
