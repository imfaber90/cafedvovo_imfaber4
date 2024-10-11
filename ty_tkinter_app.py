import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser  # Importa a biblioteca para abrir o navegador
import re  # Importa para validar email e CPF
import time  # Importa para a pausa de 5 segundos

# Função para validar email
def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao_email, email)

# Função para validar CPF (somente números e 11 dígitos)
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) 

# Função para validar número (somente números)
def validar_numero(numero):
    return numero.isdigit()

# Função para salvar os dados
def salvar_dados():
    nome = entry_nome.get()
    rua = entry_rua.get()
    cidade = entry_cidade.get()
    email = entry_email.get()
    numero = entry_número.get()
    cpf = entry_cpf.get()

    if not (nome and rua and cidade and email and numero and cpf):
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")
        return

    if not validar_email(email):
        messagebox.showwarning("Erro", "Digite um email válido!")
        return

    if not validar_numero(numero):
        messagebox.showwarning("Erro", "O campo 'Número' deve conter apenas dígitos!")
        return

    if not validar_cpf(cpf):
        messagebox.showwarning("Erro", "O CPF deve conter exatamente 11 dígitos!")
        return

    # Se todos os campos estiverem corretos
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
    limpar_campos()

    # Abre o site da Puma
    webbrowser.open("https://br.puma.com")

    # Pausa de 5 segundos
    time.sleep(2)

    # fechar site em 3 segundos


    # Exibe mensagem de conclusão do cadastro
    messagebox.showinfo("Cadastro Concluído", "Seu cadastro foi concluído com sucesso!")

# Função para limpar os campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_rua.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_número.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)

# Função para fechar o programa
def fechar():
    janela.quit()

# Criar a janela principal
janela = tk.Tk()
janela.title("CADASTRO DE LOGIN DA PUMA SPOTS ")
janela.geometry("600x600")
janela.configure(bg="#f5f5f5")

# Carregar a imagem de fundo
imagem_fundo = Image.open("C:/Users/993197/Downloads/selenium/puma.png")  # Substitua pelo caminho da sua imagem de fundo
imagem_fundo = imagem_fundo.resize((600, 600), Image.Resampling.LANCZOS)  # Ajusta o tamanho da imagem para a janela
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

# Criar um label com a imagem de fundo
label_fundo = tk.Label(janela, image=imagem_fundo_tk)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)  # Posiciona a imagem como fundo

# Nome
label_nome = tk.Label(janela, text="Nome Completo:", font=("Arial", 12), fg="black", bg="#f5f5f5")  # Cor do texto ajustada
label_nome.grid(row=0, column=0, padx=20, pady=5)
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=20, pady=5)

# Email
label_email = tk.Label(janela, text="Email:", font=("Arial", 12), fg="black", bg="#f5f5f5")  # Cor do texto ajustada
label_email.grid(row=1, column=0, padx=20, pady=5)
entry_email = tk.Entry(janela, width=30)
entry_email.grid(row=1, column=1, padx=20, pady=5)

# Rua
label_rua = tk.Label(janela, text="Rua:", font=("Arial", 12), fg="black", bg="#f5f5f5")  # Cor do texto ajustada
label_rua.grid(row=2, column=0, padx=20, pady=5)
entry_rua = tk.Entry(janela, width=30)
entry_rua.grid(row=2, column=1, padx=20, pady=5)

# Cidade
label_cidade = tk.Label(janela, text="Cidade:", font=("Arial", 12), fg="black", bg="#f5f5f5")  # Cor do texto ajustada
label_cidade.grid(row=3, column=0, padx=20, pady=5)
entry_cidade = tk.Entry(janela, width=30)
entry_cidade.grid(row=3, column=1, padx=20, pady=5)

# Número
label_número = tk.Label(janela, text="Número:", font=("Arial", 12), fg="black", bg="#f5f5f5")  # Cor do texto ajustada
label_número.grid(row=4, column=0, padx=20, pady=5)
entry_número = tk.Entry(janela, width=30)
entry_número.grid(row=4, column=1, padx=20, pady=5)

# CPF
label_cpf = tk.Label(janela, text="CPF:", font=("Arial", 12), fg="black", bg="#f5f5f5")  # Cor do texto ajustada
label_cpf.grid(row=5, column=0, padx=20, pady=5)
entry_cpf = tk.Entry(janela, width=30)
entry_cpf.grid(row=5, column=1, padx=20, pady=5)

# Botão de salvar
botao_salvar = tk.Button(janela, text="Salvar Dados", font=("Arial", 12), bg="#007bff", fg="white", width=20, command=salvar_dados)
botao_salvar.grid(row=6, column=1, columnspan=5, pady=10)

# Botão de fechar
botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 12), bg="#dc3545", fg="white", width=20, command=fechar)
botao_fechar.grid(row=7, column=1, columnspan=5, pady=10)

# Carregar a imagem do logo da Puma (se desejar)
imagem_puma = Image.open("C:/Users/993197/Downloads/selenium/puma.png")  # Substitua pelo caminho da sua imagem do logo
imagem_puma = imagem_puma.resize((200, 100), Image.Resampling.LANCZOS)

# Iniciar o loop principal
janela.mainloop()
