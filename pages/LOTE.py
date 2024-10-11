import streamlit as st
from setup import setup
from random import randrange

setup('CADASTRAR LOTE')

col1, col2 = st.columns([1,2])

with col1:
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DATA DE VALIDADE: </h2>",unsafe_allow_html=True)
    st.markdown(f"<h2 style= 'color:Orange;padding-top: 25px;'>DATA DE FABRICAÇÃO: </h2>",unsafe_allow_html=True)
    st.write("#")

    
with col2:
    dataval = st.text_input('',key='vali')
    datfab = st.text_input('',key='fabr')
    st.write("#")
    if st.button('GERAR LOTE',key='lote'):
        loteid = randrange(1,200000000)
        st.write(f'ID GERADO: {loteid}')






