import streamlit as st
from controller import ItemController # A View conversa APENAS com o Controller
from time import sleep # Função "sleep" para adicionar um delay ao adicionar um Item.

# Configuração da Página
st.set_page_config(
    page_title="Gerenciameto de Itens",
    page_icon="📝"
)
st.title("📝 Gerenciamento de Itens")

# Formulário para Adicionar um Item
st.header("Adicionar Novo Item")
with st.form(key="new_item_form", clear_on_submit=True):
    description = st.text_input("Descrição do Item")
    amount = st.number_input("Quantidade do Item", 0, 128, 1, 1)
    submit_button = st.form_submit_button("Adicionar")

    # Ação de adicionar um Item sendo delegada pelo Controller.
    if submit_button:
        ItemController.add_new_item(description, amount)
        sleep(1.5) # Delay antes de atualizar a página.
        st.rerun() # Atualizar a página.

st.divider()

# Catálogo de Itens
st.header("Catálogo de Itens")

all_itens = ItemController.get_all_items()

if not all_itens:
    st.info("Não há Itens Cadastrados.")
else:
    for item in all_itens:
        st.subheader(f"Item {item.id}")
        st.markdown(f"**Descrição**: {item.description}")
        st.markdown(f"**Quantidade**: {item.amount}")
        st.divider()
