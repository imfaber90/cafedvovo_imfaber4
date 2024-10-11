import sqlite3

# Função para conectar ou criar o banco de dados
def connect_db():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    # Criar a tabela se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        email TEXT,
                        telefone TEXT)''')
    conn.commit()
    conn.close()

# Função para inserir um cliente
def add_cliente(nome, email, telefone):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
    conn.commit()
    conn.close()

# Função para visualizar os clientes
def view_clientes():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Função para atualizar um cliente
def update_cliente(id, nome, email, telefone):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?", (nome, email, telefone, id))
    conn.commit()
    conn.close()

# Função para excluir um cliente
def delete_cliente(id):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
