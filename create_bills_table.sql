
-- Make sure to create the database first:
-- CREATE DATABASE feedback_db;

USE feedback_db;

CREATE TABLE IF NOT EXISTS bills (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer VARCHAR(100),
    item VARCHAR(100),
    price DECIMAL(10, 2),
    quantity INT,
    total DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
