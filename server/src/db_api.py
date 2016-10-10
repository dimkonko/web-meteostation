import MySQLdb as mdb


class MySQLApi(object):
    def __init__(self, config):
        self.config = config

    def connect(self):
        config = self.config
        return mdb.connect(config['HOST'], config['USERNAME'], config['PASSWORD'], config['DBNAME'])

    def get_dict_cursor(self, conn):
        return conn.cursor(mdb.cursors.DictCursor)

    def get_meteo_data(self):
        rows = []
        con = self.connect()
        with con:
            cur = self.get_dict_cursor(con)
            cur.execute("select * from METEO_DATA")
            rows = cur.fetchall()

        return rows

    def insert_meteo_data(self, t, h, create_date):
        con = self.connect()
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO METEO_DATA (temperature, humidity, create_date) VALUES (%s, %s, %s)" % (t, h, create_date))

