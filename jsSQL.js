const sqlite3 = require('sqlite3').verbose();

function login(username, password) {
    const db = new sqlite3.Database('users.db');
    const query = `SELECT * FROM users WHERE username = ? AND password = ?`;
    
    db.get(query, [username, password], (err, row) => {
        if (err) {
            console.error("Database error:", err.message);
            return;
        }

        if (row) {
            console.log("Login successful!");
        } else {
            console.log("Invalid credentials.");
        }
    });
}
