from tkinter import *
import time
import random

#configuraçoes da janela
menu = Tk()   
menu.title("O ataque sabatico") 
menu.geometry("1000x600" ) 

#TITULO DO MENU
titulo = Label(menu, text="O ataque sabatico", font=("Arial", 12)) 
titulo.grid(row=0, column=1) 

#Leitor do arquivo de texto
meuArquivo = open("introducao.txt", "r", encoding="utf-8")
minhasLinhasDeTexto = meuArquivo.readlines()

#Variaveis
contador = 0
probabilidade_soco = 0.8
probabilidade_chute = 0.5
life = 10
life_enemy = 10
#Texto principal com o sisstema
def updateText():

  global contador
  contador+=1

  if contador==1:
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  
  if contador==2:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    
  if contador==3:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==4:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==5:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    primeiraEscolha()
  if contador==6:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==7:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==8:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==9:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==10:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])

  if contador==11:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==12:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==13:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==14:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==15:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==16:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  # if contador==17:
  
  #   textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  # if contador==18:
  
  #   textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  # if contador==19:
  
  #   textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  # if contador==20:
  
  #   textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    # myLabel.configure(image=minhaImagem2)

def primeiraEscolha():
  bt_continuar.place_forget()
  bt_dormir.place(x=350, y=520)
  bt_ir_ao_show.place(x=750,y=520)

def dormir():
  textoPrincipal.configure(text='Mesmo sendo uma oportunidade única, sua personalidade vagabunda e preguiçosa fala mais alta e você volta a dormir.')
  bt_continuar.place(x=450, y=420)
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

def irNoShow():
  textoPrincipal.configure(text='Não posso perder esse show!! Quem seria otário de perder a chance de ver o Raffa em carne e osso dando um espetáculo ao vivo!!???')
  bt_continuar.place(x=450, y=420)
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

#Sistema de luta
def tretando():
    bt_chute.place(x=250,y=450)
    bt_soco.place(x=750,y=450)
    bt_treta.place_forget()
    bt_continuar.place_forget()
    textoPrincipal.configure(text=f'Wodak esta na sua frente o que você faz?')  
    
def status_da_luta():
    global life, life_enemy
    if life > 0 and life_enemy <= 0:
        # print("Você ganhou!")
        textoPrincipal.configure(text=f'Você ganhou!')
    elif life <= 0:
        textoPrincipal.configure(text=f'Você perdeu!')
    # else:
    #     textP.configure(text=f'O jogo continua')
    Vidas = Label(menu,text=f'Sua vida:{life} Vida do inimigo:{life_enemy}')
    Vidas.place(x=100,y=100)
    
def socar():
    global life, life_enemy
    if random.random() < probabilidade_soco:
        dano = random.randint(1,4)
        life_enemy -= dano
        # print(f'voce acertou o inimigo e deu {dano} de dano')
        textoPrincipal.configure(text=f'Vc deu um soco no inimigo e deu {dano} de dano, porem ele revida e da 2 de dano')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()
    else:
        # print("Vc errouuu")
        textoPrincipal.configure(text=f'Você errouu e ainda levou um tapa do Wodak -2 de vida')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()  
    
def chutar():
    global life, life_enemy
    if random.random() < probabilidade_chute:
        dano = random.randint(2,8)
        life_enemy -= dano
        # print(f'voce acertou o inimigo e deu {dano} de dano')
        textoPrincipal.configure(text=f'Vc deu um chute no inimigo e deu {dano} de dano, porém ele revida e da 2 de dano')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()
    else:
        # print("Vc errouuu")
        textoPrincipal.configure(text=f'Você errouu e ainda levou um tapa do Wodak -2 de vida')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()  
    
#Botoes do sistema de luta
bt_soco=Button(menu,text="soco", command=socar)
bt_chute=Button(menu,text="chute", command=chutar)
bt_treta=Button(menu,text="treta", command=tretando)
bt_treta.place(x=400,y=400)

#Botoes de escolhas
bt_dormir = Button(menu, text='Voltar a dormir',command=dormir)
bt_ir_ao_show = Button(menu,text='Ir ao show',command= irNoShow)


#Botao principal
bt_continuar = Button(menu, text = 'Continuar', command = updateText, image="")
bt_continuar.place(x=450, y=420)

textoPrincipal = Label(menu,text="oiii",font=("Arial", 12),wraplength=300)
textoPrincipal.place(relx=0.5, rely=0.35, anchor="center")
menu.mainloop()