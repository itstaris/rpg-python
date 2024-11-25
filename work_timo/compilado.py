from tkinter import *
import time
import random

#configuraçoes da janela
menu = Tk()   
menu.title("O ATAQUE SABÁTICO") 
menu.geometry("1000x600") 
menu.configure(bg="#322A2D")
menu.iconbitmap("sabba.ico")

#CORES
#marrom claro #322A2D
#marrom escuro #272022
#amarelo #EADBA7

caixa_texto = Canvas(menu, width=525, height=200, bg="#EADBA7", highlightthickness=0)

#Leitor do arquivo de texto
meuArquivo = open("introducao.txt", "r", encoding="utf-8")
minhasLinhasDeTexto = meuArquivo.readlines()

#Variáveis
contador = 0
probabilidade_soco = 0.8
probabilidade_chute = 0.65
life = 10
life_enemy = 10
vida_do_boss = 99
tempo_de_espera = 150

Vidas = Label(menu,text=f'Sua vida: {life} \nVida do inimigo: {life_enemy}', font=("Georgia", 12),wraplength=500,justify="left", fg="#272022", bg="#EADBA7")
Vidas2 = Label(menu,text=f'Sua vida: {life} \nVida do inimigo: {vida_do_boss}',font=("Georgia", 12),wraplength=500,justify="left", fg="#272022", bg="#EADBA7")

#Texto principal com o sistema
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
    bt_comprar_curso.place(relx=0.33, rely=0.7, anchor="center")
    bt_treta.place(relx=0.66, rely=0.7, anchor="center")
  if contador==27:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])

  if contador==28:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==29:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    menu.update_idletasks()
  if contador==30:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==31:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==32:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==33:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    bt_continuar.place_forget()
    bt_comer_milho.place(relx=0.33, rely=0.7, anchor="center")
    bt_recusar_milho.place(relx=0.66, rely=0.7, anchor="center")
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
    bt_charada_errado1.place(relx=0.33, rely=0.7, anchor="center")
    bt_charada_errado2.place(relx=0.66, rely=0.7, anchor="center")
    bt_charada_certa.place(relx=0.33, rely=0.85, anchor="center")
    bt_recorrer_a_violencia.place(relx=0.66, rely=0.85, anchor="center")
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
    contador += 10
  if contador==67:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
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
    esperando()
    txt_de_espera.place(relx=0.5, rely=0.3, anchor="center")
    bt_continuar.place_forget()
  if contador==75:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])

  if contador==76:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    txt_de_espera.place_forget()
  if contador==77:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==78:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==79:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==80:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==81:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==82:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==83:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==84:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==85:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==86:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==87:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==88:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
  if contador==89:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    luta_final()

  if contador==90:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])

  if contador==91:
  
    textoPrincipal.configure(text=minhasLinhasDeTexto[contador])
    bt_continuar.place_forget()
    bt_perdeu.place(relx=0.5, rely=0.7, anchor="center")

#Primeiras opções
def primeiraEscolha():
  bt_continuar.place_forget()
  bt_dormir.place(relx=0.33, rely=0.7, anchor="center")
  bt_ir_ao_show.place(relx=0.66, rely=0.7, anchor="center")

def dormir():
  textoPrincipal.configure(text='Mesmo sendo uma oportunidade única, sua personalidade vagabunda e preguiçosa fala mais alto e você volta a dormir.')
  bt_perdeu.place(relx=0.5, rely=0.7, anchor="center")
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

def irNoShow():
  textoPrincipal.configure(text='Não posso perder esse show!! Quem seria otário de perder a chance de ver o Raffa em carne e osso dando um espetáculo ao vivo!!???')
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

#Segunda opções
def segundaEscolha():
  bt_continuar.place_forget()
  bt_planice_verde.place(relx=0.33, rely=0.7, anchor="center")
  bt_plantacao_milho.place(relx=0.66, rely=0.7, anchor="center")

def planiceVerde():
  textoPrincipal.configure(text=f'[PLANÍCIE ABERTA E VERDE]')
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  bt_planice_verde.place_forget()
  bt_plantacao_milho.place_forget()

