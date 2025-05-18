import sqlite3

def safe_insert_user(name, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Pouziti parametrizovaneho dotazu pro prevenci SQL injection
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
