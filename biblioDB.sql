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

INSERT INTO usuario (username, direccion, municipio, estado, email, contrasena) VALUES ('Victor Omar Jimenez Barajas', 'Valle de Santiago 100', 'Salamanca', 'Guanajuato', 'zodiaco405@hotmail.com', 'universidad');
INSERT INTO usuario (username, direccion, municipio, estado, email, contrasena) VALUES ('Julian Lopez Ortega', '12 de Octubre 400', 'Morelia', 'Michoacan', 'zodiaco48@hotmail.com', 'guadalajar');
