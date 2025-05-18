import sqlite3

def safe_insert_user(name, password, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Use parameterized query to prevent SQL injection
    cursor.execute(
        "INSERT INTO users (name, password, email) VALUES (?, ?, ?)", 
        (name, password, email)
    )
    conn.commit()
    conn.close()
