import sqlite3
import hashlib



def connect_db():
    return sqlite3.connect('stmarys_logistics.db')


def setup_database():
    with connect_db() as con:
        cursor = con.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Warehouses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT NOT NULL,
        capacity INTEGER NOT NULL,
        ''')



