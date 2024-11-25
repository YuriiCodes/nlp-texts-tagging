import sqlite3
from analyzer import extract_keywords

DB_NAME = "texts.db"


# Ініціалізація бази даних
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            source TEXT,
            tags TEXT
        )
    """)
    conn.commit()
    conn.close()


# Додавання тексту до бази даних
def add_text(text, source, tags=None):
    if not tags:
        # Генеруємо теги автоматично
        keywords = extract_keywords(text)
        tags = ", ".join(keywords)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO texts (text, source, tags) VALUES (?, ?, ?)", (text, source, tags))
    conn.commit()
    conn.close()


# Отримання всіх текстів
def get_texts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, source, tags FROM texts")
    rows = cursor.fetchall()
    conn.close()
    return rows


# Оновлення тегів для тексту
def update_tags(text_id, new_tags):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE texts SET tags = ? WHERE id = ?", (new_tags, text_id))
    conn.commit()
    conn.close()


# Пошук текстів за фільтрами
def search_texts(query=None, tag=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Базовий SQL-запит
    query_base = "SELECT id, text, source, tags FROM texts WHERE 1=1"

    # Динамічно додаємо фільтри
    params = []
    if query:
        query_base += " AND text LIKE ?"
        params.append(f"%{query}%")
    if tag:
        query_base += " AND tags LIKE ?"
        params.append(f"%{tag}%")

    cursor.execute(query_base, params)
    rows = cursor.fetchall()
    conn.close()
    return rows
