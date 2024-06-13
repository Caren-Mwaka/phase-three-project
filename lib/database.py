#Setting up the connection to an SQLite database (part_manager.db) and preparing a cursor (CURSOR) for executing queries.
import sqlite3

def get_connection():
    conn = sqlite3.connect('part_manager.db')
    conn.row_factory = sqlite3.Row
    return conn

CONN = get_connection()
CURSOR = CONN.cursor()