import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    # connect to default database
    conn = psycopg2.connect(
        host='localhost',
        database='mypostgresdb',
        user='admin',
        password='admin'
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect(
        host='localhost',
        database='sparkifydb',
        user='admin',
        password='admin'
    )
    cur = conn.cursor()

    return cur, conn

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    print("Table dropped")

    create_tables(cur, conn)
    print("Table created")

    conn.close()

if __name__ == "__main__":
    main()