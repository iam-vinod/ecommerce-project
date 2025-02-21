CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2)
);

INSERT INTO products (name, price) VALUES
('Laptop', 1000.00),
('Phone', 500.00);
