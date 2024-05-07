import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to SQLite database.")
    except sqlite3.Error as e:
        print("Error:", e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print("Error:", e)

def insert_record(conn, record):
    sql = ''' INSERT INTO records(name, age, city)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, record)
    conn.commit()
    print("Record inserted successfully.")

def retrieve_records(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM records")

    rows = cur.fetchall()

    print("\nRecords:")
    for row in rows:
        print(row)

def main():
    database = "mydatabase.db"

    create_table_sql = """ CREATE TABLE IF NOT EXISTS records (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER,
                            city TEXT
                        ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, create_table_sql)

        records_to_insert = [
            ('Sumit', 19, 'Earth'),
            ('Shivam', 18, 'Earth'),
            ('Himayu', 17, 'Earth'),
            ('Siddarth', 20, 'Earth')
        ]
        for record in records_to_insert:
            insert_record(conn, record)

        retrieve_records(conn)

        conn.close()
        print("\nConnection to SQLite database closed.")
    else:
        print("Error: Unable to establish database connection.")

if __name__ == '__main__':
    main()
