from database import CONN, CURSOR

class Part:
    def __init__(self, name, machine_id, quantity=0, id=None):
        self.id = id
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

    @classmethod
    def create(cls, name, machine_id, quantity=0):
        part = cls(name, machine_id, quantity)
        part.save()
        return part

    def save(self):
        """Save the part instance to the database."""
        sql = """
            INSERT INTO parts (name, machine_id, quantity)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.machine_id, self.quantity))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all_parts[self.id] = self

    def update(self, name=None, machine_id=None, quantity=None):
        """Update the part instance in the database."""
        if name:
            self.name = name
        if machine_id:
            self.machine_id = machine_id
        if quantity is not None:
            self.quantity = quantity
        sql = """
            UPDATE parts
            SET name = ?, machine_id = ?, quantity = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.machine_id, self.quantity, self.id))
        CONN.commit()

    def delete(self):
        """Delete the part instance from the database."""
        sql = """
            DELETE FROM parts
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all_parts[self.id]

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM parts')
        parts = CURSOR.fetchall()
        return [cls(name=row[1], machine_id=row[2], quantity=row[3], id=row[0]) for row in parts]

    @classmethod
    def find_by_id(cls, part_id):
        CURSOR.execute('SELECT * FROM parts WHERE id = ?', (part_id,))
        part_data = CURSOR.fetchone()
        if part_data:
            return cls(part_data[1], part_data[2], part_data[3], id=part_data[0])
        return None


    @classmethod
    def get_parts_by_machine(cls, machine_id):
        CURSOR.execute('SELECT * FROM parts WHERE machine_id = ?', (machine_id,))
        parts = CURSOR.fetchall()
        return [cls(name=row[1], machine_id=row[2], quantity=row[3], id=row[0]) for row in parts]

