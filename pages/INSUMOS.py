import streamlit as st
from SQL import CRUD  # Importando as operações CRUD do módulo SQL
from asyncio import run  # Importando a função run para lidar com chamadas assíncronasstere
from setup import setup
from random import randrange

setup('INSUMOS')
# Instanciando a classe CRUD
def insertInto():
    loteid = randrange(1,200000000)
    
crud = CRUD()

col1, col2 = st.columns([1.6,4])

with col1:
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CÓDIGO DO INSUMO: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NOME DO PRODUTO: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DESCRIÇÃO: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>QUANTIDADE: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>PREÇO: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'> ID DO FORNECEDOR: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>ID DO PEDIDO: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>ID DO LOTE: </h2>",unsafe_allow_html=True)
    
with col2:
    codigo = st.text_input('',key='codigo do produto')
    nome = st.text_input('',key='nome do produto')
    descricao = st.text_input('',key='descricao')
    quantidade = st.text_input('',key='quantidade')
    preco = st.text_input('',key='preco')
    fornecedor = st.text_input('',key='fornecedor')
    pedido = st.text_input('',key='pedido')
    lote = st.text_input('',key='lote')
    st.write("#")
