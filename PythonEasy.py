import sqlite3

def store_user_input():
    # Connect to (or create) a SQLite database file
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inputs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT NOT NULL
        )
    ''')

    # Get input from the user
    user_input = input("Enter some text to store in the database: ")

    # Insert the input into the table
    cursor.execute('INSERT INTO inputs (user_text) VALUES (?)', (user_input,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Input stored successfully!")

# Example usage
if __name__ == "__main__":
    store_user_input()
