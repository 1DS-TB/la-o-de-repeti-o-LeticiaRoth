import random

while True:
    print("\n****** Bem vindo ao Jogo da DS18 ******")
    print("Escolha uma opção:")
    print("[1] Single Player (Você vs CPU)")
    print("[2] Multiplayer (Jogador 1 (Héroi) vs Jogador 2 (Inimigo))")
    print("[3] Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "3":
        print("Saindo do jogo, volte sempre!")
        break

    #Saúde
    hp_max = random.randint(200, 1000)
    hp1 = hp_max
    hp2 = hp_max
    
    #Ataque
    atq1 = random.randint(1, 50)
    atq2 = random.randint(1, 50)
    
    #Defesa
    def1 = random.randint(1, 50)
    def2 = random.randint(1, 50)

    força1_turno = 0
    força2_turno = 0
    
    escudo1_turno = 0
    escudo2_turno = 0
    
    raiva1_turno = 0
    raiva2_turno = 0
    
    tela_azul1_turno = 0
    tela_azul2_turno = 0
    
    buffer1 = False
    buffer2 = False
    
    loop1_infinito = False
    loop2_infinito = False
    
    cache1_usado = False
    cache2_usado = False
    
    efeito_usado1 = []
    efeito_usado2 = []

    turno = 1

    print("\n=== DUELO DE HERÓIS ===")
    print("=== JOGADOR 1 - HÉROI ===")
    print(f"HP: {hp1}  ATQ: {atq1}  DEF: {def1}")
    print("=== JOGADOR 2 - INIMIGO ===" if escolha == "2" else "=== INIMIGO ===")
    print(f"HP: {hp2}  ATQ: {atq2}  DEF: {def2}")

    while hp1 > 0 and hp2 > 0:
        print(f"\n--- TURNO {turno} ---")
        print(f"JOGADOR 1 HP: {hp1} | JOGADOR 2 HP: {hp2}")

        for jogador in [1, 2]: #Aqui escolhe o tipo de jogo
            if escolha == "1" and jogador == 2:
                tipo = "cpu"
            else:
                tipo = "player"

            if jogador == 1:
                hp, atq, df = hp1, atq1, def2
                força, escudo, raiva = força1_turno, escudo1_turno, raiva1_turno
                tela_azul= tela_azul2_turno
                buffer = buffer1
                loop = loop1_infinito
                efeitos_usados = efeito_usado1
                cache_usado = cache1_usado
            else:
                hp, atq, df = hp2, atq2, def1
                força, escudo, raiva = força2_turno, escudo2_turno, raiva2_turno
                tela_azul = tela_azul1_turno
                buffer = buffer2
                loop = loop2_infinito
                efeitos_usados = efeito_usado2
                cache_usado = cache2_usado

            if buffer:
                dano_buffer = int(hp_max * 0.05)
                hp -= dano_buffer
                print(f"Jogador {jogador} sofre {dano_buffer} de Buffer Overflow!")

            if loop:
                print(f"Jogador {jogador} perdeu a vez devido ao Loop Infinito!")
                if jogador == 1:
                    loop1_infinito = False
                    hp1 = hp
                else:
                    loop2_infinito = False
                    hp2 = hp
                continue

            if tela_azul > 0:
                df = 0
                if jogador == 1:
                    tela_azul2_turno -= 1
                else:
                    tela_azul1_turno -= 1

            if força > 0:
                atq += 10
                if jogador == 1:
                    força1_turno -= 1
                else:
                    força2_turno -= 1

            if escudo > 0:
                df += 10
                if jogador == 1:
                    escudo1_turno -= 1
                else:
                    escudo2_turno -= 1

            if raiva > 0:
                atq = int(atq * 1.5)
                if jogador == 1:
                    raiva1_turno -= 1
                else:
                    raiva2_turno -= 1
            elif raiva == -1:
                atq = int(atq * 0.75)
                if jogador == 1:
                    raiva1_turno = 0
                else:
                    raiva2_turno = 0

            if tipo == "player":
                print(f"\nJogador {jogador}, escolha sua ação:")
                print("[1] Atacar\n[2] Curar\n[3] Usar Item\n[4] Usar Efeito de Status")
                acao = input("> ")
            else:
                acao = random.choice(["1", "2"])

            if acao == "1":
                critico = random.random() < 0.1
                dano = atq - df
                dano = max(dano, 0)
                if critico:
                    dano *= 2
                    print(f"Jogador {jogador} acertou um CRÍTICO!")
                print(f"Jogador {jogador} ataca e causa {dano} de dano!")
                if jogador == 1:
                    hp2 -= dano
                else:
                    hp1 -= dano

            elif acao == "2":
                cura = random.randint(20, 50)
                hp += cura
                print(f"Jogador {jogador} se cura em {cura} HP!")
                if jogador == 1:
                    hp1 = hp
                else:
                    hp2 = hp

            elif acao == "3":
                if tipo == "cpu":
                    item = random.choice(["1", "2", "3", "4"])
                else:
                    print("[1] Poção de Força (+ATQ por 2 turnos)")
                    print("[2] Poção de Cura (+100 HP)")
                    print("[3] Poção de Escudo (+DEF por 2 turnos)")
                    print("[4] Poção de Raiva (+50% ATQ por 1 turno)")
                    item = input("Escolha um item: ")

                if item == "1":
                    print(f"Jogador {jogador} usou Poção de Força!")
                    if jogador == 1:
                        força1_turno = 2
                    else:
                        força2_turno = 2

                elif item == "2":
                    print(f"Jogador {jogador} usou Poção de Cura!")
                    hp += 100

                elif item == "3":
                    print(f"Jogador {jogador} usou Poção de Escudo!")
                    if jogador == 1:
                        escudo1_turno = 2
                    else:
                        escudo2_turno = 2

                elif item == "4":
                    print(f"Jogador {jogador} usou Poção de Raiva!")
                    if jogador == 1:
                        raiva1_turno = 1
                    else:
                        raiva2_turno = 1

                if jogador == 1:
                    hp1 = hp
                else:
                    hp2 = hp

            elif acao == "4":
                if tipo == "cpu":
                    continue  # CPU não usa efeitos
                print("Efeitos disponíveis:")
                print("[1] Buffer Overflow (5% de dano por turno)")
                print("[2] Loop Infinito (inimigo perde 1 turno)")
                print("[3] Tela Azul (DEF = 0 por 2 turnos)")
                print("[4] Cache Hit (+30% HP, se HP < 25%)")
                efeito = input("Escolha um efeito: ")

                if efeito in efeitos_usados:
                    print("Você já usou esse efeito!")
                    continue
                efeitos_usados.append(efeito)

                if efeito == "1":
                    print("Buffer Overflow ativado!")
                    if jogador == 1:
                        buffer2 = True
                    else:
                        buffer1 = True

                elif efeito == "2":
                    print("Loop Infinito ativado!")
                    if jogador == 1:
                        loop2_infinito = True
                    else:
                        loop1_infinito = True

                elif efeito == "3":
                    print("Tela Azul ativada!")
                    if jogador == 1:
                        tela_azul2_turno = 2
                    else:
                        tela_azul1_turno = 2

                elif efeito == "4":
                    if hp < hp_max * 0.25 and not cache_usado:
                        cura = int(hp_max * 0.3)
                        hp += cura
                        print(f"Cache Hit ativado! Cura de {cura} HP.")
                        if jogador == 1:
                            cache1_usado = True
                        else:
                            cache2_usado = True
                    else:
                        print("Você não pode usar Cache Hit agora!")

                if jogador == 1:
                    hp1 = hp
                else:
                    hp2 = hp

        turno += 1

    print("\n--- FIM DE JOGO - DUELO DE HÉROIS---")
    if hp1 <= 0 and hp2 <= 0:
        print("Empate!")
    elif hp1 <= 0:
        print("Jogador 2 (INIMIGO) venceu!" if escolha == "2" else "CPU venceu!")
    else:
        print("Jogador 1 (HÉROI) venceu!")
