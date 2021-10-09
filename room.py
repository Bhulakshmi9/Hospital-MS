import mysql.connector

# establishing the connection
import credentials

conn = mysql.connector.connect(user='root', password=credentials.PASSWORD, host='127.0.0.1',
                               database='HospitalManagementSystem')
# Creating a cursor object using the cursor() method
cursor = conn.cursor()


def view_all():
    sql = "SELECT * FROM Room"
    cursor.execute(sql)
    return cursor.fetchall()


def update_room(cost, rid):
    sql = "Update Room SET roomCost = %s WHERE roomID = %s" % (cost, rid)
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        conn.rollback()
        return False


def delete_room(rid):
    sql = "DELETE FROM Room WHERE roomID = %s" % rid
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        conn.rollback()
        return False


def delete_column():
    try:
        cursor.execute("ALTER TABLE Room DROP COLUMN hospitalName")
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
