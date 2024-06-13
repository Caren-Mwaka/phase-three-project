from models.machines import Machine
from models.parts import Part
from models.maintenance_records import MaintenanceRecord

if __name__ == "__main__":

    Machine.drop_table()
    Machine.create_table()

    Part.drop_table()
    Part.create_table()

    MaintenanceRecord.drop_table()
    MaintenanceRecord.create_table()