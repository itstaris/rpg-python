from tkinter import *
import time

menu = Tk()
menu.geometry("1000x600")
tempo_de_espera = 20
txt = Label(menu,text=str(f'{tempo_de_espera}'))
txt.place(x=100,y=100)


def tempo():
    global tempo_de_espera
    while tempo_de_espera >= 1:
        tempo_de_espera -= 1
        time.sleep(1)
        txt.configure(text=f'{tempo_de_espera}')
        menu.update_idletasks()
    return




bt_oi = Button(menu,text="oi",command=tempo)
bt_oi.place(x=200,y=200)
menu.mainloop()