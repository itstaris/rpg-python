import tkinter as tk
import subprocess

def reproduzir_video():
    caminho_video = "raffa_o_bardo"
    comando_player = ["wmplayer.exe", caminho_video]
    subprocess.call(comando_player)

# Criar a janela Tkinter
root = tk.Tk()

# Criar um botão para iniciar a reprodução
botao = tk.Button(root, text="Reproduzir Vídeo", command=reproduzir_video)
botao.pack()

root.mainloop()