def plantacaoMilho():
  global contador
  textoPrincipal.configure(text=f'[CAMPO DE PLANTAÇÃO DE MILHO]')
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  bt_planice_verde.place_forget()
  bt_plantacao_milho.place_forget()
  contador += 10
def comerMilho():
  bt_recusar_milho.place_forget()
  bt_comer_milho.place_forget()
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  textoPrincipal.configure(text=f'Você e Ana aceitam e Jullin fica muito feliz. Vocês comem um milho. Dois, três, quatro… Vocês se entopem de milho o suficiente para perderem as contas. Jullin realmente faz um milho delícia.')
def recusarMilho():
  bt_recusar_milho.place_forget()
  bt_comer_milho.place_forget()
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  textoPrincipal.configure(text=f'Você não tem tempo para perder com um caipira aleatório e recusa seu delicioso milho. Parabéns, você chateou um pobre caipira simpático!')
#Ponte opçoes
def errado():
  textoPrincipal.configure(text=f'Jânovisk: Não não não. Completamente errado.')
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  bt_charada_errado1.place_forget()
  bt_charada_errado2.place_forget()
  bt_charada_certa.place_forget()
  bt_recorrer_a_violencia.place_forget()
def recorrerAviolencia():
  textoPrincipal.configure(text=f'Você sabe que a violência nunca é a resposta, ela é a pergunta. E a resposta é sim. Em um pulo, você tenta atacar o grande goblin. Porém, com apenas uma mão, Jânovisk te segura pelo pescoço e o quebra sem qualquer esforço. Parabéns, você morreu nas mãos de um goblin preguiçoso!')
  global contador
  bt_perdeu.place(relx=0.5, rely=0.7, anchor="center")
  bt_charada_errado1.place_forget()
  bt_charada_errado2.place_forget()
  bt_charada_certa.place_forget()
  bt_recorrer_a_violencia.place_forget()
  contador += 7
def acertou():  
  global contador
  textoPrincipal.configure(text=f'Jânovisk: É isso, acertou. Podem seguir seu caminho. Se sobreviverem…')
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
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
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  contador += 7
  
#Sistema de luta
def tretando():
    bt_chute.place(relx=0.33, rely=0.7, anchor="center")
    bt_soco.place(relx=0.66, rely=0.7, anchor="center")
    bt_comprar_curso.place_forget()
    bt_treta.place_forget()
    bt_continuar.place_forget()
    textoPrincipal.configure(text=f'Você está quase sendo convencido, até que se lembra que nem ao menos tem ovelhas. Mesmo recusando educadamente, Wodak se enfurece e parte para cima. O que você faz?')  
    Vidas.place(relx=0.15, rely=0.22, anchor="center")

def status_da_luta():
    global life, life_enemy, contador
    Vidas.configure(text=f'Sua vida: {life} \nVida do inimigo: {life_enemy}')
    if life > 0 and life_enemy <= 0:
        # print("Você ganhou!")
        textoPrincipal.configure(text=f'Você dá um sarrafo em Wodak e ganha a luta! Felizmente não caiu na lábia de um desconhecido...')
        bt_chute.place_forget()
        bt_soco.place_forget()
        Vidas.place_forget()
        
        bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
        menu.update_idletasks()
        Vidas.place_forget()
        contador+=7
    elif life <= 0:
        bt_chute.place_forget()
        bt_soco.place_forget()
        textoPrincipal.configure(text=f'Você e Ana apanharam feio de Wodak. Quem diria que perderiam para um cara desses.')
        bt_perdeu.place(relx=0.5, rely=0.7, anchor="center")
    # else:
    #     textP.configure(text=f'O jogo continua')
    

    
def socar():
    global life, life_enemy
    if random.random() < probabilidade_soco:
        dano = random.randint(1,4)
        life_enemy -= dano
        # print(f'voce acertou o inimigo e deu {dano} de dano')
        textoPrincipal.configure(text=f'Você dá um soco no inimigo e o tira {dano} de vida, porém ele revida e dá 2 de dano!')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()
    else:
        # print("Vc errouuu")
        textoPrincipal.configure(text=f'Você erra e ainda leva um tapa do Wodak, perdendo 2 de vida!')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()  
    
