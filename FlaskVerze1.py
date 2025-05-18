from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'data.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/save', methods=['POST'])
def save_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing 'name' or 'email'"}), 400

    name = data['name']
    email = data['email']

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "User saved successfully"}), 201

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
