import sqlite3
from model import Item

class ItemDAO:
    """Classe DAO para gerenciar e encapsular as operações relacionadas ao Banco de Dados da aplicação."""
    __db_name = "item_list.db" # Nome do arquivo do Banco de Dados.

    @classmethod
    def __get_db_connection(cls) -> sqlite3.Connection:
        """Retorna o objeto da conexão com o Banco de Dados."""
        conn = sqlite3.connect(cls.__db_name)
        conn.row_factory = sqlite3.Row # Permite acessar o Banco de Dados como um dicionário ao invés de uma tupla.
        return conn

    @classmethod
    def add_item(cls, item: Item) -> None:
        """Adiciona um objeto "Item" ao Banco de Dados."""
        conn = cls.__get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (description, amount) VALUES (?, ?)",
            (item.description, item.amount)
        )
        conn.commit()
        conn.close()

    @classmethod
    def fetch_all_items(cls) -> list[Item]:
        """Busca todos os items e retorna uma lista de objetos Item."""
        conn = cls.__get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items ORDER BY amount DESC")
        
        rows = cursor.fetchall()
        conn.close()
        
        # Transforma cada linha do resultado do banco em um objeto Item.
        return [
            Item(
                id=row['id'], 
                description=row['description'], 
                amount=row['amount']
            ) for row in rows
        ]

    # Opcional: Uma função para inicializar o DB, se necessário.
    @classmethod
    def init_db(cls) -> None:
        """Inicializa o banco de dados e cria a tabela se ela não existir."""
        conn = cls.__get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount INTEGER
        );
        """)
        conn.commit()
        conn.close()

# Se você executar este arquivo diretamente, ele inicializará o banco.
if __name__ == '__main__':
    ItemDAO.init_db()
    print("Banco de dados inicializado.")