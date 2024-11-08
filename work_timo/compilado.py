from tkinter import *


menu = Tk()   #inicia uma janela

menu.title("O ataque sabatico") #dá nome à janela
menu.geometry("1000x600" ) 


#TITULO DO MENU
titulo = Label(menu, text="O ataque sabatico", font=("Arial", 12)) 
titulo.grid(row=0, column=1) #LEMBRAR DE CENTRALIZAR O TITULO DEPOIS

meuArquivo = open("feijao.txt", "r", encoding="utf-8")

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
    # myLabel.configure(image=minhaImagem2)

btn2 = Button(menu, text = 'Continuar', command = updateText, image="")
btn2.place(x=450, y=420)

textoPrincipal = Label(menu,text="oiii",font=("Arial", 12))
textoPrincipal.place(relx=0.5, rely=0.75, anchor="center")
menu.mainloop()