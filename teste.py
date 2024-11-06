import tkinter as tk

# Função para ler o arquivo e armazenar as linhas
def carregar_linhas(introdução.txt):
    with open(introdução.txt, 'r', encoding="utf-8") as f:
        return f.readlines()

# Função para atualizar o label com a próxima linha
def proxima_linha():
    global linha_atual
    if linha_atual < len(linhas):
        label.config(text=linhas[linha_atual].strip())
        linha_atual += 1

# Carregar as linhas do arquivo
linhas = carregar_linhas('C:/Users/202310164/Desktop/projeto python/rpg-python')
linha_atual = 0

# Criar a janela principal
janela = tk.Tk()
janela.title("Leitor de Linhas")

# Criar um label para exibir a linha
label = tk.Label(janela, text=linhas[linha_atual].strip(), font=("Arial", 16))
label.pack(pady=20)

# Criar um botão para mudar a linha
botao = tk.Button(janela, text="Próxima linha", command=proxima_linha)
botao.pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()
