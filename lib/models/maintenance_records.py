from database import CONN, CURSOR

class MaintenanceRecord:
    all_maintenance_records = {}

    def __init__(self, machine_id, description, performed_at, id=None):
        self.id = id 
        self.machine_id = machine_id
        self.description = description
        self.performed_at = performed_at
        if id is not None:
            self.__class__.all_maintenance_records[id] = self

    def __repr__(self):
        return f"MaintenanceRecord(id={self.id}, machine_id={self.machine_id}, description={self.description}, performed_at={self.performed_at})"

    @classmethod
    def create_table(cls):
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

    @classmethod
    def create(cls, machine_id, description, performed_at):
        record = cls(machine_id, description, performed_at)
        record.save()  
        return record  

    def save(self):
        """Saves the maintenance record instance to the database."""
        sql = """
            INSERT INTO maintenance_records (machine_id, description, performed_at)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.machine_id, self.description, self.performed_at))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all_maintenance_records[self.id] = self

    def update(self, description=None, performed_at=None):
        """Updates the maintenance record instance in the database."""
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


    def delete(self):
        """Deletes the maintenance record instance from the database."""
        sql = """
            DELETE FROM maintenance_records
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        if self.id in type(self).all_maintenance_records:
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

