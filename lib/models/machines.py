from database import CONN, CURSOR

class Machine:
    all_machines = {}

    def __init__(self, name, type, id=None):
        self.id = id
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

    @classmethod
    def create(cls, name, type):
        machine = cls(name, type)
        machine.save()  
        return machine  

    def save(self):
        """Save the machine instance to the database."""
        sql = """
            INSERT INTO machines (name, type)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def update(self, name=None, type=None):
        """Update the machine instance in the database."""
        if name:
            self.name = name
        if type:
            self.type = type
        sql = """
            UPDATE machines
            SET name = ?, type = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.type, self.id))
        CONN.commit()

    def delete(self):
        # """Delete the machine instance from the database."""
        # # Delete associated parts
        # CURSOR.execute('DELETE FROM parts WHERE machine_id = ?', (self.id,))
        
        # # Delete associated maintenance records
        # CURSOR.execute('DELETE FROM maintenance_records WHERE machine_id = ?', (self.id,))
        
        # Delete the machine itself
        CURSOR.execute('DELETE FROM machines WHERE id = ?', (self.id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM machines')
        machines = CURSOR.fetchall()
        return machines

    @classmethod
    def find_by_id(cls, machine_id):
        CURSOR.execute('SELECT * FROM machines WHERE id = ?', (machine_id,))
        machine_data = CURSOR.fetchone()
        if machine_data:
            return cls(machine_data['name'], machine_data['type'], id=machine_data['id'])
        return None

    @classmethod
    def get_parts_by_machine(cls, machine_id):
        CURSOR.execute('SELECT * FROM parts WHERE machine_id = ?', (machine_id,))
        parts = CURSOR.fetchall()
        return parts

    @classmethod
    def get_maintenance_records_by_machine(cls, machine_id):
        CURSOR.execute('SELECT * FROM maintenance_records WHERE machine_id = ?', (machine_id,))
        records = CURSOR.fetchall()
        return records
