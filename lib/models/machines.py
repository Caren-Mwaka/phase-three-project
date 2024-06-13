from database import CONN, CURSOR

class Machine:

    def __init__(self, name, type):
        self.id = None  
        self.name = name
        self.type = type

    def __repr__(self):
        return f"Machine(id={self.id}, name={self.name}, type={self.type})"

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL
        )
        ''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS machines')
        CONN.commit()
