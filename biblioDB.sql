DROP TABLE IF EXISTS usuario;
DROP DATABASE IF EXISTS library;
CREATE DATABASE library;
USE library;

CREATE TABLE usuario
(
    usuario_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
	direccion VARCHAR(30) NOT NULL,
	municipio VARCHAR(30) NOT NULL,
	estado VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL,
    contrasena VARCHAR(100) NOT NULL

);

CREATE TABLE libro
(
	libro_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    edicion INT NOT NULL,
    año INT NOT NULL,
    editorial VARCHAR(50) NOT NULL,
    disponibles INT NOT NULL,
    totales INT NOT NULL
    
);

CREATE TABLE prestamo
(
	usuario_id INT NOT NULL PRIMARY KEY,
    libro_id INT NOT NULL    
);

INSERT INTO usuario (username, direccion, municipio, estado, email, contrasena) VALUES ('Victor Omar Jimenez Barajas', 'Valle de Santiago 100', 'Salamanca', 'Guanajuato', 'zodiaco405@hotmail.com', 'universidad');
INSERT INTO usuario (username, direccion, municipio, estado, email, contrasena) VALUES ('Julian Lopez Ortega', '12 de Octubre 400', 'Morelia', 'Michoacan', 'zodiaco48@hotmail.com', 'guadalajar');
INSERT INTO usuario (username, direccion, municipio, estado, email, contrasena) VALUES ('Luis Blanco', 'Avenida del Valle #54', 'Guerrero', 'Guerrero', 'zodiaco49@hotmail.com', '141414');

INSERT INTO libro (nombre, autor, edicion, año, editorial, disponibles, totales) VALUES ('El Calculo', 'Louis Leithold', 7, 1998, 'Oxford University Press', 7, 7);
INSERT INTO libro (nombre, autor, edicion, año, editorial, disponibles, totales) VALUES ('Calculo', 'Ron Larson - Bruce H. Edwards', 9, 2011, 'McGraw Hill', 11, 11);
INSERT INTO libro (nombre, autor, edicion, año, editorial, disponibles, totales) VALUES ('Fisica para ciencias e ingenieria', 'Serway-Jewett', 9, 2014, 'Cengage Learning', 3, 3);
INSERT INTO libro (nombre, autor, edicion, año, editorial, disponibles, totales) VALUES ('C++ Como Programar', 'DEITEL, HARVEY M.-PAUL J. DEITEL', 6, 2008, 'Prentice Hall', 5, 5);
INSERT INTO libro (nombre, autor, edicion, año, editorial, disponibles, totales) VALUES ('Quimica', 'Raymond Chang', 7, 2002, 'McGraw Hill', 8, 8);
