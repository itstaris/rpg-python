from tkinter import *
import random

Menu = Tk()
Menu.geometry("1000x600" )
textP = Label(Menu,text="oi")
textP.place(x=500,y=200)

probabilidade_soco = 0.8
probabilidade_chute = 0.5
life = 10
life_enemy = 10

def tretando():
    bt_chute.place(x=250,y=450)
    bt_soco.place(x=750,y=450)
    bt_treta.place_forget()  
    
def status_da_luta():
    global life, life_enemy
    if life > 0 and life_enemy <= 0:
        # print("Você ganhou!")
        textP.configure(text=f'Você ganhou!')
    elif life <= 0:
        textP.configure(text=f'Você perdeu!')
    # else:
    #     textP.configure(text=f'O jogo continua')
    Vidas = Label(Menu,text=f'Sua vida:{life} Vida do inimigo:{life_enemy}')
    Vidas.place(x=100,y=100)
    
def socar():
    global life, life_enemy
    if random.random() < probabilidade_soco:
        dano = random.randint(1,4)
        life_enemy -= dano
        # print(f'voce acertou o inimigo e deu {dano} de dano')
        textP.configure(text=f'Vc deu um soco no inimigo e deu {dano} de dano, porem ele revida e da 2 de dano')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()
    else:
        # print("Vc errouuu")
        textP.configure(text=f'Você errouu e ainda levou um tapa do Wodak -2 de vida')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()  
    
def chutar():
    global life, life_enemy
    if random.random() < probabilidade_chute:
        dano = random.randint(2,8)
        life_enemy -= dano
        # print(f'voce acertou o inimigo e deu {dano} de dano')
        textP.configure(text=f'Vc deu um chute no inimigo e deu {dano} de dano, porém ele revida e da 2 de dano')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()
    else:
        # print("Vc errouuu")
        textP.configure(text=f'Você errouu e ainda levou um tapa do Wodak -2 de vida')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()  
    


bt_soco=Button(Menu,text="soco", command=socar)
bt_chute=Button(Menu,text="chute", command=chutar)
bt_treta=Button(Menu,text="treta", command=tretando)
bt_treta.place(x=400,y=400)
Menu.mainloop()