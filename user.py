import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='HospitalManagementSystem')
# Creating a cursor object using the cursor() method
cursor = conn.cursor()


def create_user(username, password):
    try:
        sql = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (username, password)
        cursor.execute(sql)
        return True
    except Exception as Ex:
        print("Error creating MySQL User: %s" % Ex)
        return False


def drop_user(username):
    try:
        sql = "DROP USER '%s'@'localhost';" % username
        cursor.execute(sql)
        return True
    except Exception as Ex:
        print("Error dropping MySQL User: %s" % Ex)
        return False


def grant_privileges(permissions, tables, username):
    try:
        print(permissions, tables, username)
        for table in tables:
            sql = "GRANT %s ON HospitalManagementSystem.%s TO '%s'@'localhost'" % (permissions, table, username)
            cursor.execute(sql)
        return True
    except Exception as Ex:
        print("Error: %s" % Ex)
        return False

