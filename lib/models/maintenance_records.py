from database import CONN, CURSOR

class MaintenanceRecord:
    all_maintenance_records = {}

    def __init__(self, machine_id, description, performed_at, id=None):
        self.id = id 
        self.machine_id = machine_id
        self.description = description
        self.performed_at = performed_at

    def __repr__(self):
        return f"MaintenanceRecord(id={self.id}, machine_id={self.machine_id}, description={self.description}, performed_at={self.performed_at})"

    @staticmethod
    def create_table():
        CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS maintenance_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            performed_at TEXT NOT NULL,
            FOREIGN KEY (machine_id) REFERENCES machines(id)
        )
        ''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS maintenance_records')
        CONN.commit()

    def save(self):
        """Save the maintenance record instance to the database."""
        sql = """
            INSERT INTO maintenance_records (machine_id, description, performed_at)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.machine_id, self.description, self.performed_at))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all_maintenance_records[self.id] = self

    def update(self, description=None, performed_at=None):
        """Update the maintenance record instance in the database."""
        if description:
            self.description = description
        if performed_at:
            self.performed_at = performed_at
        sql = """
            UPDATE maintenance_records
            SET description = ?, performed_at = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.description, self.performed_at, self.id))
        CONN.commit()

    @classmethod
    def create(cls, machine_id, description, performed_at):
        record = cls(machine_id, description, performed_at)
        record.save()  # Call save method to insert into the database
        return record  # Return the created maintenance record instance

    def delete(self):
        sql = """
            DELETE FROM maintenance_records
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all_maintenance_records[self.id]

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM maintenance_records')
        records = CURSOR.fetchall()
        return [cls.find_by_id(record["id"]) for record in records]

    @classmethod
    def find_by_id(cls, record_id):
        CURSOR.execute('SELECT * FROM maintenance_records WHERE id = ?', (record_id,))
        record = CURSOR.fetchone()
        if record:
            return cls(record["machine_id"], record["description"], record["performed_at"], id=record["id"])
        return None

    @classmethod
    def get_records_by_machine(cls, machine_id):
        CURSOR.execute('SELECT * FROM maintenance_records WHERE machine_id = ?', (machine_id,))
        records = CURSOR.fetchall()
        return [cls.find_by_id(record["id"]) for record in records]

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

    @classmethod
    def create(cls, name, machine_id, quantity=0):
        part = cls(name, machine_id, quantity)
        part.save()  
        return part  

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
        return parts

    @classmethod
    def find_by_id(cls, part_id):
        CURSOR.execute('SELECT * FROM parts WHERE id = ?', (part_id,))
        part = CURSOR.fetchone()
        return part

    @classmethod
    def get_parts_by_machine(cls, machine_id):
        CURSOR.execute('SELECT * FROM parts WHERE machine_id = ?', (machine_id,))
        parts = CURSOR.fetchall()
        return parts
