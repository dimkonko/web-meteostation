CREATE DATABASE IF NOT EXISTS meteo

USE 'meteo'

CREATE TABLE METEO_DATA  (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT(4, 2),
    humidity TINYINT ,
    wind_speed FLOAT(4, 2),
    wind_dir VARCHAR(2),
    create_date DATETIME NOT NULL
);
