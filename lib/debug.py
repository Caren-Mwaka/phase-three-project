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

  
    machines_data = [
        {"name": "Lathe Machine", "type": "Heavy-duty"},
        {"name": "CNC Milling Machine", "type": "Computer Numerical Control"},
        {"name": "Drilling Machine", "type": "Bench Type"},
        {"name": "Grinding Machine", "type": "Surface Grinder"},
        {"name": "Injection Molding Machine", "type": "Hydraulic"},
        {"name": "Press Machine", "type": "Mechanical"},
    ]

    for data in machines_data:
        machine = Machine.create(data["name"], data["type"])
