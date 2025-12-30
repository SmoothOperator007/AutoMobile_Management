/* 
=====================================================
 Automobile Management System - Database Script
=====================================================
*/

-- Create database
CREATE DATABASE IF NOT EXISTS automobile_management;
USE automobile_management;

-- --------------------------------------------------
-- Vehicles Table
-- --------------------------------------------------
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    availability INT NOT NULL
);

-- --------------------------------------------------
-- Customers Table
-- --------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(15),
    email VARCHAR(100)
);

-- --------------------------------------------------
-- Sales Table
-- --------------------------------------------------
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    vehicle_id INT,
    sale_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- --------------------------------------------------
-- Services Table
-- --------------------------------------------------
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT,
    service_date DATE,
    details TEXT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- --------------------------------------------------
-- Sample Data (Optional but useful for testing)
-- --------------------------------------------------

INSERT INTO vehicles (make, model, price, availability) VALUES
('Toyota', 'Camry', 30000, 10),
('Honda', 'Civic', 25000, 5),
('Ford', 'F-150', 40000, 8);

INSERT INTO customers (name, contact, email) VALUES
('Alice Johnson', '9876543210', 'alice@example.com'),
('Bob Smith', '8765432109', 'bob@example.com'),
('Charlie Brown', '7654321098', 'charlie@example.com');
.com');
