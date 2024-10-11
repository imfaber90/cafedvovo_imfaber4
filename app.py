import streamlit as st
import base64
from database import add_cliente, view_clientes, update_cliente, delete_cliente, connect_db # type: ignore

# Conectar ao banco de dados
connect_db()


# Função para converter imagem em base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Converta a imagem local para Base64
img_base64 = get_base64_of_bin_file('Cafedvovo01.png')

# Defina a imagem de fundo usando o base64
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        color: black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir imagem
#st.image('Cafedvovo01.png', caption='Minha Imagem', use_column_width=True)

# Título do aplicativo
st.title('Cadastro de Clientes')

# Função para exibir a lista de clientes
def listar_clientes():
    clientes = view_clientes()
    for cliente in clientes:
        st.write(f'ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}')

# Criação dos botões para as ações do CRUD
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('Cadastrar Cliente', key='cadastrar'):
        st.session_state.acao = 'cadastrar'

with col2:
    if st.button('Listar Clientes', key='listar'):
        st.session_state.acao = 'listar'

with col3:
    if st.button('Atualizar Cliente', key='atualizar'):
        st.session_state.acao = 'atualizar'

with col4:
    if st.button('Excluir Cliente', key='excluir'):
        st.session_state.acao = 'excluir'

# Verifica a ação selecionada
if 'acao' not in st.session_state:
    st.session_state.acao = None

# CADASTRAR CLIENTE
if st.session_state.acao == 'cadastrar':
    st.subheader('Cadastrar Cliente')
    
    # Entrada de dados
    nome = st.text_input('Nome')
    email = st.text_input('Email')
    telefone = st.text_input('Telefone')

    if st.button('Adicionar Cliente'):
        add_cliente(nome, email, telefone)
        st.success(f'Cliente {nome} adicionado com sucesso!')

# LISTAR CLIENTES
elif st.session_state.acao == 'listar':
    st.subheader('Lista de Clientes')
    listar_clientes()

# ATUALIZAR CLIENTE
elif st.session_state.acao == 'atualizar':
    st.subheader('Atualizar Cliente')
    listar_clientes()

    id = st.number_input('ID do cliente para atualizar', min_value=1)
    nome = st.text_input('Novo Nome')
    email = st.text_input('Novo Email')
    telefone = st.text_input('Novo Telefone')

    if st.button('Atualizar Cliente'):
        update_cliente(id, nome, email, telefone)
        st.success(f'Cliente {id} atualizado com sucesso!')

# EXCLUIR CLIENTE
elif st.session_state.acao == 'excluir':
    st.subheader('Excluir Cliente')
    listar_clientes()

    id = st.number_input('ID do cliente para excluir', min_value=1)

    if st.button('Excluir Cliente'):
        delete_cliente(id)
        st.success(f'Cliente {id} excluído com sucesso!')
