CREATE DATABASE glass;

CREATE TABLE linkedin (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(80),
    title VARCHAR(80)
);

CREATE TABLE glassdoor (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(80),
    title VARCHAR(80),
    count INT,
    max_sal INT,
    min_sal INT,
    mean_sal INT
);
