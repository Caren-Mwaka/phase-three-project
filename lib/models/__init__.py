# To initialize the models folder as a package I added the "init" file. 
# This allows Python to recognize models as a module that can be imported.
from models.machines import Machine
from models.parts import Part
from models.maintenance_records import MaintenanceRecord