import sqlite3
import pandas as pd
from model import Item
from typing import List

db_name = "item_list.db"

def get_db_connection():
    conn = sqlite3.connect(db_name)
    return conn

def add_post(post: Item):
    """Adiciona um objeto Post ao banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        (post.descricao, post.quantidade)
    )
    conn.commit()
    conn.close()

def fetch_all_posts() -> List[Item]:
    """Busca todos os posts e retorna uma lista de objetos Post."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts ORDER BY quantidade DESC")
    
    rows = cursor.fetchall()
    conn.close()
    
    # Transforma cada linha do resultado do banco em um objeto Post
    return [
        Item(
            id=row['id'], 
            descricao=row['descricao'], 
            quantidade=row['quantidade']
        ) for row in rows
    ]

# Opcional: Uma função para inicializar o DB, se necessário.
def init_db():
    """Inicializa o banco de dados e cria a tabela se ela não existir."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        quantidade INTEGER
    );
    """)
    conn.commit()
    conn.close()

# Se você executar este arquivo diretamente, ele inicializará o banco.
if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado.")