def chutar():
    global life, life_enemy
    if random.random() < probabilidade_chute:
        dano = random.randint(2,8)
        life_enemy -= dano
        # print(f'voce acertou o inimigo e deu {dano} de dano')
        textoPrincipal.configure(text=f'Você dá um chute no inimigo e o tira {dano} de vida, porém ele revida e dá 2 de dano!')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()
    else:
        # print("Vc errouuu")
        textoPrincipal.configure(text=f'Você erra e ainda leva um tapa do Wodak, perdendo 2 de vida!')
        life -= 2 
        # print(f'Wodak te atacou e vc perdeu 2 de vida')
        status_da_luta()

#luta com o chefao final
def luta_final():
  global life,vida_do_boss
  life=10
  bt_luta_final.place_forget()
  bt_continuar.place_forget()
  bt_rasteira2.place(relx=0.33, rely=0.7, anchor="center")
  bt_peteleco2.place(relx=0.66, rely=0.7, anchor="center")
  # bt_caixa_dagua.place(x=500,y=500)
  textoPrincipal.configure(text=f'O grande demônio está a sua frente, o que você faz?')
  Vidas.place_forget()
  Vidas2.place(relx=0.15, rely=0.22, anchor="center")


def status_do_boss():
  global life, vida_do_boss 
  Vidas2.configure(text=f'Sua vida:{life} \nVida do inimigo:{vida_do_boss}')

  if life > 0 and vida_do_boss <= 0:
    bt_rasteira2.place_forget()
    bt_peteleco2.place_forget() 
    esquecer()
    Vidas2.place_forget()
    bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
    #textoPrincipal.configure(text=f'PARABÉNS, VOCÊ DERROTOU O GRANDE DEMÔNIO!!')
  elif life <= 0:
    bt_rasteira2.place_forget()
    bt_peteleco2.place_forget()
    textoPrincipal.configure(text=f'Você perdeu!')
    bt_caixa_dagua.after(1, esquecer)
    bt_perdeu.place(relx=0.5, rely=0.7, anchor="center")
  if life < 3:
    bt_caixa_dagua.place(relx=0.5, rely=0.85, anchor="center")

def rasteira2():
    global life, vida_do_boss
    if random.random() < probabilidade_chute:
        dano2 = random.randint(2,8)
        vida_do_boss -= dano2
        textoPrincipal.configure(text=f'Você dá uma rasteira em Sabba e a faz perder {dano2} de vida, porém ela cospe em você e dá 3 de dano!')
        life -= 3 
        status_do_boss()
    else:
        textoPrincipal.configure(text=f'Você erra e ainda leva uma catarrada de fogo, perdendo 3 de vida!')
        life -= 3
        status_do_boss()

def peteleco2():
    global life, vida_do_boss
    if random.random() < probabilidade_soco:
        dano2 = random.randint(1,4)
        vida_do_boss -= dano2
        textoPrincipal.configure(text=f'Você dá um peteleco em Sabba e a faz perder {dano2} de vida, porém ela cospe em você e dá 3 de dano!')
        life -= 3 
        status_do_boss()
    else:
        textoPrincipal.configure(text=f'Você erra e ainda levou uma catarrada de fogo, perdendo 3 de vida!')
        life -= 3
        status_do_boss()    

def caixa_dagua():
  global life,vida_do_boss
  vida_do_boss -= 100
  textoPrincipal.configure(text=f"Você pega a super caixa d'agua e arremessa no grande demônio, enfim a derrotando!!!")
  bt_caixa_dagua.after(1, esquecer)
  status_do_boss()

def esquecer():
  bt_caixa_dagua.place_forget()

#terceira opçao
def terceiraEscolha():
  bt_continuar.place_forget()
  bt_therezoca.place(relx=0.33, rely=0.7, anchor="center")
  bt_romania.place(relx=0.66, rely=0.7, anchor="center")

def therezoca():
  global contador
  textoPrincipal.configure(text=f'[RUÍNAS DE THEREZOCA]')
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  bt_therezoca.place_forget()
  bt_romania.place_forget()

def romania():
  global contador
  contador += 6
  textoPrincipal.configure(text='[LABIRINTO DE ROMANIA]')
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  bt_therezoca.place_forget()
  bt_romania.place_forget()

