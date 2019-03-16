''' module to create database migrations '''
import argparse
from DB.db_con import db_init
from DB.queries import drop_tables, create_tables, truncate

def migrate():
    ''' create db migrations '''
    drop_tables()
    create_tables()
    # create_tables(db_conn)
    # pass


if __name__ == "__main__":

    PARSER = argparse.ArgumentParser(
        description='Database management tool for flocka_records')

    PARSER.add_argument(
        '-a', '--action', metavar='[migrate|truncate|seed]', help='Database action',
        choices={'migrate', 'truncate', 'seed'}, const='migrate', nargs='?')

    ARGS = PARSER.parse_args()

# open database connection
    BASE_CONN = db_init()

    if ARGS.action == 'migrate':
        migrate()
    elif ARGS.action == 'truncate':
        truncate()
    elif ARGS.action == 'seed':
        # seed()
        pass
    else:
        pass
    BASE_CONN.commit()
# close connection here
