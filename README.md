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

### B.) Select specific rows and columns

 1. Click 'User'
 2. Enter login info and log in
 3. Click 'View Patient Contact Info'
 4. Enter ID of patient you are searching for

sql = "SELECT concat(firstName, ' ', lastName) as fullName, email, phoneNumber FROM Patient WHERE patientID = %s" % ID

curr.execute(sql)

### C.) Apply search conditions with calculated fields

 1. Click 'User'
 2. Enter login info and log in
 3. Click 'View Patients Above Age'
 4. Enter age to get details on all patients above that age

sql = "SELECT concat(firstname, ' ', lastname) as FullName, TIMESTAMPDIFF(YEAR, birthDate, CURDATE()) AS age FROM Patient Having age > %s Order by age" % age

curr.execute(sql)

### D.) Use pattern search

 1. Click 'User'
 2. Enter login info and log in
 3. Click 'View Patient Contact Info'
 4. Enter part of first or last name to pattern search the names of patients

sql = "SELECT concat(firstName, ' ', lastName) as fullName, email, phoneNumber FROM Patient WHERE LOWER(firstName) LIKE '%" + fname.lower() + "%'"

curr.execute(sql)

### E.) Select tuples based on ordering

 1. Click 'Admin'
 2. Click 'Manage'
 3. Click 'Manage Treatments'
 4. Click 'View Treatments By Order'

sql = "SELECT treatmentName, treatmentDescription, treatmentCost, diseaseName, deathRate FROM Treatment t, Disease d WHERE t.diseaseID = d.diseaseID ORDER BY treatmentCost ASC, deathRate DESC;"
    
cursor.execute(sql)

### F.) Use nested queries

 1. Click 'User'
 2. Enter login info and log in
 3. Click 'View Staff by Room'
 4. Enter the room number to view staff assigned to that room

sql = "SELECT concat(firstName, ' ', lastName) as fullName, email, phoneNumber FROM Staff WHERE staffID IN (SELECT staffID FROM RoomAssignments WHERE roomID = %s)" % num

self.cursor.execute(sql)

### G.) Use aggregated functions

 1. Click 'Admin'
 2. Click 'Manage'
 3. Click 'View Number of Records in each table'

sql = "SELECT COUNT(*), 'Patient' as type from Patient;" \
      "SELECT COUNT(*), 'Doctor' as type from Doctor;" \
      "SELECT COUNT(*), 'Staff' as type from Staff;" \
      "SELECT COUNT(*), 'Disease' as type from Disease;" \
      "SELECT COUNT(*), 'Treatment' as type from Treatment;" \     
      "SELECT COUNT(*), 'Room' as type from Room;" \     
      "SELECT COUNT(*), 'RoomAss' as type from RoomAssignments;" \
      "SELECT COUNT(*), 'Appointment' as type from Appointment;" \
      "SELECT COUNT(*), 'Bill' as type from Bill;"
      
results = cursor.execute(sql, multi=True)

### H.) Take multiple relations in a query

 1. Click 'User'
 2. Enter login info and log in
 3. Click 'View Appointments'

sql = "SELECT concat(firstName, ' ', lastName) as fullName, p.email, p.phoneNumber, d.diseaseName, t.treatmentName, r.roomID, r.roomName, a.startDate " \
      "FROM Appointment a " \
      "JOIN Patient p  ON p.patientID  = a.patientID " \
      "JOIN Disease d ON d.diseaseID = a.diseaseID " \
      "JOIN Treatment t ON d.diseaseID = t.diseaseID " \
      "JOIN Room r ON r.roomID = a.roomID WHERE (a.type = 'outpatient' and startDate >= %s) or " \
      "(a.type = 'inpatient' and endDate is NULL and startDate >= %s)" % ("'"+date+"'", "'"+date+"'")

self.cursor.execute(sql)

### I.) Update specific columns and/or fields



### J.) Drop specific columns and rows



### K.) Create users and provide different views

 1. Click 'Admin'
 2. Click 'Aministration'
 3. Click 'Add New User'
 4. Enter login info for the new user

sql = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (username, password)

cursor.execute(sql)

### L.) Grant priveleges for specific users

 1. Click 'Admin'
 2. Click 'Aministration'
 3. Click 'Grant Permissions'
 4. Enter the user name of the user and select all priveleges to grant them

sql = "GRANT %s ON HospitalManagementSystem.%s TO '%s'@'localhost'" % (permissions, table, username)

cursor.execute(sql)

### M.) Backup the database



### N.) Import backed-up database



# Team
Vijnathi Katamaneni

Malan Moody

Bruce Stofft

Harish Babu

Bhulakshmi Kunchala
