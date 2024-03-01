-- Active: 1703403626338@@127.0.0.1@3306

CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone_number VARCHAR(15)
);

-- Create Dogs table
CREATE TABLE Dogs (
    dog_id INT PRIMARY KEY,
    customer_id INT,
    dog_name VARCHAR(50) NOT NULL,
    breed VARCHAR(50),
    age INT,
    gender VARCHAR(4),
);

-- Create Services table
CREATE TABLE Services (
    service_id INT PRIMARY KEY,
    service_name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Create Appointments table
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY,
    customer_id INT,
    dog_id INT,
    service_id INT,
    appointment_date DATE,
    appointment_time TIME,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (dog_id) REFERENCES Dogs(dog_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);

