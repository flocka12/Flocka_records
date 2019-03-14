''' Module representing the music model '''
from psycopg2.extras import RealDictCursor

from DB.db_con import db_init
class Music():
    ''' Definition for music model '''
    table = 'music'

    def __init__(self):
        self.connection = db_init()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
    def find_if_exists(self, key, value):
        """Find a user by username"""
        query = "SELECT COUNT (*) FROM {} WHERE {} = %s".format(
            self.table, key)
        self.cursor.execute(query, (value,))
        result = self.cursor.fetchone()

        return result['count']
    def all(self):
        """ Select all from the table """
        query = "SELECT * FROM {}".format(self.table)
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return results
