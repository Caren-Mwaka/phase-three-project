from database import CONN, CURSOR

class Part:

    def __init__(self, name, machine_id, quantity=0):
        self.id = None  
        self.name = name
        self.machine_id = machine_id
        self.quantity = quantity

    def __repr__(self):
        return f"Part(id={self.id}, name={self.name}, machine_id={self.machine_id}, quantity={self.quantity})"

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            machine_id INTEGER NOT NULL,
            quantity INTEGER DEFAULT 0,
            FOREIGN KEY (machine_id) REFERENCES machines(id)
        )
        ''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS parts')
        CONN.commit()