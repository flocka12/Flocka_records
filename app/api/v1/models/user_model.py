''' Module representing the user model '''
from psycopg2.extras import RealDictCursor

from DB.db_con import db_init
class User():
    ''' Definition for user model '''
    table = 'users'

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
    def add_user(self, data):
        """Add a new user to the 'users' table"""
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        username = data['username']
        password = data['password']
        query = "INSERT INTO {} (firstname, lastname, username, email, password)" \
                " VALUES (%s, %s, %s, %s, %s) RETURNING {}.*".format(self.table, self.table)

        self.cursor.execute(query, (firstname, lastname, username, email, password))
        self.connection.commit()
        return self.cursor.fetchone()
