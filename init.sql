CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);


INSERT INTO users (name, email) VALUES
('James', 'james@example.com'),
('Alice', 'alice@example.com'),
('Sam', 'Sam@example.com'),
('John', 'John@example.com'),
('Alex', 'alex@example.com'),
('steve', 'steve@example.com'),
('Bran', 'Bran@example.com');
