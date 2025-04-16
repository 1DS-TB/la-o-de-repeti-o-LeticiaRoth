import random

#Jogador 1 - Héroi
hp_jogador = random.randint(200,1000) #Vai sortear entre 200  a 1000
ataque_jogador = random.randint(1,50) #Vai sortear entre 1  a 50
defesa_jogador = random.randint(1,50)


#Jogador 2 - Inimigo
hp_inimigo = random.randint(200, 1000)
ataque_inimigo = random.randint(1, 50)
defesa_inimigo = random.randint(1, 50)


while True:
    print("\n****** Bem vindo ao Jogo da DS18 ******")
    print("Escolha uma opção:")
    print("[1] Iniciar Jogo")
    print("[2] Sair")
    escolha = input("Digite a opção: ")
    
    if escolha == "1":
        print("\n=== DUELO DE HERÓIS ===")
        turno = 1
        
        while True:
            print(f"\n--- Turno {turno} ---")
            print(f"Seu HP: {hp_jogador} | Inimigo HP: {hp_inimigo}") #Mostro a vida dos jogadores
            
            #Ataques do Jogador
            opcao = input("Sua vez: [1] Atacar ou [2] Curar? ")
            if opcao == "1":
                dano_jogador = ataque_jogador - defesa_inimigo
                if dano_jogador < 0:
                    dano = 0 
                    
                hp_inimigo -= dano_jogador
                print(f"Você ataca! Inimigo perde {dano_jogador} HP.")
                
            elif opcao == "2":
                cura_jogador = random.randint(10, 50)
                hp_jogador += cura_jogador
                print(f"Você se cura em {cura_jogador} HP!") 
    
    
            #Ataques do inimigo
            inimigo_opcao = random.choices(["atacar", "curar"])[0]
            if inimigo_opcao == "atacar":
                dano_inimigo = ataque_inimigo - defesa_jogador
                
                if dano_inimigo < 0:
                    dano = 0 
                    
                hp_jogador -= dano_inimigo
                print(f"Inimigo ataca! Você perde {dano_inimigo} HP.")
            else:
                cura_inimigo = random.randint(10, 50)
                hp_inimigo += cura_inimigo
                print(f"Inimigo se cura em {cura_inimigo} HP.")
                
            if hp_jogador <= 0:
                print(f"\n Você foi DERROTADO")
                break 
            
            elif hp_inimigo <= 0:
                print(f"\n Você VENCEU, Parabéns!")
                break #Para assim que verifica o hp e vê quem ganhou
            
            turno += 1
            
    elif escolha == "2":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
    
    
    
    