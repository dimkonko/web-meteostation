CREATE USER 'meteo'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON meteo . * TO 'meteo'@'localhost';
FLUSH PRIVILEGES;
