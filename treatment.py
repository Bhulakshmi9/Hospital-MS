# SELECT treatmentName, treatmentDescription, treatmentCost, diseaseName FROM Treatment t, Disease d WHERE t.diseaseID = d.diseaseID ORDER BY treatmentCost ASC, treatmentName DESC;

import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='HospitalManagementSystem')
# Creating a cursor object using the cursor() method
cursor = conn.cursor()


def get_treatments_by_cost_asc_name_desc():
    sql = "SELECT treatmentName, treatmentDescription, treatmentCost, diseaseName, deathRate FROM Treatment t, Disease d WHERE t.diseaseID = d.diseaseID ORDER BY treatmentCost ASC, deathRate DESC;"
    cursor.execute(sql)
    return cursor.fetchall()

