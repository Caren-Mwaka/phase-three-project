import sys
from database import CONN, CURSOR  # Importing database connection objects
from models import Machine, Part, MaintenanceRecord  # Importing models for database interaction

class CLI:
    def __init__(self):
        # Define commands for different menu options
        self.commands = {
            '1': self.machines_menu,
            '2': self.parts_menu,
            '3': self.maintenance_records_menu,
            'q': self.quit
        }

    def display_main_menu(self):
        # Displaying the main menu options
        print("\n*** Main Menu ***")
        print("1. Machines Menu")
        print("2. Parts Menu")
        print("3. Maintenance Records Menu")
        print("q. Quit")

    def run(self):
        # Main loop to run the CLI
        while True:
            self.display_main_menu()  # Display the main menu
            choice = input("Select an option: ").strip().lower()  # Get user choice
            if choice in self.commands:
                self.commands[choice]()  # Execute corresponding function for the choice
            else:
                print("Invalid option. Please choose again.")

    def machines_menu(self):
        # Menu for machine operations
        while True:
            print("\n*** Machines Menu ***")
            print("1. Create a Machine")
            print("2. Delete a Machine")
            print("3. Display all Machines")
            print("4. View Parts of a Machine")
            print("5. View Maintenance Records of a Machine")
            print("6. Find a Machine by ID")
            print("b. Back to Main Menu")
            choice = input("Select an option: ").strip().lower()
            
            # Execute corresponding function based on user choice
            if choice == '1':
                self.create_machine()
            elif choice == '2':
                self.delete_machine()
            elif choice == '3':
                self.display_all_machines()
            elif choice == '4':
                self.view_parts_of_machine()
            elif choice == '5':
                self.view_maintenance_records_of_machine()
            elif choice == '6':
                self.find_machine_by_id()
            elif choice == 'b':
                break
            else:
                print("Invalid option. Please choose again.")

  # methods to create a new machine(), delete_machine(), display_all_machines(),view_parts_of_machine(), view_maintenance_records_of_machine() and find_machine_by_id ()
    def create_machine(self):
      
        name = input("Enter machine name: ").strip()
        type = input("Enter machine type: ").strip()
        if name and type:
            Machine.create(name, type)  # Using the Machine model to create a new machine
            print("Machine created successfully.")
        else:
            print("Invalid input. Both name and type are required.")
    

    def delete_machine(self):
            machine_id = input("Enter machine ID to delete: ").strip()
            if machine_id.isdigit():
                machine_id = int(machine_id)
                machine = Machine.find_by_id(machine_id)
                if machine:
                    Machine.delete(machine_id)
                    print(f"Machine with ID {machine_id} deleted.")
                else:
                    print(f"No machine found with ID {machine_id}.")
            else:
                print("Invalid input. Machine ID must be a number.")

    def display_all_machines(self):
        machines = Machine.get_all()
        print("\n*** All Machines ***")
        for machine in machines:
            print(f"Machine ID: {machine['id']}, Name: {machine['name']}, Type: {machine['type']}")

    def view_parts_of_machine(self):
        machine_id = input("Enter machine ID to view parts: ").strip()
        if machine_id.isdigit():
            machine_id = int(machine_id)
            parts = Part.get_parts_by_machine(machine_id)
            print(f"\n*** Parts of Machine ID {machine_id} ***")
            for part in parts:
                print(f"Part ID: {part['id']}, Name: {part['name']}, Quantity: {part['quantity']}")

    def view_maintenance_records_of_machine(self):
        machine_id = input("Enter machine ID to view maintenance records: ").strip()
        if machine_id.isdigit():
            machine_id = int(machine_id)
            records = MaintenanceRecord.get_records_by_machine(machine_id)
            print(f"\n*** Maintenance Records of Machine ID {machine_id} ***")
            for record in records:
                print(record)
        else:
            print("Invalid input. Machine ID must be a number.")


    def find_machine_by_id(self):
        machine_id = input("Enter machine ID to find: ").strip()
        if machine_id.isdigit():
            machine_id = int(machine_id)
            machine = Machine.find_by_id(machine_id)
            if machine:
                print(machine)
            else:
                print(f"No machine found with ID {machine_id}.")
        else:
            print("Invalid input. Machine ID must be a number.")

    def parts_menu(self):
        # Menu for part operations
        while True:
            print("\n*** Parts Menu ***")
            print("1. Create a Part")
            print("2. Delete a Part")
            print("3. Display all Parts")
            print("4. Find a Part by ID")
            print("b. Back to Main Menu")
            choice = input("Select an option: ").strip().lower()
            
            # Executing corresponding function based on user choice
            if choice == '1':
                self.create_part()
            elif choice == '2':
                self.delete_part()
            elif choice == '3':
                self.display_all_parts()
            elif choice == '4':
                self.find_part_by_id()
            elif choice == 'b':
                break
            else:
                print("Invalid option. Please choose again.")

     # Methods for parts operations (create_part(), delete_part(), display_all_parts(), find_part_by_id())
    def create_part(self):
            name = input("Enter part name: ").strip()
            machine_id = input("Enter associated machine ID: ").strip()
            quantity = input("Enter quantity (default is 0): ").strip()
            if name and machine_id.isdigit():
                machine_id = int(machine_id)
                quantity = int(quantity) if quantity.isdigit() else 0
                Part.create(name, machine_id, quantity)
                print("Part created successfully.")
            else:
                print("Invalid input. Name must not be empty and machine ID must be a number.")

    def delete_part(self):
        part_id = input("Enter part ID to delete: ").strip()
        if part_id.isdigit():
            part_id = int(part_id)
            part = Part.find_by_id(part_id)
            if part:
                Part.delete(part_id)
                print(f"Part with ID {part_id} deleted.")
            else:
                print(f"No part found with ID {part_id}.")
        else:
            print("Invalid input. Part ID must be a number.")

    def display_all_parts(self):
            parts = Part.get_all()
            print("\n*** All Parts ***")
            for part in parts:
                print(f"Part ID: {part[0]}, Name: {part[1]}, Machine ID: {part[2]}, Quantity: {part[3]}")

    def find_part_by_id(self):
        part_id = input("Enter part ID to find: ").strip()
        if part_id.isdigit():
            part_id = int(part_id)
            part = Part.find_by_id(part_id)
            if part:
                print(part)
            else:
                print(f"No part found with ID {part_id}.")
        else:
            print("Invalid input. Part ID must be a number.")

    def maintenance_records_menu(self):
        # Menu for maintenance record operations
        while True:
            print("\n*** Maintenance Records Menu ***")
            print("1. Create a Maintenance Record")
            print("2. Delete a Maintenance Record")
            print("3. Display all Maintenance Records")
            print("4. Find a Maintenance Record by ID")
            print("b. Back to Main Menu")
            choice = input("Select an option: ").strip().lower()
            
            # Execute corresponding function based on user choice
            if choice == '1':
                self.create_maintenance_record()
            elif choice == '2':
                self.delete_maintenance_record()
            elif choice == '3':
                self.display_all_maintenance_records()
            elif choice == '4':
                self.find_maintenance_record_by_id()
            elif choice == 'b':
                break
            else:
                print("Invalid option. Please choose again.")

    # Methods for maintenance record operations (create_maintenance_record(), delete_maintenance_record(), display_all_maintenance_records(), find_maintenance_record_by_id())
    def create_maintenance_record(self):
        machine_id = input("Enter machine ID: ").strip()
        description = input("Enter maintenance description: ").strip()
        performed_at = input("Enter performed date/time (YYYY-MM-DD HH:MM): ").strip()
        if machine_id.isdigit() and description and performed_at:
            machine_id = int(machine_id)
            MaintenanceRecord.create(machine_id, description, performed_at)
            print("Maintenance record created successfully.")
        else:
            print("Invalid input. Machine ID must be a number, description and performed date/time are required.")

    def delete_maintenance_record(self):
        record_id = input("Enter maintenance record ID to delete: ").strip()
        if record_id.isdigit():
            record_id = int(record_id)
            record = MaintenanceRecord.find_by_id(record_id)
            if record:
                MaintenanceRecord.delete(record_id)
                print(f"Maintenance record with ID {record_id} deleted.")
            else:
                print(f"No maintenance record found with ID {record_id}.")
        else:
            print("Invalid input. Maintenance record ID must be a number.")

    def display_all_maintenance_records(self):
        records = MaintenanceRecord.get_all()
        print("\n*** All Maintenance Records ***")
        for record in records:
            print(record)

    def find_maintenance_record_by_id(self):
        record_id = input("Enter maintenance record ID to find: ").strip()
        if record_id.isdigit():
            record_id = int(record_id)
            record = MaintenanceRecord.find_by_id(record_id)
            if record:
                print(record)
            else:
                print(f"No maintenance record found with ID {record_id}.")
        else:
            print("Invalid input. Maintenance record ID must be a number.")

    def quit(self):
        # Function to quit the program
        print("Exiting program. Goodbye!")
        sys.exit(0)

# Entry point of the program
if __name__ == "__main__":
    cli = CLI()  # Creating an instance of CLI
    cli.run()  # Running the CLI