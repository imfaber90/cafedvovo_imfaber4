from databases import Database as db
/home/cafe/Documentos/Vscode Server/__pycache__import asyncio
# Inicializa a conexão com o banco de dados usando SQLite com suporte a async
database = db('sqlite+aiosqlite:///cafevovo.db')

async def criar():
    # Conecta ao banco de dados de forma assíncrona
    await database.connect()
    
    #*************************************
    # TABELA CADASTROS DE PESSOAS .
    #query = """CREATE TABLE if not exists CLIENTE (INSERIR OS CAMPOS)"""
    #await database.execute(query=query)
    #Codigo para Adicionar Foreigh Key, após o último campo iserir o codigo
    # FOREIGN KEY(idpessoa) REFERENCES CADASTROS_DE_PESSOAS(idpessoa)

    query = """CREATE TABLE if not exists CADASTROS_DE_PESSOAS (idpessoa INTEGER PRIMARY KEY, email VARCHAR(255), datadecadastro DATE, nome VARCHAR(60))"""
    await database.execute(query=query)

  

    #*************************************
    # TABELA TELEFONE . 
 
    query = """CREATE TABLE IF NOT EXISTS TELEFONE (idTelefone INTEGER PRIMARY KEY AUTOINCREMENT, idpessoa INT, telefone VARCHAR(45), FOREIGN KEY(idpessoa) REFERENCES CCADASTROS_DE_PESSOAs(idpessoa));"""  
    await database.execute(query=query)

    
    #*************************************
    # TABELA ENDERECOS .
        
    query = """CREATE TABLE if not exists ENDERECOS (idendereco INTEGER PRIMARY KEY, idpessoa INT, Logradouro VARCHAR(100), Pais VARCHAR(60), Cep INTEGER, Localidade VARCHAR(60), Bairro VARCHAR(60), FOREIGN KEY(idpessoa) REFERENCES CADASTROS_DE_PESSOAS(idpessoa));"""
    await database.execute(query=query)


    #*************************************
    # TABELA FUNCIONARIOS .
    query = """CREATE TABLE if not exists FUNCIONARIOS (idpessoa INT PRIMARY KEY, IdMatricula VARCHAR(45), Cargo VARCHAR(45), Salario VARCHAR(45), FOREIGN KEY(idpessoa) REFERENCES CADASTROS_DE_PESSOAS(idpessoa));"""
    await database.execute(query=query)
    
    
    #*************************************
    # TABELA FISICA .
    #query = """CREATE TABLE if not exists CLIENTE (INSERIR OS CAMPOS)"""
    #await database.execute(query=query) 
    query = """CREATE TABLE if not exists FISICA (idpessoa INTEGER PRIMARY KEY, CPF VARCHAR(45), nome VARCHAR(225), FOREIGN KEY(idpessoa) REFERENCES CADASTROS_DE_PESSOAS(idpessoa));"""
    await database.execute(query=query)
    
    #*************************************
    # TABELA JURIDICA .
    #query = """CREATE TABLE if not exists CLIENTE (INSERIR OS CAMPOS)"""
    #await database.execute(query=query) 

    query = """CREATE TABLE if not exists JURIDICA (idpessoa INTEGER PRIMARY KEY, Descricao VARCHAR(255), Cnpj VARCHAR(60), FOREIGN KEY(idpessoa) REFERENCES CADASTROS_DE_PESSOAS(idpessoa));"""
    await database.execute(query=query)
    
    #*************************************
    # TABELA ESTRANGEIRO .
    #query = """CREATE TABLE if not exists CLIENTE (INSERIR OS CAMPOS)"""
    #await database.execute(query=query) 
    
    query = """CREATE TABLE if not exists ESTRANGEIRO (idpessoa INTEGER PRIMARY KEY, Documento Internacional VARCHAR(60), Descricao VARCHAR(144), FOREIGN KEY(idpessoa) REFERENCES CADASTROS_DE_PESSOAS(idpessoa));"""
    await database.execute(query=query)
     
           
    #*************************************
    # TABELA Orcamento .
    #query = """CREATE TABLE if not exists CLIENTE (INSERIR OS CAMPOS)"""
    #await database.execute(query=query) 
    
    query = """CREATE TABLE IF NOT EXISTS Orcamento (idOrcamento INT PRIMARY KEY, idpessoa INT, valor_total VARCHAR(45), status_orcamento VARCHAR(45), data DATE, FOREIGN KEY(idpessoa) REFERENCES CADASTROS_DE_PESSOAS(idpessoa));"""
    await database.execute(query=query)


    #*************************************
    # TABELA Fornecedor
    #query = """CREATE TABLE if not exists CLIENTE (INSERIR OS CAMPOS)"""
    #await database.execute(query=query) 
    
    query = """CREATE TABLE IF NOT EXISTS FORNECEDOR (fornecedor_id INT PRIMARY KEY, nome_empresa VARCHAR(100), documento VARCHAR(45), endereço VARCHAR(45));"""
    await database.execute(query=query)


asyncio.run(criar())