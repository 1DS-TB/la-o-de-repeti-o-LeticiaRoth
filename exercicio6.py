numero = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a, b = 0, 1 #Inicia os dois primeiros termos
i = 0
fibonnaci =[]

if numero < 1:
    print("INVALIDO")
else:
    while i < numero:
        a,b = b,a+b
        fibonnaci.append(a)
        i +=1
print(fibonnaci)



