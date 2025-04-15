numero = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

a, b = 0, 1 #Inicia os dois primeiros termos

i = 0

print("Sequência de Fibonacci:")
while i < numero:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
>>>>>>> f2747d953f3aa011d969c39c12d3beaa7cecdd31
