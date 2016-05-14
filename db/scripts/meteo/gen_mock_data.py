import random

from datetime import datetime, timedelta

INSERT_PATTERN = "INSERT INTO METEO_DATA_SMART_HOUSE(temperature, humidity, create_date) VALUES(%f, %d, '%s');\n"

# TODO: Read config variables from console
FILE_NAME = "insert_mock_data.sql"
DB_NAME = "meteo"

days = 7

with open("/vagrant/db/sql/data/" + FILE_NAME, "w") as f:
    f.write("USE %s\n\n" % DB_NAME)

    hour_delta = timedelta(hours=1)
    create_date = datetime(2016, 1, 1, 0, 0, 0, 0)
    for i in xrange(0, days * 24):
        temperature = random.uniform(20.0, 30.0)
        humidity = random.randint(50, 80)
        create_date += hour_delta
        f.write(INSERT_PATTERN % (temperature, humidity, str(create_date)))
