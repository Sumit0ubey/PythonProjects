import sqlite3 as sql


def create_tables_database():
    database = sql.connect('Inventory_Storage.db')
    query = database.cursor()

    query.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT UNIQUE,
                    password INTEGER)''')

    query.execute('''CREATE TABLE IF NOT EXISTS products
                    (product_id INTEGER UNIQUE,
                    product_name TEXT,
                    quantity INTEGER,
                    price REAL)''')

    database.commit()
    database.close()


create_tables_database()
