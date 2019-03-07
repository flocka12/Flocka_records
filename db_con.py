''' module that connects  to the database and queries'''
import psycopg2

CONN = psycopg2.connect(
    "dbname='flocka_records' user='postgres' host='localhost' password='postgres'")
CURR = CONN.cursor()
def truncate(TABLES):
    """Delete all the data in all the tables"""
    TABLES = ["users", "music"]
    for table in TABLES:
        CURR.execute("TRUNCATE TABLE {} CASCADE".format(table))
        CONN.commit()

def drop_tables(TABLES):
    """Drop all the database tables"""
    TABLES = ["users", "music"]
    for table in TABLES:
        CURR.execute("DROP TABLE {} ".format(table))
        CONN.commit()

def create_tables(TABLE_QUERIES):
    """Create database tables"""
    TABLE_QUERIES = [
        """
        CREATE TABLE IF NOT EXISTS users(
        id SERIAL NOT NULL,
        firstname VARCHAR(191) NOT NULL,
        lastname VARCHAR(191) NOT NULL,
        email VARCHAR(191) NOT NULL,
        password VARCHAR(191) NOT NULL
        )
        """
        ]
    for query in TABLE_QUERIES:
        CURR.execute(query)
    CONN.commit()

if __name__ == "__main__":
    create_tables(TABLE_QUERIES)
    # drop_tables(TABLES)
    pass
    