# SELECT treatmentName, treatmentDescription, treatmentCost, diseaseName FROM Treatment t, Disease d WHERE t.diseaseID = d.diseaseID ORDER BY treatmentCost ASC, treatmentName DESC;

import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='HospitalManagementSystem')
# Creating a cursor object using the cursor() method
cursor = conn.cursor()


def get_numbers():
    final_res = {}
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
    for cur in results:
        if cur.with_rows:
            res = cur.fetchall()
            table_type = res[0][1]

            if table_type == 'Patient':
                final_res[table_type] = res[0][0]
            elif table_type == 'Doctor':
                final_res[table_type] = res[0][0]
            elif table_type == 'Disease':
                final_res[table_type] = res[0][0]
            elif table_type == 'Treatment':
                final_res[table_type] = res[0][0]
            elif table_type == 'Staff':
                final_res[table_type] = res[0][0]
            elif table_type == 'Bill':
                final_res[table_type] = res[0][0]
            elif table_type == 'Appointment':
                final_res[table_type] = res[0][0]
            elif table_type == 'Room':
                final_res[table_type] = res[0][0]
            elif table_type == 'RoomAss':
                final_res[table_type] = res[0][0]

    print('result:', final_res)

    return final_res
