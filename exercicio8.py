N = int(input("Digite um número: "))
total = 0

for numeros in range(1, N + 1):
    total += 1/numeros
    serie_harmonica = float(total)
print(f"\nSérie harmônica de {N}: {serie_harmonica:.2f}")