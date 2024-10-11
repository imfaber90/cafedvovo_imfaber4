import streamlit as st
from SQL import CRUD  # Importando as operações CRUD do módulo SQL
from asyncio import run  # Importando a função run para lidar com chamadas assíncronasstere
from setup import setup
from random import randrange

setup('CADASTRO')
# Instanciando a classe CRUD
def insertInto():
    loteid = randrange(1,200000000)
    return loteid
    
crud = CRUD()

col1, col2 = st.columns([0.8,3])

with col1:
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NOME: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>EMAIL: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>TELEFONE: </h2>",unsafe_allow_html=True)
    st.write("#")
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CEP: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>PAíS: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>LOCALIDADE: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>BAIRRO: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>LOGRADOURO: </h2>",unsafe_allow_html=True)
    st.write("#")
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>PESSOA: </h2>",unsafe_allow_html=True)
    
with col2:
    nome = st.text_input('',key='name')
    email = st.text_input('',key='email')
    tel = st.text_input('',key='tel')
    st.write("#")
    cep = st.text_input('',key='cep')
    pais = st.text_input('',key='pais')
    local = st.text_input('',key='local')
    bairro = st.text_input('',key='bairr')
    logradouro = st.text_input('',key='logra')
    st.write("#")
    select = st.selectbox('',['Fisica','Jurídica'],key='selec1')


if select == 'Fisica':
    with col1:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CPF: </h2>",unsafe_allow_html=True)
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CARGO: </h2>",unsafe_allow_html=True)
    with col2:
        cpf = st.text_input('',key='cpf')
        select2 = st.selectbox('',['Nenhum','Funcionário','Estrangeiros'],key='selec2')
    
    if select2 == 'Funcionário':
        with col1:
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>MATRÍCULA: </h2>",unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CARGO: </h2>",unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>SALÁRIO: </h2>",unsafe_allow_html=True)
        with col2:
            matricula = st.text_input('',key='matr')
            cargo = st.text_input('',key='carg')
            salario = st.text_input('',key='sala')
            if st.button('CADASTRAR',key='cadfun'):
                pass
    
    elif select2 == 'Estrangeiros':
        with col1:
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DOCUMENTO INTERNACIONAL:</h2>",unsafe_allow_html=True)
            st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DESCRIÇÃO: </h2>",unsafe_allow_html=True)
        with col2:
            for i in range(3):
                st.write('')
            doc_inter = st.text_input('',key='cnpj')
            descricao_es = st.text_input('',key='desc')
            if st.button('CADASTRAR',key='cadest'):
                pass
    
    elif select2 == 'Nenhum':
        with col2:
            if st.button('CADASTRAR',key='cadnull'):
                pass

elif select == 'Jurídica':
    with col1:
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CNPJ: </h2>",unsafe_allow_html=True)
        st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DESCRIÇÃO: </h2>",unsafe_allow_html=True)
    with col2:
        cnpj = st.text_input('',key='cnpj')
        descricao = st.text_input('',key='desc')
        if st.button('CADASTRAR',key='cadjur'):
            pass
