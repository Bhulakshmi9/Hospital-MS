import mysql.connector
import credentials
# global cursor
# global conn

# def connect():
# establishing the connection
conn = mysql.connector.connect(user='root', password=credentials.PASSWORD, host='127.0.0.1', auth_plugin='mysql_native_password')
# Creating a cursor object using the cursor() method
cursor = conn.cursor()


def create():
    # Doping database MYDATABASE if already exists.
    cursor.execute("DROP database IF EXISTS HospitalManagementSystem")
    # Preparing query to create a database
    sql = "CREATE database HospitalManagementSystem"
    # Creating a database
    cursor.execute(sql)
    cursor.execute("Use HospitalManagementSystem")

    # Dropping Staff table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Staff")
    # create table staff
    staff_sql = 'CREATE TABLE Staff(staffID INT NOT NULL AUTO_INCREMENT, firstName VARCHAR(20) NOT NULL, ' \
                'lastName VARCHAR(20) NOT NULL, birthDate DATE NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(100) NOT NULL, ' \
                'phoneNumber VARCHAR(15) NOT NULL, address VARCHAR(200) NOT NULL, SSN varchar(11) NOT NULL, type VARCHAR(15) NOT NULL, duties VARCHAR(255), ' \
                'PRIMARY KEY (staffID), UNIQUE(email))'
    cursor.execute(staff_sql)

    # Dropping Patient table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Patient")
    # Creating table Patient
    patient_sql = 'CREATE TABLE Patient(patientID INT NOT NULL AUTO_INCREMENT, firstName VARCHAR(20) NOT NULL, ' \
                  'lastName VARCHAR(20) NOT NULL, birthDate DATE NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(100) NOT NULL, ' \
                  'phoneNumber VARCHAR(15) NOT NULL, height float, weight float, address VARCHAR(200) NOT NULL, SSN varchar(11) NOT NULL,' \
                  'PRIMARY KEY (patientID), UNIQUE(email))'
    cursor.execute(patient_sql)

    # Dropping Doctor table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Doctor")

    # Creating table Doctor
    doctor_sql = 'CREATE TABLE Doctor(doctorID INT NOT NULL AUTO_INCREMENT, firstName VARCHAR(20) NOT NULL, ' \
                 'lastName VARCHAR(20) NOT NULL, birthDate DATE NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(100) NOT NULL, ' \
                 'phoneNumber VARCHAR(12) NOT NULL, weight float, height float, address VARCHAR(255) NOT NULL, hospitalName VARCHAR(100), ' \
                 'consultationCost DECIMAL(13,2) NOT NULL, PRIMARY KEY (doctorID), UNIQUE(email))'
    cursor.execute(doctor_sql)

    # Dropping table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Room")

    # Creating table as per requirement
    room_sql = 'CREATE TABLE Room(roomID INT NOT NULL AUTO_INCREMENT, roomName VARCHAR(50) NOT NULL, type VARCHAR(20) NOT NULL, ' \
               'roomDescription VARCHAR(255), hospitalName VARCHAR(100), roomCost DECIMAL(13,2) NOT NULL, PRIMARY KEY (roomID))'
    cursor.execute(room_sql)

    # Dropping RoomAssignments table if already exists.
    cursor.execute("DROP TABLE IF EXISTS RoomAssignments")

    # Creating table RoomAssignment
    room_ass_sql = 'CREATE TABLE RoomAssignments(staffID INT NOT NULL, roomID INT NOT NULL, PRIMARY KEY (staffID, roomID), ' \
                   'FOREIGN KEY (staffID) REFERENCES Staff(staffID), FOREIGN KEY (roomID) REFERENCES Room(roomID))'
    cursor.execute(room_ass_sql)

    # Dropping Disease table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Disease")
    disease_sql = 'CREATE TABLE Disease(diseaseID INT NOT NULL AUTO_INCREMENT, diseaseName VARCHAR(50) NOT NULL, ' \
                  'diseaseDescription VARCHAR(255), symptoms VARCHAR(255) NOT NULL, deathRate VARCHAR(45), ' \
                  'PRIMARY KEY (diseaseID))'
    cursor.execute(disease_sql)

    # Dropping Treatment table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Treatment")
    treatment_sql = 'CREATE TABLE Treatment (treatmentID INT NOT NULL AUTO_INCREMENT,treatmentName VARCHAR(50) NOT NULL, ' \
                    'treatmentDescription VARCHAR(255) NULL, treatmentCost decimal(13,2) NULL, diseaseID int, ' \
                    'PRIMARY KEY (treatmentID), FOREIGN KEY (diseaseID) REFERENCES Disease(diseaseID))'
    cursor.execute(treatment_sql)

    # Dropping Appointment table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Appointment")
    appointment_sql = 'CREATE TABLE Appointment(appointmentID INT NOT NULL AUTO_INCREMENT, patientID INT NOT NULL, ' \
                      'doctorID INT NOT NULL, diseaseID INT NOT NULL, roomID INT, type VARCHAR(15) NOT NULL, startDate DATE NOT NULL, ' \
                      'endDate DATE, PRIMARY KEY (appointmentID), FOREIGN KEY (patientID) REFERENCES Patient(patientID), ' \
                      'FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID), FOREIGN KEY (diseaseID) REFERENCES Disease(diseaseID), ' \
                      'FOREIGN KEY (roomID) REFERENCES Room(roomID))'
    cursor.execute(appointment_sql)

    # # Dropping Bill table if already exists.
    cursor.execute("DROP TABLE IF EXISTS Bill")
    bill_sql = 'CREATE TABLE Bill(billID INT NOT NULL AUTO_INCREMENT, appointmentID INT NOT NULL, ' \
               'diseaseID INT NOT NULL, amount float, PRIMARY KEY (billID), ' \
               'FOREIGN KEY (appointmentID) REFERENCES Appointment(appointmentID), ' \
               'FOREIGN KEY (diseaseID) REFERENCES Disease(diseaseID))'
    cursor.execute(bill_sql)

    # # Dropping OutPatientAppointment table if already exists.
    # cursor.execute("DROP TABLE IF EXISTS OutPatientAppointment")
    # outpatient_sql = 'CREATE TABLE OutPatientAppointment(OutPatientAppID VARCHAR(20) NOT NULL, patientID INT NOT NULL, ' \
    #                  'doctorID INT NOT NULL, diseaseID INT NOT NULL, appDate DATE NOT NULL, ' \
    #                  'PRIMARY KEY (OutPatientAppID), FOREIGN KEY (patientID) REFERENCES Patient(patientID), ' \
    #                  'FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID), FOREIGN KEY (diseaseID) REFERENCES Disease(diseaseID))'
    # cursor.execute(outpatient_sql)
    #
    # # Dropping INPatientAppointment table if already exists.
    # cursor.execute("DROP TABLE IF EXISTS INPatientAppointment")
    # inpatient_sql = 'CREATE TABLE INPatientAppointment(InPatientAppID VARCHAR(20) NOT NULL, patientID INT NOT NULL, ' \
    #                 'doctorID INT NOT NULL, diseaseID INT NOT NULL, roomID INT NOT NULL, startDate DATE NOT NULL, ' \
    #                 'endDate DATE, PRIMARY KEY (InPatientAppID), FOREIGN KEY (patientID) REFERENCES Patient(patientID), ' \
    #                 'FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID), FOREIGN KEY (diseaseID) REFERENCES Disease(diseaseID), ' \
    #                 'FOREIGN KEY (roomID) REFERENCES Room(roomID))'
    # cursor.execute(inpatient_sql)
    insert()


