using System;
using System.Data.SQLite;

class Program {
    static void Login(string username, string password) {
        using (var conn = new SQLiteConnection("Data Source=users.db")) {
            conn.Open();

            string query = "SELECT * FROM users WHERE username = @username AND password = @password;";
            using (var cmd = new SQLiteCommand(query, conn)) {
                cmd.Parameters.AddWithValue("@username", username);
                cmd.Parameters.AddWithValue("@password", password);

                using (var reader = cmd.ExecuteReader()) {
                    if (reader.Read()) {
                        Console.WriteLine("Login successful!");
                    } else {
                        Console.WriteLine("Invalid credentials.");
                    }
                }
            }
        }
    }
}