def esperando():
  global tempo_de_espera
  tempo_de_espera=tempo_de_espera-1
  
  if tempo_de_espera<0:
    return
  textoPrincipal.config(text=str(tempo_de_espera))
  textoPrincipal.after(1000,esperando)
  if tempo_de_espera == 0:
    bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
    txt_de_espera.place_forget()


#Botoes do sistema de luta
bt_soco=Button(menu,text="Soco", command=socar, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_chute=Button(menu,text="Chute", command=chutar, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_treta=Button(menu,text="Recusar", command=tretando, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)


#Botoes de escolhas
bt_dormir = Button(menu, text='Voltar a dormir',command=dormir, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_ir_ao_show = Button(menu,text='Ir ao show',command= irNoShow, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_planice_verde = Button(menu,text=f'Planícies verdes',command=planiceVerde, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_plantacao_milho = Button(menu,text=f'Plantação de milho',command=plantacaoMilho, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_therezoca = Button(menu,text='Ruínas de Therezoca',command=therezoca, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_romania = Button(menu,text='Labirinto de Romania',command=romania, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)

#Botoes de subescolha
bt_comprar_curso = Button(menu,text='Comprar curso',command=comprar_curso, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_comer_milho = Button(menu,text=f'Comer milho',command=comerMilho, font=("Cambria", 14), bg="#272022", fg="white",  width=25, pady=6)
bt_recusar_milho = Button(menu,text=f'Recusar milho',command=recusarMilho, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_charada_errado1 = Button(menu,text="Março",command=errado, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_charada_errado2 = Button(menu,text="Julho",command=errado, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_charada_certa = Button(menu,text=f'Mary',command=acertou, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_recorrer_a_violencia = Button(menu,text=f'Atacar janôvisk',command=recorrerAviolencia, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)


#Botao principal
bt_continuar = Button(menu, text = 'Continuar', command = updateText, image="", font=("Cambria", 14), bg="#272022", fg="white", padx=30, pady=5)
#bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
bt_perdeu = Button(menu,text=f'Fim',command=menu.quit, font=("Cambria", 14), bg="#272022", fg="white", padx=30, pady=5)

textoPrincipal = Label(menu,text="[O INÍCIO]",font=("Georgia", 16),wraplength=500,justify="center", fg="#272022", bg="#EADBA7")

#Start
def comecar():
  bt_continuar.place(relx=0.5, rely=0.7, anchor="center")
  bt_start.place_forget()
  titulo.place_forget()
  textoPrincipal.place(relx=0.5, rely=0.35, anchor="center")
  caixa_texto.place(relx=0.5, rely=0.35, anchor="center")

bt_start = Button(menu, text = 'Jogar', command = comecar, image="", font=("Cambria", 20), bg="#272022", fg="white", padx=40, pady=10)
bt_start.place(relx=0.5, rely=0.7, anchor="center")

titulo = Label(menu, text="O ATAQUE SABÁTICO",font=("Georgia", 50), wraplength=500,justify="center", fg="#EADBA7", bg="#322A2D")
titulo.place(relx=0.5, rely=0.45, anchor="center")

creditos = Label(menu, text="Desenvolvido por:\nTimo\nTamires", font=("Georgia", 10), wraplength=500,justify="left", fg="#EADBA7", bg="#322A2D" )
creditos.place(relx=0.1, rely=0.9, anchor="center")

#espera no labirinto
txt_de_espera = Label(menu,text="Você sente na pele a demora para chegar no fim do labirinto...",font=("Georgia", 12),wraplength=500,justify="center", fg="#272022", bg="#EADBA7")

#luta
bt_luta_final = Button(menu,text="Treta final",command=luta_final)
bt_rasteira2 = Button(menu,text="Rasteira",command=rasteira2, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_peteleco2 = Button(menu,text="Peteleco",command=peteleco2, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)
bt_caixa_dagua = Button(menu,text="SUPER CAIXA D'ÁGUA",command=caixa_dagua, font=("Cambria", 14), bg="#272022", fg="white", width=25, pady=6)

'''
def skip():
  global contador
  contador += 88
bt_skip= Button(menu,text="skip",command=skip)
bt_skip.place(x=900,y=100)
'''

menu.mainloop()