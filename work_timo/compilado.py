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
  if contador==0:
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])

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
  if contador==17:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    segundaEscolha()
  if contador==18:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    
  if contador==19:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==20:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    
  if contador==21:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==22:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    
  if contador==23:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==24:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==25:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==26:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    bt_continuar.place_forget()
    bt_comprar_curso.place(x=350, y=520)
    bt_treta.place(x=750,y=520)
  if contador==27:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])

  if contador==28:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==29:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==30:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==31:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==32:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==33:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    bt_continuar.place_forget()
    bt_comer_milho.place(x=350,y=520)
    bt_recusar_milho.place(x=750,y=520)
  if contador==34:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==35:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==36:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==37:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==38:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==39:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==40:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==41:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==42:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    bt_continuar.place_forget()
    bt_charada_errado1.place(x=500,y=400)
    bt_charada_errado2.place(x=700,y=400)
    bt_charada_certa.place(x=500,y=500)
    bt_recorrer_a_violencia.place(x=700,y=500)
  if contador==43:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==44:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==45:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==46:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==47:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==48:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==49:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==50:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==51:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==52:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==53:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==54:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==55:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==56:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==57:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==58:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  
  if contador==59:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==60:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==61:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    terceiraEscolha()
  if contador==62:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==63:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==64:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==65:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==66:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==67:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    contador += 10
  if contador==68:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==69:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==70:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==71:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==72:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==73:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==74:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==75:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==76:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==77:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==78:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==79:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==80:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    

#Primeiras opções
def primeiraEscolha():
  bt_continuar.place_forget()
  bt_dormir.place(x=350, y=520)
  bt_ir_ao_show.place(x=750,y=520)

def dormir():
  textoPrincipal.configure(text='Mesmo sendo uma oportunidade única, sua personalidade vagabunda e preguiçosa fala mais alta e você volta a dormir.')
  bt_perdeu.place(x=450, y=420)
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

def irNoShow():
  textoPrincipal.configure(text='Não posso perder esse show!! Quem seria otário de perder a chance de ver o Raffa em carne e osso dando um espetáculo ao vivo!!???')
  bt_continuar.place(x=450, y=420)
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

#Segunda opções
def segundaEscolha():
  bt_continuar.place_forget()
  bt_planice_verde.place(x=350, y=520)
  bt_plantacao_milho.place(x=750,y=520)

def planiceVerde():
  textoPrincipal.configure(text=f'PLANÍCIE ABERTA E VERDE')
  bt_continuar.place(x=450, y=420)
  bt_planice_verde.place_forget()
  bt_plantacao_milho.place_forget()

def plantacaoMilho():
  global contador
  textoPrincipal.configure(text=f'CAMPO DE PLANTAÇÃO DE MILHO')
  bt_continuar.place(x=450, y=420)
  bt_planice_verde.place_forget()
  bt_plantacao_milho.place_forget()
  contador += 10
def comerMilho():
  bt_recusar_milho.place_forget()
  bt_comer_milho.place_forget()
  bt_continuar.place(x=450, y=420)
  textoPrincipal.configure(text=f'Você e Ana aceitam e Jullin fica muito feliz. Vocês comem um milho. Dois, três, quatro… Vocês se entopem de milho o suficiente para perderem as contas. Jullin realmente faz um milho delícia.')
def recusarMilho():
  bt_recusar_milho.place_forget()
  bt_comer_milho.place_forget()
  bt_continuar.place(x=450, y=420)
  textoPrincipal.configure(text=f'Você não tem tempo para perder com um caipira aleatório e recusa seu delicioso milho. Parabéns, você chateou um caipira triste!')

#Ponte opçoes
def errado():
  textoPrincipal.configure(text=f'Jânovisk: Não não não. Completamente errado.')
  bt_continuar.place(x=450, y=420)
  bt_charada_errado1.place_forget()
  bt_charada_errado2.place_forget()
  bt_charada_certa.place_forget()
  bt_recorrer_a_violencia.place_forget()
def recorrerAviolencia():
  textoPrincipal.configure(text=f'Você sabe que a violência nunca é a resposta, ela é a pergunta. E a resposta é sim. Em um pulo, você tenta atacar o grande goblin. Porém, com apenas uma mão, Jânovisk te segura pelo pescoço e o quebra sem qualquer esforço. Parabéns, você morreu nas mãos de um goblin preguiçoso!')
  global contador
  bt_perdeu.place(x=450, y=420)
  bt_charada_errado1.place_forget()
  bt_charada_errado2.place_forget()
  bt_charada_certa.place_forget()
  bt_recorrer_a_violencia.place_forget()
  contador += 7
