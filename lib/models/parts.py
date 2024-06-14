from database import CONN, CURSOR

class Part:
    all_parts = {}

    def __init__(self, name, machine_id, quantity=0):
        self.id = None
        self.name = name
        self.machine_id = machine_id
        self.quantity = quantity

    def __repr__(self):
        return f"Part(id={self.id}, name={self.name}, machine_id={self.machine_id}, quantity={self.quantity})"

    @staticmethod
    def create_table():
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

    @classmethod
    def create(cls, name, machine_id, quantity=0):
        part = cls(name, machine_id, quantity)
        part.save()
        return part
    
    def save(self):
        """Saves the part instance to the database."""
        sql = """
            INSERT INTO parts (name, machine_id, quantity)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.machine_id, self.quantity))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all_parts[self.id] = self
    
    @classmethod
    def update(cls, part_data ):
        """Updates the part instance in the database."""

        sql = """
            UPDATE parts
            SET name = ?, machine_id = ?, quantity = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (part_data['name'], part_data['machine_id'], part_data['quantity'], part_data['id']))
        CONN.commit()

    @classmethod
    def delete(cls, part):
        """Deletes the part instance from the database."""
        sql = """
            DELETE FROM parts
            WHERE id = ?
        """
        CURSOR.execute(sql, (part['id'],))
        CONN.commit()
       
    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM parts')
        parts = CURSOR.fetchall()
        return parts
    
    @classmethod
    def find_by_id(cls, part_id):
        CURSOR.execute('SELECT * FROM parts WHERE id = ?', (part_id,))
        row = CURSOR.fetchone()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'machine_id': row[2],
                'quantity': row[3]
            }
        return None

    @classmethod
    def get_parts_by_machine(cls, machine_id):
        CURSOR.execute('SELECT * FROM parts WHERE machine_id = ?', (machine_id,))
        parts = CURSOR.fetchall()
        return parts
