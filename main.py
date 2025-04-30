import streamlit as st
import importlib

# Função para o conteúdo da página selecionada

def show_pages(page_name):
    modules = {
        "Home": "home",
        "Sobre": "sobre",
        "Contato": "contato",
        "Análise de Dados": "analise_dados",
        "Projetos": "projetos",
        "Clash Royale": "clash_royale",
        "Análise de Texto": "analise_texto",
        "Dashboard": "dashboard",
    }
    
    module_name = modules.get(page_name)
    if module_name:
        module = importlib.import_module(module_name)
        #module.show_page()
        if hasattr(module, 'run'):
            module.run()
        else:
            st.write("O módulo não possui a função 'run'.")
       
    else:
        st.write("Página não encontrada.")
        
# página de navegação

page = st.sidebar.selectbox('',
    options=["Home", "Sobre", "Contato", "Análise de Dados", "Projetos", "Clash Royale", "Dashboard"],             
                  )

# Página de resumo

if page == "Home":
    st.title("Portifólio de Análise de Dados")
    st.write("Bem-vindo à página inicial!")
    st.write("Selecione uma opção no menu lateral para começar.")

else:
    show_pages(page)