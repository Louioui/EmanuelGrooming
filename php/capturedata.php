<?php
// Database connection details (replace with your own)
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Function to validate and sanitize user input
function validate_and_sanitize($data) {
  $validated_data = array();
  foreach ($data as $key => $value) {
    $validated_data[$key] = filter_var(htmlspecialchars($value), FILTER_SANITIZE_STRING);
  }
  return $validated_data;
}

// Get user data from POST request (assuming a form)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $user_data = validate_and_sanitize($_POST);

  // Prepare SQL statement (prevents SQL injection)
  $sql = "INSERT INTO your_table (column1, column2, ...) VALUES (?, ?, ...)";
  $stmt = $conn->prepare($sql);

  // Bind parameters to the statement
  $bind_params = [];
  foreach ($user_data as $value) {
    $bind_params[] = "s"; // String parameter type (adjust based on data types)
    $bind_params[] = $value;
  }

  // Execute the statement
  $stmt->bind_param(...$bind_params);
  if ($stmt->execute()) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }
  $stmt->close();
}

$conn->close();
?>