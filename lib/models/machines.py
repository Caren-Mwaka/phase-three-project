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
        """Saves the machine instance to the database."""
        sql = """
            INSERT INTO machines (name, type)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type))
        CONN.commit()
        self.id = CURSOR.lastrowid


    @classmethod
    def update(cls, machine_data):
        """Updates the machine instance in the database."""
        sql = """
            UPDATE machines
            SET name = ?, type = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (machine_data['name'], machine_data['type'], machine_data['id']))
        CONN.commit()
        print(f"Updated machine with ID {machine_data['id']}")

    @classmethod
    def delete(cls, machine):
        """Deletes the machine instance from the database."""
        sql = 'DELETE FROM machines WHERE id = ?'
        CURSOR.execute(sql, (machine['id'],))
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM machines')
        machines = CURSOR.fetchall()
        return machines

    @classmethod
    def find_by_id(cls, machine_id):
        sql = 'SELECT * FROM machines WHERE id = ?'
        CURSOR.execute(sql, (machine_id,))
        row = CURSOR.fetchone()
        if row:
            return {
                'id': row['id'],
                'name': row['name'],
                'type': row['type']
            }
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
