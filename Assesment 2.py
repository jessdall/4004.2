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


def add_inventory_item(warehouse_id, item_name, quantity, threshold):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Inventory (warehouse_id, item_name, quantity, threshold) 
            VALUES (?, ?, ?, ?)
        ''', (warehouse_id, item_name, quantity, threshold))
        print("Inventory item added successfully.")


def update_inventory_item(item_id, quantity):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Inventory SET quantity = ? WHERE id = ?
        ''', (quantity, item_id))
        print("Inventory updated successfully.")


def view_inventory():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Inventory')
        items = cursor.fetchall()
        return items


def delete_inventory_item(item_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM Inventory WHERE id = ?
        ''', (item_id,))
        print("Inventory item deleted successfully.")


def add_transportation(vehicle_id, driver_name, schedule, route):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Transportation (vehicle_id, driver_name, schedule, route)
            VALUES (?, ?, ?, ?)
        ''', (vehicle_id, driver_name, schedule, route))
        print("Transportation entry added successfully.")


def view_transportation():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Transportation')
        transportation = cursor.fetchall()
        return transportation


def add_user(username, password, role):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Users (username, password, role)
            VALUES (?, ?, ?)
        ''', (username, hashed_password, role))
        print("User added successfully.")


def authenticate_user(username, provided_password):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM Users WHERE username = ?', (username,))
        result = cursor.fetchone()
        if result:
            stored_password = result[0]
            return hashlib.sha256(provided_password.encode()).hexdigest() == stored_password
        return False


# Set up the database tables
setup_database()

# Example usage:
add_user('admin', 'password123', 'administrator')
authenticated = authenticate_user('admin', 'password123')
print("Authentication successful:", authenticated)

add_inventory_item(1, 'Widgets', 100, 10)
print("Current inventory:", view_inventory())
