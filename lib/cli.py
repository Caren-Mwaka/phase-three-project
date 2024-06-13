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
