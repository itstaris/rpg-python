from tkinter import *

janela = Tk()

janela.title("O ataque sabatico")

janela.geometry("400x400" )
def next_scene():
    # Lógica para mudar para a próxima cena
    label.config(text="abacate")

# Texto do diálogo
label = Label(janela, text="oioioioioi", font=("Arial", 12))
label.grid(row=0, column=1)

# Botão de próxima ação
button = Button(janela, text="Continuar", command=next_scene)
button.grid(row=1, column=1)

janela.mainloop()