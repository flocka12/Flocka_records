''' module that connects  to the database  '''
import psycopg2
import os


def db_init():
    """creates db connection"""

    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    host = os.getenv('DB_HOST')
    password = os.getenv('DB_PASSWORD')
    
    db_conn = psycopg2.connect(
        "dbname={} user={} host={} password={}".format(dbname, user, host, password),
        connection_factory=None, cursor_factory=None)
    return db_conn
