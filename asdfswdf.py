from tkinter import *
janela = Tk()

dialogos = {
    "cena1": {
        1: {"personagem": "A", "texto": "Olá, mundo!", "opcoes": ["Continuar", "Sair"]}
    }
}

# ... (resto do código para criar a interface)

def exibir_dialogo(dialogo_id):
    dialogo = dialogos["cena1"][dialogo_id]
    Label.config(text=f"{dialogo['personagem']}: {dialogo['texto']}")
    # ... (criar botões para as opções)

janela.mainloop()