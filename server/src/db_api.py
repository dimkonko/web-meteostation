import MySQLdb as mdb


class MySQLApi(object):
    def __init__(self, config):
        self.config = config

    def connect(self):
        config = self.config
        return mdb.connect(config['HOST'], config['USERNAME'], config['PASSWORD'], config['DBNAME'])

    def get_dict_cursor(self, conn):
        return conn.cursor(mdb.cursors.DictCursor)

    def get(self, query):
        rows = []
        con = self.connect()
        with con:
            cur = self.get_dict_cursor(con)
            cur.execute(query)
            rows = cur.fetchall()

        return rows

    def set(self, query, *args):
        con = self.connect()
        with con:
            cur = con.cursor()
            cur.execute(query % args)
