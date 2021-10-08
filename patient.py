import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='HospitalManagementSystem')
# Creating a cursor object using the cursor() method
cursor = conn.cursor()


def view_all():
    sql = "SELECT * FROM Patient"
    cursor.execute(sql)
    return cursor.fetchall()


def view_by_id(p_id):
    sql = "SELECT * FROM Patient WHERE patientID = " + p_id
    cursor.execute(sql)
    return cursor.fetchone()


def view_by_email(email):
    sql = "SELECT * FROM Patient WHERE LOWER(email) LIKE %" + email + "%"
    cursor.execute(sql)
    return cursor.fetchall()


def get_contact_info_by_fname(username, password, fname):
    con = mysql.connector.connect(user=username, password=password, host='127.0.0.1',
                                  database='HospitalManagementSystem')
    # Creating a cursor object using the cursor() method
    curr = con.cursor()
    try:
        sql = "SELECT concat(firstName, ' ', lastName) as fullName, email, phoneNumber FROM Patient WHERE LOWER(firstName) LIKE '%" + fname.lower() + "%'"
        curr.execute(sql)
        return curr.fetchall(), 'success'
    except Exception as Ex:
        print("Error:", Ex)
        return [], 'error'


def get_contact_info_by_lname(username, password, lname):
    con = mysql.connector.connect(user=username, password=password, host='127.0.0.1',
                                  database='HospitalManagementSystem')
    # Creating a cursor object using the cursor() method
    curr = con.cursor()
    try:
        sql = "SELECT concat(firstName, ' ', lastName) as fullName, email, phoneNumber FROM Patient WHERE LOWER(lastName) LIKE '%" + lname.lower() + "%'"
        curr.execute(sql)
        return curr.fetchall(), 'success'
    except Exception as Ex:
        print("Error:", Ex)
        return [], 'error'


def get_contact_info_by_id(username, password, ID):
    con = mysql.connector.connect(user=username, password=password, host='127.0.0.1',
                                  database='HospitalManagementSystem')
    # Creating a cursor object using the cursor() method
    curr = con.cursor()
    try:
        sql = "SELECT concat(firstName, ' ', lastName) as fullName, email, phoneNumber FROM Patient WHERE patientID = %s" % ID
        curr.execute(sql)
        return curr.fetchall(), 'success'
    except Exception as Ex:
        print("Error:", Ex)
        return [], 'error'


def get_patients_above_age(username, password, age):
    con = mysql.connector.connect(user=username, password=password, host='127.0.0.1',
                                  database='HospitalManagementSystem')
    # Creating a cursor object using the cursor() method
    curr = con.cursor()
    try:
        sql = "SELECT concat(firstname, ' ', lastname) as FullName, TIMESTAMPDIFF(YEAR, birthDate, CURDATE()) AS age FROM Patient Having age > %s Order by age" % age
        curr.execute(sql)
        return curr.fetchall(), 'success'
    except Exception as Ex:
        print("Error:", Ex)
        return [], 'error'
