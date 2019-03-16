''' module that connects and creates queries'''
from .db_con import db_init

def create_tables():
    """Create database tables"""
    db_conn = db_init()
    db_curr = db_conn.cursor()
    table_queries = [
        """
        CREATE TABLE IF NOT EXISTS users(
        id SERIAL NOT NULL,
        firstname VARCHAR(191) NOT NULL,
        lastname VARCHAR(191) NOT NULL,
        email VARCHAR(191) NOT NULL,
        username VARCHAR(191) NOT NULL,
        password VARCHAR(191) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS music(
        id SERIAL NOT NULL,
        name VARCHAR(191) NOT NULL
        )
        """
        ]
    for query in table_queries:
        db_curr.execute(query)
    db_conn.commit()
def truncate():
    """Delete all the data in all the tables"""
    db_conn = db_init()
    db_curr = db_conn.cursor()
    trun_quer = ["users", "music"]
    db_curr.execute('TRUNCATE TABLE ' + ','.join(trun_quer) +
                    ' RESTART IDENTITY CASCADE')
    db_conn.commit()

def drop_tables():
    """Drop all the database tables"""
    db_conn = db_init()
    db_curr = db_conn.cursor()
    trun_quer = ["users", "music"]
    for table in trun_quer:
        db_curr.execute("DROP TABLE IF EXISTS {} ".format(table))
        db_conn.commit()
# def seed():
#     db_conn = db_init()
#     db_cur = db_conn.cursor()
#     db_cur.execute("INSERT INTO users (firstname, lastname, email, username, password)\
#         VALUES ('Waka', 'Jos', 'admin@app.com', 'hypnos', 'stesra')"
#         db_conn.commit()
if __name__ == "__main__":
    pass
