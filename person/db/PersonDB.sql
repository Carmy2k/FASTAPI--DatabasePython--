DROP DATABASE IF EXISTS PersonDB;
CREATE DATABASE IF NOT EXISTS PersonDB;
USE PersonDB;

DROP TABLE IF EXISTS People;
CREATE TABLE IF NOT EXISTS People (
	id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(48) NOT NULL,
	lastname VARCHAR(48) NOT NULL,
	UNIQUE(firstname, lastname),
	age INT NOT NULL CHECK(age > 0)
);

INSERT INTO People(age, firstname, lastname) VALUES
	(27, 'Alessandra', 'Prota'),
	(42, 'Biagio Rosario', 'Greco'),
	(18, 'Cristiamo', 'La Mura'),
	(18, 'Alessio', 'Rapicano');