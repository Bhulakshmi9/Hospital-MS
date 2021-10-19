import mysql.connector


# establishing the connection
class Login:

    def __init__(self, username, password):
        try:
            self.conn = mysql.connector.connect(user=username, password=password, host='127.0.0.1',
                                                database='HospitalManagementSystem')
            # Creating a cursor object using the cursor() method
            self.cursor = self.conn.cursor()
        except:
            pass

    def validate(self):
        try:
            if self.conn:
                return True
        except:
            return False

    def view_appointments(self, date):
        try:
            sql = "SELECT concat(firstName, ' ', lastName) as fullName, p.email, p.phoneNumber, d.diseaseName, t.treatmentName, r.roomID, r.roomName, a.startDate " \
                  "FROM Appointment a " \
                  "JOIN Patient p  ON p.patientID  = a.patientID " \
                  "JOIN Disease d ON d.diseaseID = a.diseaseID " \
                  "JOIN Treatment t ON d.diseaseID = t.diseaseID " \
                  "JOIN Room r ON r.roomID = a.roomID WHERE (a.type = 'outpatient' and a.startDate >= %s) or " \
                  "(a.type = 'inpatient' and a.endDate is NULL and a.startDate >= %s)" % (
                      "'" + date + "'", "'" + date + "'")
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res, "success"
        except:
            print("Error")
            return [], "error"

    # viewing staff based on room number
    def view_rooms(self, num):
        try:
            sql = "SELECT concat(firstName, ' ', lastName) as fullName, email, phoneNumber FROM Staff WHERE staffID IN (SELECT staffID FROM RoomAssignments WHERE roomID = %s)" % num
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res, "success"
        except Exception as Ex:
            print("Error", Ex)
            return [], "error"
