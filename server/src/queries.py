GET_ALL_RECORDS = """
SELECT *
FROM METEO_DATA
"""

GET_LAST_RECORD = """
SELECT *
FROM METEO_DATA
ORDER BY id DESC
LIMIT 1;
"""

INSERT_RECORD = """
INSERT INTO METEO_DATA
(temperature, humidity, create_date)
VALUES
(%s, %s, '%s');
"""
