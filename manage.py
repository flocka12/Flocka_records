''' module to create database migrations '''
import argparse
import psycopg2

CONNECTION = psycopg2.connect(
    "dbname='flocka_records' user='postgres' host='localhost' password='postgres'")
def migrate(CONNECTION):
    pass


if __name__ == "__main__":

    PARSER = argparse.ArgumentParser(
        description='Database management tool for iReporter')

    PARSER.add_argument(
        '-a', '--action', metavar='[migrate|truncate|seed]', help='Database action',
        choices={'migrate', 'truncate', 'seed'}, const='migrate', nargs='?')

    ARGS = PARSER.parse_args()

# open database connection

    if ARGS.action == 'migrate':
        # run migrate function
        pass
    elif ARGS.action == 'truncate':
        # run truncate function
        pass
    elif ARGS.action == 'seed':
        # adds seed data to appliction
        pass
    else:
        pass

# close connection here
