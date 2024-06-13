import sys
from database import CONN, CURSOR  # Importing database connection objects
from models import Machine, Part, MaintenanceRecord  # Importing models for database interaction

class CLI:
    def __init__(self):
        # Defining the commands for different menu options
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
            choice = input("Select an option: ").strip().lower()  # Getting user choice
            if choice in self.commands:
                self.commands[choice]()  # Executing corresponding function for the choice
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
            
            # Executing corresponding function based on user choice
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