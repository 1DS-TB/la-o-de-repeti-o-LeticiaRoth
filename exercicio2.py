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
