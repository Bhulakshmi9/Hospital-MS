# Hospital Management System
A small project created for the CSC785: Info Storage & Retrieval master's course. 


# Prerequisites
Prerequisites for this project include Python, Pycharm and MySQL Server.

https://www.python.org/downloads/

https://www.jetbrains.com/pycharm/download/

https://www.mysql.com/downloads/

# Project Objectives

### A.) Properties of all relations
Relations in this database include:

#### Patient
Details on patients in the hospital, including:
 - Patient ID
 - first name
 - last name
 - birthday
 - gender
 - email
 - phone number
 - height
 - weight
 - address
 - SSN

#### Doctor 
Details on doctors in the hospital, including:
 - Doctor ID
 - first name
 - last name
 - birthday
 - gender
 - email
 - phone number
 - height
 - weight
 - address
 - hospital name
 - consultation cost

#### Staff
Details on all other staff in the hospital (such as nurses and ward boys), including:
 - Staff ID
 - first name
 - last name
 - birthday
 - gender
 - email
 - phone number
 - address
 - type (nurse, ward boy, etc.)
 - duties

#### Room
Details on all rooms in the hospital, including:
 - Room ID
 - name
 - type (ICU, Operating Theater, etc.)
 - description
 - hospital name
 - room cost

#### RoomAssignments
Junction table for assigning staff to rooms:
  - Staff ID
  - Room ID

#### Disease
Details on diseases, including:
 - Disease ID
 - name
 - description
 - symptoms
 - death rate

#### Treatment
Details on treatments for diseases, including:
 - Treatment ID
 - name
 - description
 - treatment cost
 - Disease ID

#### Appointment
Appointments made between doctors and patients:
 - Appointment ID
 - Patient ID
 - Doctor ID
 - Disease ID
 - Room ID
 - start date
 - end date

#### Bill
Details on appointment bill, including:
 - Bill ID
 - Appointment ID
 - Disease ID
 - amount

### B.)

# Team
Vijnathi Katamaneni

Malan Moody

Bruce Stofft

Harish Babu

Bhulakshmi Kunchala