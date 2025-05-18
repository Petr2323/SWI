 <?php
function login($username, $password) {
    try {
        $pdo = new PDO('sqlite:users.db');
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Use prepared statements to avoid SQL injection
        $stmt = $pdo->prepare('SELECT * FROM users WHERE username = :username');
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            echo "Login successful!";
        } else {
            echo "Invalid credentials.";
        }
    } catch (PDOException $e) {
        echo "Database error: " . htmlspecialchars($e->getMessage());
    }
}
?>