def acertou():  
  global contador
  textoPrincipal.configure(text=f'Jânovisk: É isso, acertou. Podem seguir seu caminho. Se sobreviverem…')
  bt_continuar.place(x=450, y=420)
  bt_charada_errado1.place_forget()
  bt_charada_errado2.place_forget()
  bt_charada_certa.place_forget()
  bt_recorrer_a_violencia.place_forget()
  contador += 7

def comprar_curso():
  global contador
  bt_treta.place_forget()
  bt_comprar_curso.place_forget()
  textoPrincipal.configure(text=f'Wodak te convence e você gasta todo seu dinheiro comprando o curso. Sua lábia e persuasão são tão eficientes que te fizeram esquecer que não tem ovelhas. Parabéns, você comprou um curso inútil! [Curso inútil e pobreza adquiridos!]')
  bt_continuar.place(x=450, y=420)
  contador += 7
  
#Sistema de luta
def tretando():
    bt_chute.place(x=250,y=450)
    bt_soco.place(x=750,y=450)
    bt_comprar_curso.place_forget()
    bt_treta.place_forget()
    bt_continuar.place_forget()
    textoPrincipal.configure(text=f'Wodak esta na sua frente o que você faz?')  
    
def status_da_luta():
    global life, life_enemy
    if life > 0 and life_enemy <= 0:
        # print("Você ganhou!")
        textoPrincipal.configure(text=f'Você ganhou!')
        bt_chute.place_forget()
        bt_soco.place_forget()
        bt_continuar.place(x=450, y=420)
        contador == 29
    elif life <= 0:
        textoPrincipal.configure(text=f'Você perdeu!')
        bt_perdeu.place(x=800, y=100)
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
    
#terceira opçao
def terceiraEscolha():
  bt_continuar.place_forget()
  bt_therezoca.place(x=350, y=520)
  bt_romania.place(x=750, y=520)

def therezoca():
  bt_continuar.place(x=450, y=420)
  bt_therezoca.place_forget()
  bt_romania.place_forget()

def romania():
  global contador
  contador += 6
  textoPrincipal.configure(text='LABIRINTO DE ROMANIA')
  bt_continuar.place(x=450, y=420)
  bt_therezoca.place_forget()
  bt_romania.place_forget()

#Botoes do sistema de luta
bt_soco=Button(menu,text="soco", command=socar)
bt_chute=Button(menu,text="chute", command=chutar)
bt_treta=Button(menu,text="treta", command=tretando)


#Botoes de escolhas
bt_dormir = Button(menu, text='Voltar a dormir',command=dormir)
bt_ir_ao_show = Button(menu,text='Ir ao show',command= irNoShow)
bt_planice_verde = Button(menu,text=f'Planices verdes',command=planiceVerde)
bt_plantacao_milho = Button(menu,text=f'Plantação de milho',command=plantacaoMilho)
bt_therezoca = Button(menu,text='Ruínas de Therezoca',command=therezoca)
bt_romania = Button(menu,text='Labirinto de Romania',command=romania)

#Botoes de subescolha
bt_comprar_curso = Button(menu,text='Comprar curso',command=comprar_curso)
bt_comer_milho = Button(menu,text=f'Comer milho',command=comerMilho)
bt_recusar_milho = Button(menu,text=f'Recusar milho',command=recusarMilho)
bt_charada_errado1 = Button(menu,text="Março",command=errado)
bt_charada_errado2 = Button(menu,text="Julho",command=errado)
bt_charada_certa = Button(menu,text=f'Mary',command=acertou)
bt_recorrer_a_violencia = Button(menu,text=f'Atacar janovisk',command=recorrerAviolencia)


#Botao principal
bt_continuar = Button(menu, text = 'Continuar', command = updateText, image="")
bt_continuar.place(x=450, y=420)
bt_perdeu = Button(menu,text=f'Perdeu',command=menu.quit)


textoPrincipal = Label(menu,text="INTRODUÇÃO",font=("Arial", 12),wraplength=300,justify="left")
textoPrincipal.place(relx=0.5, rely=0.35, anchor="center")
menu.mainloop()