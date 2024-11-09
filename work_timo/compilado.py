from tkinter import *
import time

menu = Tk()   #inicia uma janela

menu.title("O ataque sabatico") #dá nome à janela
menu.geometry("1000x600" ) 


#TITULO DO MENU
titulo = Label(menu, text="O ataque sabatico", font=("Arial", 12)) 
titulo.grid(row=0, column=1) #LEMBRAR DE CENTRALIZAR O TITULO DEPOIS

meuArquivo = open("introducao.txt", "r", encoding="utf-8")

minhasLinhasDeTexto = meuArquivo.readlines()

#teste
contador = 0
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
  btn2.place_forget()
  bt_dormir.place(x=350, y=520)
  bt_ir_ao_show.place(x=750,y=520)


def dormir():
  textoPrincipal.configure(text='Mesmo sendo uma oportunidade única, sua personalidade vagabunda e preguiçosa fala mais alta e você volta a dormir.')
  btn2.place(x=450, y=420)
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

def irNoShow():
  textoPrincipal.configure(text='Não posso perder esse show!! Quem seria otário de perder a chance de ver o Raffa em carne e osso dando um espetáculo ao vivo!!???')
  btn2.place(x=450, y=420)
  bt_dormir.place_forget()
  bt_ir_ao_show.place_forget()

bt_dormir = Button(menu, text='Voltar a dormir',command=dormir)
bt_ir_ao_show = Button(menu,text='Ir ao show',command= irNoShow)

btn2 = Button(menu, text = 'Continuar', command = updateText, image="")
btn2.place(x=450, y=420)
# btn2.grid(row=1,column=3)


textoPrincipal = Label(menu,text="oiii",font=("Arial", 12),wraplength=300)
textoPrincipal.place(relx=0.5, rely=0.35, anchor="center")
menu.mainloop()