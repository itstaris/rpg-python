from tkinter import *


menu = Tk()   #inicia uma janela

menu.title("O ataque sabatico") #dá nome à janela
menu.geometry("1000x600" ) 


#TITULO DO MENU
titulo = Label(menu, text="O ataque sabatico", font=("Arial", 12)) 
titulo.grid(row=0, column=1) #LEMBRAR DE CENTRALIZAR O TITULO DEPOIS

meuArquivo = open("introdução.txt", "r", encoding="utf-8")

minhasLinhasDeTexto = meuArquivo.readlines()
contador = -1

def mudanca_texto():
    bt_jogar.destroy()
    titulo.destroy()
    bt_continuar = Button(menu, text="CONTINUAR", command=mudanca_texto)
    bt_continuar.grid(row=1, column=1)
    global contador
    contador+=1
    minhasLinhasDeTexto[contador]
    texto_aparecendo = Label(menu, text=minhasLinhasDeTexto[contador], font=("Arial", 12))
    texto_aparecendo.grid(row=2, column=1)

bt_jogar = Button(menu, text="JOGAR", command=mudanca_texto)
bt_jogar.grid(row=1, column=1)

menu.mainloop()