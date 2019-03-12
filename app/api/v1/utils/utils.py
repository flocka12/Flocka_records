''' module representing utils '''
from psycopg2.extras import RealDictCursor

from DB.db_con import db_init
class Utility:
    ''' creates utils for factoring code '''
    def __init__(self):
        self.connection = db_init()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
    def find_item_if_exists(self, tablename, column, value):
        """Find an item if it exists"""
        query = """SELECT * FROM {} WHERE {}='{}';""".format(tablename, column, value)
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
