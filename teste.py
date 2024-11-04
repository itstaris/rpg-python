import tkinter as tk

def atualizar_texto():
    global linha_atual
    try:
        with open('introdução.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            linha_atual += 1
            if linha_atual >= len(linhas):
                linha_atual = 0
            label['text'] = linhas[linha_atual].strip()
    except FileNotFoundError:
        label['text'] = "Arquivo não encontrado!"

# Inicialização
linha_atual = 0

# Cria a janela principal
janela = tk.Tk()
janela.title("Leitor de Arquivo")

# Cria o rótulo
label = tk.Label(janela, text="")
label.pack()

# Cria o botão
botao = tk.Button(janela, text="Próxima Linha", command=atualizar_texto)
botao.pack()

# Lê a primeira linha e atualiza o label
atualizar_texto()

janela.mainloop()