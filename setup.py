import base64
import streamlit as st

def setup(titulo):
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

    # Converta a imagem local para Base64
    img_log_base64 = get_base64_of_bin_file('logo.png')

    st.markdown(
            f"""
            <style>
                [data-testid="stSidebarNav"] {{
                    background-image: url("data:image/png;base64,{img_log_base64}");
                    background-repeat: no-repeat;
                    padding-top: 250px;
                    background-position: 10px -32px;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )

    st.sidebar.write('')
    st.sidebar.image('Coffee-cup-icon-on-transparent-background-PNG-removebg-preview.png')
        # Título da aplicação
    st.markdown(f"<h1 style= 'color:Black;'>{titulo}</h1>",unsafe_allow_html=True)
