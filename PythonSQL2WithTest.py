import sqlite3
import unittest

# Database initialization for demonstration
def initialize_db():
    conn = sqlite3.connect("test_users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)
    cursor.execute("DELETE FROM users")  # Clear table for repeatable tests
    # Insert sample users
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("alice", "password123"))
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("bob", "secure456"))
    conn.commit()
    conn.close()

# Login function
def login(username, password):
    conn = sqlite3.connect("test_users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Unit tests
class TestLoginFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        initialize_db()

    def test_valid_login(self):
        self.assertTrue(login("alice", "password123"))
        self.assertTrue(login("bob", "secure456"))

    def test_invalid_username(self):
        self.assertFalse(login("charlie", "password123"))

    def test_invalid_password(self):
        self.assertFalse(login("alice", "wrongpass"))

    def test_invalid_credentials(self):
        self.assertFalse(login("charlie", "nopass"))

# Run tests if this script is executed directly
if __name__ == "__main__":
    unittest.main()
