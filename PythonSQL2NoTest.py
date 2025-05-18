import sqlite3
import hashlib

def create_user_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    password_hash = hash_password(password)
    try:
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")
    conn.close()

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    password_hash = hash_password(password)
    cursor.execute('SELECT * FROM users WHERE username = ? AND password_hash = ?', (username, password_hash))
    result = cursor.fetchone()
    conn.close()
    if result:
        print("Login successful.")
        return True
    else:
        print("Login failed.")
        return False

# Example usage
if __name__ == '__main__':
    create_user_table()
    # Uncomment below to add a user
    # add_user('testuser', 'securepassword123')

    login('testuser', 'securepassword123')  # Try logging in
