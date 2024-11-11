from tkinter import *
import time

# l_nome_variável = leitura das linhas do txt
# bt = botão

menu = Tk()   #inicia uma janela

menu.title("O ataque sabatico") #dá nome à janela
menu.geometry("1000x600" ) 

#TITULO DO MENU
titulo = Label(menu, text="O ataque sabatico", font=("Arial", 12)) 
titulo.grid(row=0, column=1) #LEMBRAR DE CENTRALIZAR O TITULO DEPOIS


meuArquivo = open("introducao.txt", "r", encoding="utf-8")
minhasLinhasDeTexto = meuArquivo.readlines()

#INTRODUÇÃO
contador = 0
def uptxt_introducao():

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

meuArquivo = open("ir_no_show.txt", "r", encoding="utf-8")
l_ir_no_show = meuArquivo.readlines()

def uptxt_ir_no_show():
  global contador
  contador+=1

  if contador==1:
    textoPrincipal.configure(text=l_ir_no_show[contador])
  
  if contador==2:
  
    textoPrincipal.configure(text=l_ir_no_show[contador])

def primeiraEscolha():
  bt_continuar.place_forget()
  bt_dormir.place(x=350, y=520)
  bt_ir_ao_show.place(x=750,y=520)


def dormir():
  textoPrincipal.configure(text='Mesmo sendo uma oportunidade única, sua personalidade vagabunda e preguiçosa fala mais alta e você volta a dormir.')
  bt_dormir.place_forget()
  #criar botao de iniciar game
  bt_ir_ao_show.place_forget()
  contador = 0

def irNoShow():
  textoPrincipal.configure(text='Não posso perder esse show!! Quem seria otário de perder a chance de ver o Raffa em carne e osso dando um espetáculo ao vivo!!???')
  bt_continuar.place(x=450, y=420, command= uptxt_ir_no_show)
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()
  contador = 0

bt_dormir = Button(menu, text='Voltar a dormir',command=dormir)
bt_ir_ao_show = Button(menu,text='Ir ao show',command= uptxt_ir_no_show)

bt_continuar = Button(menu, text = 'Continuar', command = uptxt_introducao, image="")
bt_continuar.place(x=450, y=420)
# btn2.grid(row=1,column=3)


textoPrincipal = Label(menu,text="oiii",font=("Arial", 12),wraplength=300)
textoPrincipal.place(relx=0.5, rely=0.35, anchor="center")
menu.mainloop()