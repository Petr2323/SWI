import sqlite3
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def init_db(db_path='user_inputs.db'):
    """Initialize the database and create table if not exists."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_inputs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                input_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def store_user_input(user_input, db_path='user_inputs.db'):
    """
    Store user input safely in the database.

    Args:
        user_input (str): The user input string.
        db_path (str): Path to the SQLite database file.

    Returns:
        bool: True if success, False otherwise.
    """
    # Input validation
    if not isinstance(user_input, str):
        logging.error("Invalid input type. Expected string.")
        return False
    if len(user_input) == 0:
        logging.error("Input cannot be empty.")
        return False
    if len(user_input) > 500:
        logging.error("Input too long. Maximum 500 characters allowed.")
        return False

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            # Parameterized query to prevent SQL injection
            cursor.execute('INSERT INTO user_inputs (input_text) VALUES (?)', (user_input,))
            conn.commit()
        logging.info("User input stored successfully.")
        return True
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return False
