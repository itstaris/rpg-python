from tkinter import *


menu = Tk()   #inicia uma janela

menu.title("O ataque sabatico") #dá nome à janela
menu.geometry("1000x600" ) 

#TITULO DO MENU
titulo = Label(menu, text="O ataque sabatico", font=("Arial", 12)) 
titulo.grid(row=0, column=1) #LEMBRAR DE CENTRALIZAR O TITULO DEPOIS


#BOTAO INICIAR
def txt1():
    botao_inicio.destroy()
    titulo.destroy()
    texto = Label(menu, text="Você dorme tranquilamente em sua cama confortável, até que seu sono é interrompido por barulhos na janela.")
    texto.grid(row=0, column=1)
    def mudanca_texto():
        texto.config(text= "É um pombo correio cutucando o vidro, você abre a janela e pega uma carta que ele te trouxe.")

    botao_continuar = Button(menu, text="CONTINUAR", command=mudanca_texto)
    botao_continuar.grid(row=1, column=1)

botao_inicio = Button(menu, text="JOGAR", command=txt1)
botao_inicio.grid(row=1, column=1)

menu.mainloop()