def insert():
    # insert rows to staff
    staff_insert_stmt = "INSERT INTO Staff (firstName, lastName, birthDate, gender, email, phoneNumber, address, SSN, type, duties) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    staff_data = [
        ('Jerry', 'Jones', '1965-05-01', 'male', 'JJ1965@gmail.com', '305-911-8765', '14 Cherry St',
         '765-93-3324', 'ward boy', 'custodian'),
        ('Elizabeth', 'Ratchet', '1970-01-15', 'female', 'NurseR@yahoo.com', '410-556-1577',
         '198 Pine St', '542-19-4392', 'nurse', 'ER nurse'),
        ('Barry', 'Cosby', '1989-06-18', 'male', 'bc1989@gmail.com', '712-827-2141',
         '1701 Starfleet Dr', '612-26-1863', 'ward boy', 'custodian'),
        ('Margret', 'Perryman', '1992-02-09', 'female', '1992MP@yahoo.com', '545-989-2165',
         '11 Sycamore Drive', '293-55-2819', 'nurse', 'Travel nurse'),
        ('Nacy', 'Spungeon', '1966-08-18', 'female', 'BadNewsNurse@aol.com', '212-827-8826',
         '81 Sidney Lane', '236-82-1392', 'nurse', 'Shift nurse')
    ]

    patient_insert_stmt = "INSERT INTO Patient (firstName, lastName, birthDate, gender, email, phoneNumber, height, weight, address, SSN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    patient_data = [('Mike', 'Smith', '1980-02-12', 'male', 'mike.smith@gmail.com', '212-986-1314', 68, 180,
                     '123 Main St', '206-55-1024'),
                    ('Mary', 'Jones', '1976-04-22', 'female', 'mjones@yahoo.com', '454-123-1812', 60, 105,
                     '2788 Elm St',
                     '454-78-6598'),
                    ('Duey', 'Cox', '1958-02-14', 'male', 'dcox@gmail.com', '703-376-2554', 74, 255,
                     '1313 Mockingbird Lane', '667-42-7412'),
                    ('Meg', 'Griffin', '1989-01-01', 'female', 'MGriffin66@yahoo.com', '605-342-6529', 63, 133,
                     '28 Spruce Drive', '382-99-4658'),
                    ('Elvis', 'Myers', '1982-12-31', 'male', 'FatBoySlim@compuserve.com', '778-965-4215', 74, 239,
                     '2 Redwood Place', '956-43-1614'),
                    ('Dummy', 'Entry', '1982-01-31', 'male', 'DummyEntry@compuserve.com', '778-963-3315', 70, 230,
                     '1 Redwood Place', '956-23-1714')
                    ]

    doctor_insert_stmt = "INSERT INTO Doctor (firstName, lastName, birthDate, gender, email, phoneNumber, weight, height, address, hospitalName, consultationCost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    doctor_data = [('Braylen', 'Stern', '1989-03-15', 'female', 'braylen.stern@gmail.com', '445-646-4268', 120, 68,
                    '123 1st St', 'Test Hospital', 500.00),
                   ('Mitra', 'Holland', '1978-08-04', 'female', 'mholland@yahoo.com', '856-152-6256', 105, 64,
                    '321 1st St',
                    'Test Hospital', 600.00),
                   ('Sneha', 'Miyake', '1990-12-21', 'male', 'snehamiyake@gmail.com', '256-958-6352', 150, 70,
                       '555 41st St',
                       'Test Hospital', 400.00),
                   ('Amit', 'Moses', '1000-01-01', 'male', 'Amit@yahoo.com', '145-857-9431', 100, 60,
                    '111 Fake Address Rd',
                    'Test Hospital', 111111111.11),
                   ('Vaiva', 'Mcalister', '9999-12-31', 'female', 'new_email@gmail.com', '778-965-4215', 999, 99,
                    '999 Fake Address Rd', 'Test Hospital', 999999999.99)
                   ]
    room_insert_stmt = "INSERT INTO Room (roomID, roomName, type, roomDescription, hospitalName, roomCost) VALUES (%s, %s, %s, %s, %s, %s)"
    room_data = [(101, 'The Ward', 'Ward', 'It\'s the Ward', 'Test Hospital', 100.00),
                 (102, 'Jerry', 'ICU', 'Intensive care unit', 'Test Hospital', 250.00),
                 (103, 'RoomName?', 'Operating Theater', 'Operations happen here', 'Test Hospital', 1000.00),
                 (104, 'DummyEntry', 'DummyRoom', 'Will use it to delete', 'Dummy Hospital', 0.0)]
    #
    room_ass_insert_stmt = "INSERT INTO RoomAssignments (staffID, roomID) VALUES (%s, %s)"
    room_ass_data = [(1, 101),
                     (4, 101),
                     (5, 101),
                     (1, 102),
                     (2, 102),
                     (3, 103)
                     ]
    #
    disease_insert_stmt = "INSERT INTO Disease (diseaseName, diseaseDescription, symptoms, deathRate) VALUES (%s, %s, %s, %s)"
    disease_data = [('none', 'patient shows no signs of illness', 'none', 0),
                    ('Flu', 'patient has influenza', 'fever, cough', 0.0005),
                    ('Covid', 'patient has covid-19', 'fever, sore muscles, loss of taste', 0.02),
                    ('test', 'dummy entry', 'test', 1)
                    ]

    treatment_insert_stmt = "INSERT INTO Treatment (treatmentName, treatmentDescription, treatmentCost, diseaseID) VALUES (%s, %s, %s, %s)"
    treatment_data = [('none', 'no treatment', 0.00, 1),
                      ('ibuprofen', 'common anti-inflammatory', 10.00, 2),
                      ('remdesivir', 'antiviral for treating covid', 100.00, 3),
                      ('test', 'dummy entry', 999.99, 4)
                      ]

    app_insert_stmt = "INSERT INTO Appointment (patientID, doctorID, diseaseID, roomID, type, startDate, endDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    app_data = [(1, 1, 1, None, 'outpatient', '2021-10-01', None),
                (2, 2, 2, 101, 'inpatient', '2021-10-05', None),
                (3, 4, 3, 102, 'inpatient', '2021-09-15', '2021-09-30'),
                (4, 1, 1, None, 'outpatient', '2021-10-03', None),
                (5, 5, 4, 103, 'inpatient', '1000-01-01', '9999-12-31')
                ]
    #
    bill_insert_stmt = "INSERT INTO Bill (appointmentID, diseaseID, amount) VALUES (%s, %s, %s)"
    bill_data = [(1, 1, 20.00),
                 (2, 3, 50.00),
                 (3, 2, 200.50),
                 (5, 3, 999.99)
                 ]

    try:
        # Executing the SQL command
        cursor.executemany(staff_insert_stmt, staff_data)
        cursor.executemany(patient_insert_stmt, patient_data)
        cursor.executemany(doctor_insert_stmt, doctor_data)
        cursor.executemany(room_insert_stmt, room_data)
        cursor.executemany(room_ass_insert_stmt, room_ass_data)
        cursor.executemany(disease_insert_stmt, disease_data)
        cursor.executemany(treatment_insert_stmt, treatment_data)
        cursor.executemany(app_insert_stmt, app_data)
        cursor.executemany(bill_insert_stmt, bill_data)
        # Commit your changes in the database
        conn.commit()
    except Exception as Ex:
        print(Ex)
        # Rolling back in case of error
        # conn.rollback()

    close()

# Retrieving the list of databases
# print("List of databases: ")
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())
# Closing the connection
def close():
    conn.close()
