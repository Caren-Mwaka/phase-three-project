from database import CONN, CURSOR

class MaintenanceRecord:

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