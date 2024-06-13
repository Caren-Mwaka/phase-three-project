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

     # Defining data for machines
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

    # Defining data for parts
    parts_data = [
        {"name": "Bolt", "machine_ids": [1, 2], "quantity": 100}, 
        {"name": "Nut", "machine_id": 1, "quantity": 100},
        {"name": "Screw", "machine_id": 2, "quantity": 75},
        {"name": "Washer", "machine_id": 2, "quantity": 200},
        {"name": "Drill Bit", "machine_id": 3, "quantity": 30},
        {"name": "Grinding Wheel", "machine_id": 4, "quantity": 15},
        {"name": "Hydraulic Pump", "machine_id": 5, "quantity": 3},
        {"name": "Mechanical Arm", "machine_id": 6, "quantity": 5},
        
    ]

    # Creating part instances and accounting for a situation where a part can be found in more than one machine
    for data in parts_data:
        if isinstance(data.get("machine_ids"), list): 
            for machine_id in data["machine_ids"]:
                part = Part.create(name=data["name"], machine_id=machine_id, quantity=data["quantity"])
        else:
            part = Part.create(name=data["name"], machine_id=data["machine_id"], quantity=data["quantity"])

    # Retrieving and printing parts used by each machine
    for machine in Machine.get_all():
        machine_id = machine[0]
        machine_name = machine[1]
        parts = Part.get_parts_by_machine(machine_id)
        part_names = [part[1] for part in parts]
        print(f"The parts used by {machine_name} (ID: {machine_id}) are: {', '.join(part_names)}")

    # Defining data for maintenance records
    maintenance_data = [
        {"machine_id": 1, "description": "Oil Change", "performed_at": "2023-01-01"},
        {"machine_id": 2, "description": "Calibration", "performed_at": "2023-02-01"},
        {"machine_id": 3, "description": "Inspection", "performed_at": "2023-03-01"},
        {"machine_id": 4, "description": "Belt Replacement", "performed_at": "2023-04-01"},
        {"machine_id": 5, "description": "Hydraulic Fluid Check", "performed_at": "2023-05-01"},
        {"machine_id": 6, "description": "Motor Check", "performed_at": "2023-06-01"},
        {"machine_id": 1, "description": "Cleaning", "performed_at": "2023-07-01"},  
        {"machine_id": 2, "description": "Lubrication", "performed_at": "2023-08-01"},  
       
    ]

    # Creating maintenance record instances
    for data in maintenance_data:
        maintenance_record = MaintenanceRecord.create(
            machine_id=data["machine_id"],
            description=data["description"],
            performed_at=data["performed_at"]
        )

    # Retrieving and printing maintenance records for each machine
    for machine in Machine.get_all():
        machine_id = machine[0]
        machine_name = machine[1]
        records = MaintenanceRecord.get_records_by_machine(machine_id)
        record_descriptions = [record.description for record in records]
        print(f"The maintenance records for {machine_name} (ID: {machine_id}) are: {', '.join(record_descriptions)}")

      # Updating a machine
    machine = Machine.find_by_id(2)
    if machine:
        machine_instance = Machine(machine['name'], machine['type'])
        machine_instance.id = machine['id']
        machine_instance.update(name="New Lathe Machine")

    # Updating a part
    part = Part.find_by_id(1)
    if part:
        part_instance = Part(part['name'], part['machine_id'], part['quantity'])
        part_instance.id = part['id']
        part_instance.update(name="New Bolt", quantity=150)

    # Updating a maintenance record
    record = MaintenanceRecord.find_by_id(1)
    if record:
        record_instance = MaintenanceRecord(record.machine_id, record.description, record.performed_at)
        record_instance.id = record.id
        record_instance.update(description="New Oil Change", performed_at="2023-01-15")


    # # Delete functionality
    # machine_to_delete = Machine.find_by_id(1)  
    # if machine_to_delete:
    #     machine_instance = Machine(machine_to_delete['name'], machine_to_delete['type'])
    #     machine_instance.id = machine_to_delete['id']
    #     machine_instance.delete()
    #     print(f"Machine with ID 1 has been deleted.")
