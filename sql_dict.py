import sqlite3


class LiteDict(object):
    def __init__(self):
        self.con = sqlite3.connect('my.db')

    def __getitem__(self, key):
        with self.con:
            cur = self.con.cursor()

            cur.execute(f'SELECT * FROM mytable WHERE IDKEY={key}')
            return next(cur)

    def __setitem__(self, key, value):
        pass