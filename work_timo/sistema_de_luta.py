import random

life = 10
life_enemy = 10

probabilidade_soco = 0.8
probabilidade_chute = 0.5

while life > 0 and life_enemy > 0:
    print(f'vida atual:{life}')
    print(f'vida do inimigo:{life_enemy}')
    choice = input("Escolha o seu golpe soco ou chute: ").lower().strip()

    if choice == "soco":
        if random.random() < probabilidade_soco:
            dano = random.randint(1,4)
            life_enemy -= dano
            print(f'voce acertou o inimigo e deu {dano} de dano')
        else:
            print("Vc errouuu")
    elif choice == "chute":
        if random.random() < probabilidade_chute:
            dano = random.randint(2,8)
            life_enemy -= dano
            print(f'voce acertou o inimigo e deu {dano} de dano')
        else:
            print("voce errou o golpe")

    if life_enemy > 0:
        life -= 2 
        print(f'Wodak te atacou e vc perdeu 2 de vida')

if life <= 0:
    print("vc perdeu")
else:
    print("vc ganhou")

        