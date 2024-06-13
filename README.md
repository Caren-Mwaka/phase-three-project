# Phase 3 CLI Project Template

## Title: Part Manager Application 

## Description:

The Part Manager application is a simple yet powerful tool built for efficiently managing machines and their associated parts particularly in mechanical engineering. With its intuitive command-line interface, users can effortlessly perform CRUD (Create, Read, Update, Delete) operations on machines and parts, ensuring smooth and organized maintenance workflows.

## Features:

Machine Management: Create, view, update, and delete machines seamlessly. Keep track of essential machine details such as name and type.

Part Management: Manage parts effortlessly by adding, editing, and deleting them as needed. Track part quantities and their associated machines.

Maintenance Record Tracking: Stay organized by adding maintenance records to machines. Each maintenance record includes a description of the maintenance performed, providing valuable insights into machine maintenance history.

Database Persistence: Utilizes SQLite for database management, ensuring data integrity and persistence across sessions.

User-Friendly CLI: Offers a straightforward command-line interface that makes navigation and interaction intuitive for users of all skill levels.

## DB diagram:
Table machines {
  id int [pk, increment]
  name varchar
  type varchar
}

Table parts {
  id int [pk, increment]
  name varchar
  machine_id int [ref: > machines.id]
  quantity int
}

Table maintenance_records {
  id int [pk, increment]
  machine_id int [ref: > machines.id]
  description text
  performed_at varchar
}

Ref: parts.machine_id > machines.id // many-to-one
Ref: maintenance_records.machine_id > machines.id // many-to-one

## Machine to Part Relationship (One-to-Many)

Each machine can have multiple parts.
The Part class has a foreign key machine_id referencing the Machine class.
In the Machine class, the method get_parts_by_machine(machine_id) retrieves all parts related to a machine.
Machine to MaintenanceRecord Relationship (One-to-Many)

Each machine can have multiple maintenance records.
The MaintenanceRecord class has a foreign key machine_id referencing the Machine class.
In the Machine class, the method get_maintenance_records_by_machine(machine_id) retrieves all maintenance records related to a machine.


## Purpose:

The Part Manager application is designed to simplify the process of managing machines and parts, particularly in small-scale engineering environments. It allows users to easily organize and track machines and parts, reducing manual effort and minimizing errors in inventory management.

Target Audience:

The target audience for this application includes engineers, technicians, and anyone involved in the maintenance and operation of machinery. It is suitable for both individual users and small teams looking for a lightweight solution for managing their equipment and parts inventory.

## Future Enhancements:

Future enhancements to the Part Manager application could include:

Adding support for additional attributes for machines and parts, such as serial numbers, purchase dates, etc.
Implementing authentication and user roles to restrict access to sensitive operations.
Developing a graphical user interface (GUI) for a more visually appealing and user-friendly experience.
Integrating with external APIs or services for advanced features such as automated inventory tracking or alerts for low stock levels.
Conclusion:

The Part Manager application offers a straightforward solution for managing machines and parts, providing essential features for organizing and tracking inventory. With its simple interface and database-backed design, it offers convenience and efficiency for users involved in machinery maintenance and operations.

## Installation
You can use git clone to download the repository from GitHub.

## Installation Requirements
Git
Python 3.x
SQLite3

## Access
Git clone https://github.com/Caren-Mwaka/phase-three-project.git

## Support and contact details
github.com/Caren-Mwaka

### License
The content of this site is licensed under the MIT license
Copyright (c) 2024.


