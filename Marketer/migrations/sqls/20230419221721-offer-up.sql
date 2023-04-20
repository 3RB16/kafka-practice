/* Replace with your SQL commands */
CREATE TABLE offer(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    price INT NOT NULL
);