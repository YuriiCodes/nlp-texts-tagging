import sqlite3

DB_NAME = "texts.db"

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

def add_text(text, source, tags):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO texts (text, source, tags) VALUES (?, ?, ?)", (text, source, tags))
    conn.commit()
    conn.close()

def get_texts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, source, tags FROM texts")
    rows = cursor.fetchall()
    conn.close()
    return rows
