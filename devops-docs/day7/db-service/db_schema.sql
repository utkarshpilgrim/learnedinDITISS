USE mydb;

CREATE TABLE Product(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    price FLOAT
);

INSERT INTO Product (title, price)
VALUES 
    ('product 1', 100), 
    ('product 2', 200),
    ('product 3', 300),
    ('product 4', 400),
    ('product 5', 500);