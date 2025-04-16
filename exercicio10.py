lista_kaprekar = [] 

intervalo_inicio = int(input("Digite o começo da sequência que deseja verificar: "))
intervalo_fim = int(input("Digite o fim da sequência que deseja verificar: "))

for numero in range(intervalo_inicio, intervalo_fim + 1):
    verificacao = numero ** 2
    verificacao_str = str(verificacao)
    numero_digitos = len(str(numero))

    # Separando a parte direita e esquerda
    parte_direita = verificacao_str[-n:]
    parte_esquerda = verificacao_str[:-n] if len(verificacao_str) > numero_digitos else '0'

    esquerda = int(parte_esquerda)
    direita = int(parte_direita)
    

    soma_partes = esquerda + direita
    if soma_partes == numero:
        lista_kaprekar.append(numero)


if lista_kaprekar:
    print(f"\nNúmeros de Kaprekar no intervalo: {lista_kaprekar}")
else:
    print("\nNão há números de Kaprekar no intervalo.")
