# database.py
import sqlite3

class Database:
    def __init__(self, db_name='bestbuy_products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                url TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_product(self, name, price, url):
        self.cursor.execute('''
            INSERT INTO products (name, price, url)
            VALUES (?, ?, ?)
        ''', (name, price, url))
        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def clear_table(self):
        self.cursor.execute('DELETE FROM products')
        self.conn.commit()

    def close(self):
        self.conn.close()