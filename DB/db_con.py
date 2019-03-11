''' module that connects  to the database  '''
import psycopg2

def db_init():
    ''' creates db connection '''
    db_conn = psycopg2.connect(
        "dbname='flocka_records' user='postgres' host='localhost' password='postgres'",
        connection_factory=None, cursor_factory=None)
    return db_conn
