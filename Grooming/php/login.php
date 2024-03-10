<?php

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if the username and password fields are set
    if (isset($_POST['username']) && isset($_POST['password'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Sanitize inputs to prevent SQL injection and other attacks
        $sanitized_username = htmlspecialchars($username);
        $sanitized_password = htmlspecialchars($password);

        // Validate the username and password (replace with your authentication logic)
        if ($sanitized_username === 'example' && $sanitized_password === 'password') {
            echo json_encode(['success' => true, 'message' => 'Login successful']);
        } else {
            echo json_encode(['success' => false, 'message' => 'Invalid credentials']);
        }
    } else {
        // If username or password fields are missing in the request
        echo json_encode(['success' => false, 'message' => 'Username or password not provided']);
    }
} else {
    // If the request method is not POST
    echo json_encode(['success' => false, 'message' => 'Invalid request method']);
}

