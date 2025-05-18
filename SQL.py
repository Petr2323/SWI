import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?;"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Invalid credentials.")
    conn.close()
