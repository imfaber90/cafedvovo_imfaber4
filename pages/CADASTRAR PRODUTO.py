import streamlit as st
from setup import setup
from random import randrange

setup('CADASTRAR PRODUTO')

def insertInto():
    loteid = randrange(1,200000000)
    return loteid

col1, col2 = st.columns([1,2])
with col1:
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>NOME DO PRODUTO </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>CATEGORIA: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>ESTOQUE: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>ID DO LOTE: </h2>",unsafe_allow_html=True)

    
with col2:
    nomeprod = st.text_input('',key='nameprod')
    categoria = st.text_input('',key='categ')
    estoque = st.text_input('',key='estoque')
    id_lote = st.text_input('',key='IDlote')
    st.write('#')
    if st.button('CADASTRAR PRODUTO'):
        insertInto()