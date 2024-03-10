<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve user signup data
    $username = htmlspecialchars($_POST['username']);
    $email = htmlspecialchars($_POST['email']);
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT); // Hash the password for security

    // Database connection details
    $host = 'localhost';
    $user = 'root';
    $password_db = 'password';
    $database = 'your_database'; // Change this to your actual database name

    // Create a database connection
    $conn = new mysqli($host, $user, $password_db, $database);

    // Check the connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Prepare and execute the SQL query to insert user data
    $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $email, $password);

    if ($stmt->execute()) {
        // User registration successful, now insert dog details
        $dogName = htmlspecialchars($_POST["dog_name"]);
        $selectedBreed = htmlspecialchars($_POST["breed"]);
        $age = htmlspecialchars($_POST["age"]);

        // Get the user ID of the newly registered user
        $userId = $conn->insert_id;

        // Insert dog details into the dogs table
        $stmtDog = $conn->prepare("INSERT INTO dogs (user_id, dog_name, breed, age) VALUES (?, ?, ?, ?)");
        $stmtDog->bind_param("isss", $userId, $dogName, $selectedBreed, $age);

        if ($stmtDog->execute()) {
            // Registration successful, redirect to dashboard
            header('Location:/Grooming/html/python/dashboard.html');
            exit(); // Ensure that no further code is executed after the redirect
        } else {
            echo "Registration failed for dog details: " . $stmtDog->error;
        }

        // Close the dog details statement
        $stmtDog->close();
    } else {
        echo "Registration failed: " . $stmt->error;
    }

    // Close the user registration statement and the connection
    $stmt->close();
    $conn->close();
} else {
    echo "Invalid request";
}




