USE 'meteo'

CREATE TABLE METEO_DATA_SMART_HOUSE (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT(4, 2) NOT NULL,
    humidity TINYINT NOT NULL,
    create_date DATETIME NOT NULL
);
