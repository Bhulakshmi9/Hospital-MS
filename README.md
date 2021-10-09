# Hospital Management System
A small project created for the CSC785: Info Storage & Retrieval master's course. 

# ER Diagram

![alt text](https://github.com/Vijnathi/Hospital-Management-System/blob/master/HMS-Final-ER.png)

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

Attribute | Null? | Keys | Others | Datatypes| Description
--- | --- | --- | --- |--- |---
patientID | Not Null | Primary Key | Auto Increment | Int | Unique ID of a Patient 
firstName | Not Null |  |  |Varchar | First Name of a Patient  
lastName | Not Null |  |  |Varchar| Last Name of a Patient
birthDate | Not Null |  |  |Varchar| Patient's Birth Date
gender | Not Null |  |  |Varchar| Patient's Gender
email | Not Null |  |unique |Varchar| Patient's Email
phoneNumber | Not Null |  |  | Varchar | Patient's Phone Number
height |  |  |  |float| Patient's Height
weight |  |  |  | float| Patient's Weight
address | Not Null |  |  | Varchar| Patient's Address
SSN | Not Null |  |  |Varchar| SSN of a patient

#### Staff
Details on staff in the hospital, including:

Attribute | Null? | Keys | Others |Datatypes| Description
--- | --- | --- | --- |--- |---
staffID|Not Null|Primary Key|  Auto Increment|  Int|Staff's unique Id
firstName|Not Null|    |  |Varchar|Staff's First Name
lastName|  Not Null       |      |       |Varchar|Staff's Last Name
birthDate|  Not Null|  |  |Varchar|Staff's Birth Date
gender|  Not Null| | |Varchar|Staff's Gender
email|  Not Null  |      |unique|  Varchar|Staff's Email Id
phoneNumber|  Not Null| ||Varchar  |Staff's Phone Number
address|  Not Null|  | |Varchar|Staff;s Address
SSN |  Not Null|       |         |Varchar|Staff's  Ssn
type|  Not Null|  |           |Varchar|Staff Type
duties|  |     |      |Varchar|Staff's Duties


#### Doctor
Details on Doctors in the hospital, including:
 
 Attribute | Null? | Keys | Others |Datatypes| Description
--- | --- | --- | --- |--- |---
doctorID |Not Null|Primary Key  |    Auto Increment|  Int|Doctor's Unique Id
firstName|  Not Null|  |             |Varchar|Doctor's First Name
lastName|  Not Null|        |      |Varchar|Doctor's Last Name
birthDate|  Not Null|    |   |  Varchar|Doctor's Birth Date 
gender|  Not Null|       |        |Varchar|Doctor's Gender
email|  Not Null |       |unique|  Varchar|Doctor's email Id
phoneNumber  |Not Null|         |       |Varchar|Doctor's Phone Number
weight|         |         |  |float|Doctor's Weight
heigt|          |  |     |  float|Doctor's Height 
address  |Not Null  |     |   |Varchar|Doctor;s Address
hospitalName|       |       |         |Varchar|Name of The Hospital     
consultationCost|  Not Null|       |         |Varchar|Cost For Consultation  


#### Room
Details on Rooms in the hospital, including:

Attribute | Null? | Keys | Others |Datatypes| Description
--- | --- | --- | --- |--- |---
roomID|  Not Null|  Primary Key|  Auto Increment|  Int|Unique Id of a Roomm 
roomName|  Not Null|         |     |  Varchar|Name of The Room
type|  Not Null|       |       |  Varchar|Type Of The Room
roomDescription|        |     |       |  Varchar|Description Of The Room
hospitalName|         |       |     |  Varchar|Name Of The Hospital
roomCost|  Not Null|        |       |Varchar|Cost Of The Room


Attribute | Null? | Keys | Others |Datatypes| Description
--- | --- | --- | --- |--- |---
staffID|  NOT NULL|  Primary Key,FOREIGN KEY|        |Int|Id For Staff
roomID|  NOT NULL|  Primary Key,FOREIGN KEY|        |Int|Id For Room 

#### Disease
Details on diseasess in the hospital, including:

Attribute | Null? | Keys | Others |Datatypes| Description
--- | --- | --- | --- |--- |---
diseaseID|  NOT NULL| Primary Key| Auto Increment  |Int|Unique Id Of Disease
diseaseName|  NOT NULL|  |       |  Varchar|Name Of The Disease
diseaseDescription|  |            |  |Varchar|  Description For Disease   
symptoms|  |      |  |Varchar|Symptom's Of Disease
deathRate |  |         |  |Varchar|Death Rate OF Disease


#### Treatment
Details on Treatment in the hospital, including:

Attribute | Null? | Keys | Others |Datatypes| Description
--- | --- | --- | --- |--- |---
treatmentID|NOT NULL|  Primary Key|  Auto Increment|  Int|unique Id of a Treatment
treatmentName |  NOT NULL|    |      |Varchar|Treatment's Name
treatmentDescription|  NULL|        |       |Varchar|Description For Treatment
treatmentCost|  NULL|       |  |Varchar|Treatment;s Cost
diseaseID|    |Foreign Key|    |Varchar|Treatment's Disease Id


### Appointment
Details on Appointment in the hospital, including:

Attribute | Null? | Keys | Others |Datatypes| Description
--- | --- | --- | --- |--- |---
appointmentID| NOT NULL|  Primary Key|  Auto Increment|  Int|Unique Id Of Appointment
patientID|  NOT NUL| Foreign Key|         |Int|Id For Patient
doctorID | NOT NUL|  Foreign Key |         |Int|Id For Doctor
diseaseID|  NOT NULL | Foreign Key|    |Int|Id For Disease    
roomID|      |  Foreign Key|         |Int|Id For Room
type|  NOT NUL|            |  |Varchar|Type Of Appointment
startDate|  NOT NUL|         |     |Date |  Appointment Start Date   
endDate|    |     |  | Date  | Appointment End Date  

#### Bill
Details on Billss in the hospital, including:

Attribute | Null? | Keys | Others | Datatypes | Description
--- | --- | --- | --- |--- |---
billID | NOT NULL | Primary Key | Auto Increment | Int | Unique ID of a Bill 
appointmentID | NOT NULL | Foreign Key |  | Int |Id For Appointment     
patientID | NOT NULL | Foreign Key |  | Int | Id For patient 
diseaseID | NOT NULL | Foreign Key |  | Int | Id For Disease 
Amount |  |  |  | Float | Total Cost For Treatment And Number Of Days


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

 1. Click 'Admin'
 2. Click 'Manage'
 3. Click 'Manage Tables'
 4. Select the Patient table
 5. Enter the Patient ID of the patient you wish to change and click 'Update'
 6. Enter the new height and weight for the patient and click 'Update'

sql = "Update Patient SET height = %s, weight = %s WHERE patientID = %s" % (height, weight, pid)

try:
 cursor.execute(sql)

### J.) Drop specific columns and rows
To drop rows:
 1. Click 'Admin'
 2. Click 'Manage'
 3. Click 'Manage Tables'
 4. Select the Room table
 5. Enter the Room ID of the room you wish to delete and click 'Delete'

sql = "DELETE FROM Room WHERE roomID = %s" % rid

try:
 cursor.execute(sql)

To drop columns:
 1. Click 'Admin'
 2. Click 'Manage'
 3. Click 'Delete Column'
 4. Click 'Go Ahead' to delete the hospital name column from the Room table

cursor.execute("ALTER TABLE Room DROP COLUMN hospitalName")

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
