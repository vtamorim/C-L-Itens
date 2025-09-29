import streamlit as st # Importamento do Streamlit para usar o decorador "cache_data".
from model import Item
from ItemDAO import ItemDAO

class ItemController:
    """
    Classe controlodade para gerenciar as operações dos Items.
    Funciona como a conexão entre a View (app.py) com o Model (Item) e o DAO (ItemDAO.py).
    """
    
    @staticmethod
    @st.cache_data # Salva a resposta do Banco de Dados no cache para acelerar a operação de leitura.
    def get_all_items() -> list[Item]:
        """Retorna todos os Items do Banco de Dados."""
        return ItemDAO.fetch_all_items()

    @staticmethod
    def add_new_item(description: str, amount: int) -> None:
        """Recebe os dados brutos da View, cria um objeto Item e o envia para o DAO."""

        # Pequena Validação dos dados.
        description = description.strip() # Remove os espaços laterais.
        if len(description) <= 0:
            st.error("É necessário ter uma descrição do Item.")
            return
        if amount < 0:
            st.error("Quantidade do Item não pode ser menor que 0.")
            return 

        new_item = Item(description=description, amount=amount)

        ItemDAO.add_item(new_item)
        
        st.success("Item Adicionado com Sucesso!") # Mensagem de Sucesso.
        
        st.cache_data.clear()
