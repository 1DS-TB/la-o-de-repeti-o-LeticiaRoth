lista_perfeitos = []

for numero in range(1, 10001):
    soma = 0

    for contador in range(1, numero):
        if numero % contador == 0:
            soma += contador

    if soma == numero:
        lista_perfeitos.append(numero)
        
print(lista_perfeitos)
