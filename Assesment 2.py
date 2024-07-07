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

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        warehouse_id INTEGER NOT NULL,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        threshhold INTEGER NOT NULL,
        FOREIGN KEY(warehouse_id) REFERENCES Warehouses(id),
        ''')

        cursor.execute('''
               CREATE TABLE IF NOT EXISTS Transportation (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   vehicle_id TEXT NOT NULL,
                   driver_name TEXT NOT NULL,
                   schedule TEXT NOT NULL,
                   route TEXT NOT NULL
               ''')

        cursor.execute('''
              CREATE TABLE IF NOT EXISTS Users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  role TEXT NOT NULL
              ''')

        print("Database setup complete.")













