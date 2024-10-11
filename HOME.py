import streamlit as st
import base64
import matplotlib.pyplot as plt
from SQL import CRUD
from asyncio import run
from localizer import localize

#pip install streamlit
#pip install matplotlib
#pip install databases
#pip install aiosqlite


crud = CRUD()

st.set_page_config(layout='wide')

st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

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

st.image('2-slide-1726411855687-7712896024-19169b5e89af9e644ebf72a4fe14f5c91726411850-1920-1920.webp')

st.sidebar.write('')
st.sidebar.image('Coffee-cup-icon-on-transparent-background-PNG-removebg-preview.png')

col1, col2, col3 = st.columns([1,1,1])


with col1:
    st.write('[PLACEHOLDER]')

    #labels = localize.alpha('produtos','nome_produto')
    #sizes = localize.number('produtos','preco')
    #fig, ax = plt.subplots()
    #wedges = ax.pie(sizes, labels=None, autopct=None, startangle=90)
    #legend_labels = [f'{label}: R${size}' for label, size in zip(labels, sizes)]
    #ax.legend(wedges[0], legend_labels, title="Produtos", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    #st.pyplot(fig=fig)

with col2:
    st.image('xicara-de-cafe.png')

with col3:
    st.write('[PLACEHOLDER]')

    #labels1 = localize.number('financeiro','financeiro_id')
    #sizes1 = localize.number('financeiro','valor')
    
    # Create a figure and axis with a specific style
    #fig1, ax = plt.subplots(figsize=(8, 5))  # Set figure size for better visibility

    # Create a bar chart with improved aesthetics
    #bars = ax.bar(labels1, sizes1, color='skyblue', edgecolor='white', linewidth=0.7)

    # Add data labels on top of the bars
    #for bar in bars:
        #yval = bar.get_height()
        #ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

    # Set x and y limits and ticks
    #ax.set_xlim(0, 8)
    #ax.set_xticks(range(1, 9))  # Set ticks from 1 to 8
    #ax.set_ylim(0, max(sizes1) + 1)  # Dynamically set y limit based on data
    #ax.set_yticks(range(0, int(max(sizes1) + 1), 1))  # Adjust as necessary

    # Add labels and title
    #ax.set_xlabel('Financeiro ID', fontsize=12)
    #ax.set_ylabel('Valor', fontsize=12)
    #ax.set_title('Bar Chart of Financeiro', fontsize=14)

    # Improve grid visibility
    #ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the plot in Streamlit
    #st.pyplot(fig=fig1)