import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser  # Importa a biblioteca para abrir o navegador
import re  # Importa para validar email e CPF

# Função para validar email
def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao_email, email)

# Função para validar CPF (somente números e 11 dígitos)
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

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
    webbrowser.open("https://www.magazineluiza.com.br")  # Abre o site da Magazine Luiza após o cadastro

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
janela.title("Cadastro na Magazine Luiza")
janela.geometry("600x600")
janela.configure(bg="#f5f5f5")

# Carregar a imagem de fundo (logotipo da Magazine Luiza)
imagem_fundo = Image.open("C:/Users/993197/Downloads/selenium/magazine_luiza_logo.png") 
