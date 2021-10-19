import PySimpleGUI as sg

import db_init

db_init.create()

import backup
import patient
import room
import user
import login
import treatment
import common

# sg.theme('DarkTeal9')
# sg.theme('LightBrown13')
# sg.theme('Material1')
sg.theme('DarkBrown4')
# sg.theme('LightYellow')
# ----------- Create the layouts this Window will display -----------
layoutMain = [[sg.Button('Admin', font=('Helvetica', 15)), sg.Button('User', font=('Helvetica', 15))]]
# layoutAdmin = [[sg.]]
layoutAdminLogin = [[sg.Button('Manage', font=('Helvetica', 15))],
                    [sg.Button('Administration', font=('Helvetica', 15))],
                    [sg.Button('Backup Database', font=('Helvetica', 15))],
                    [sg.Text(key='backup', text_color='Lightgreen', font=('Helvetica', 15))]]
layoutManage = [[sg.Button('View Number of Records in each table', key='ViewNum', font=('Helvetica', 15))],
                [sg.Button('Manage Tables', font=('Helvetica', 15))],
                [sg.Button('Delete Column', font=('Helvetica', 15))],
                # [sg.Button('Manage Patients')],
                # [sg.Button('Manage Doctors')],
                # [sg.Button('Manage OutPatient Appointments')],
                # [sg.Button('Manage InPatient Appointments')],
                # [sg.Button('Manage Diseases')],
                [sg.Button('Manage Treatments', font=('Helvetica', 15))],
                # [sg.Button('Manage Rooms')],
                # [sg.Button('Manage Staff')],
                # [sg.Button('Manage Room Assignments')],
                # [sg.Button('Manage Bills')],
                [sg.Button('Back to Admin', key='backtoadmin', font=('Helvetica', 15), button_color='FireBrick')]]
layoutViewNum = [[sg.Text(key='PatientNum', font=('Helvetica', 15))],
                 [sg.Text(key='DoctorNum', font=('Helvetica', 15))],
                 [sg.Text(key='StaffNum', font=('Helvetica', 15))],
                 [sg.Text(key='RoomNum', font=('Helvetica', 15))],
                 [sg.Text(key='RoomAssNum', font=('Helvetica', 15))],
                 [sg.Text(key='DiseaseNum', font=('Helvetica', 15))],
                 [sg.Text(key='TreatmentNum', font=('Helvetica', 15))],
                 [sg.Text(key='AppointmentNum', font=('Helvetica', 15))],
                 [sg.Text(key='BillNum', font=('Helvetica', 15))],
                 [sg.Button('Back to Manage', key='backtomanage', font=('Helvetica', 15), button_color='FireBrick')]]
# layoutManagePatient = [[sg.Button('View Patients')],
#     #                    [sg.Button('Add Patient')],
#     #                    [sg.Button('Update Patient')],
#     #                    [sg.Button('Delete Patient')],
#                        [sg.Button('Back to Admin Menu')]
# ]
# layoutManageDoctor = [[sg.Button('View Doctors', font=('Helvetica', 15))],
#                       [sg.Button('Add Doctor', font=('Helvetica', 15))],
#                       [sg.Button('Update Doctor', font=('Helvetica', 15))],
#                       [sg.Button('Delete Doctor', font=('Helvetica', 15))],
#                       [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
# layoutManageOutPatientApp = [[sg.Button('View OutPatient Appointments', font=('Helvetica', 15))],
#                              [sg.Button('Add OutPatient Appointment', font=('Helvetica', 15))],
#                              [sg.Button('Update OutPatient Appointment', font=('Helvetica', 15))],
#                              [sg.Button('Delete OutPatient Appointment', font=('Helvetica', 15))],
#                              [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
# layoutManageInPatientApp = [[sg.Button('View InPatient Appointments', font=('Helvetica', 15))],
#                             [sg.Button('Add InPatient Appointment', font=('Helvetica', 15))],
#                             [sg.Button('Update InPatient Appointment', font=('Helvetica', 15))],
#                             [sg.Button('Delete InPatient Appointment', font=('Helvetica', 15))],
#                             [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
# layoutManageDisease = [[sg.Button('View Diseases', font=('Helvetica', 15))],
#                        [sg.Button('Add Disease', font=('Helvetica', 15))],
#                        [sg.Button('Update Disease', font=('Helvetica', 15))],
#                        [sg.Button('Delete Disease', font=('Helvetica', 15))],
#                        [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
layoutManageTreatment = [[sg.Button('View Treatments By Order', key="ViewTreatmentsOrder", font=('Helvetica', 15))],
                         # [sg.Button('Add Treatment')],
                         # [sg.Button('Update Treatment')],
                         # [sg.Button('Delete Treatment')],
                         # [sg.Button('Back to Admin Menu')],
                         [sg.Button('Back to Manage', key='backtomanage1', font=('Helvetica', 15),
                                    button_color='FireBrick')]
                         ]
# layoutManageRoom = [[sg.Button('View Rooms', font=('Helvetica', 15))],
#                     [sg.Button('Add Room', font=('Helvetica', 15))],
#                     [sg.Button('Update Room', font=('Helvetica', 15))],
#                     [sg.Button('Delete Room', font=('Helvetica', 15))],
#                     [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
# layoutManageStaff = [[sg.Button('View Staffs', font=('Helvetica', 15))],
#                      [sg.Button('Add Staff', font=('Helvetica', 15))],
#                      [sg.Button('Update Staff', font=('Helvetica', 15))],
#                      [sg.Button('Delete Staff', font=('Helvetica', 15))],
#                      [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
# layoutManageRoomAssignments = [[sg.Button('View Room Assignments', font=('Helvetica', 15))],
#                                [sg.Button('Assign a Room', font=('Helvetica', 15))],
#                                [sg.Button('Update Room Assignment', font=('Helvetica', 15))],
#                                [sg.Button('Delete Room Assignment', font=('Helvetica', 15))],
#                                [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
# layoutManageBill = [[sg.Button('View Bills', font=('Helvetica', 15))],
#                     [sg.Button('Add Bill', font=('Helvetica', 15))],
#                     [sg.Button('Update Bill', font=('Helvetica', 15))],
#                     [sg.Button('Delete Bill', font=('Helvetica', 15))],
#                     [sg.Button('Back to Admin Menu', font=('Helvetica', 15))]]
layoutAdministration = [[sg.Button('Add New User', font=('Helvetica', 15))],
                        [sg.Button('Drop User', font=('Helvetica', 15))],
                        [sg.Button('Grant Permissions', font=('Helvetica', 15))],
                        [sg.Button('Back to Admin', key='backtoadmin1', font=('Helvetica', 15),
                                   button_color='FireBrick')]]
layoutAddNewUser = [
    [sg.Text('Enter Username', font=('Helvetica', 15)), sg.Input(key='-InputUsername-', font=('Helvetica', 15))],
    [sg.Text('Enter Password', font=('Helvetica', 15)), sg.Input(key='-InputPassword-', font=('Helvetica', 15))],
    [sg.Button('Add User', font=('Helvetica', 15))],
    [sg.Text(key='-AddUserError-', text_color='Red', font=('Helvetica', 15))],
    [sg.Text(key='-AddUserSuccess-', text_color='Lightgreen', font=('Helvetica', 15))],
    [sg.Button('Back to Administration', key='backtoadminis', font=('Helvetica', 15), button_color='FireBrick')]]
layoutDropUser = [[sg.Text('Enter Username'), sg.Input(key='-InputUsernameDrop-')],
                  [sg.Button('Drop')],
                  [sg.Text(key='-DropUserError-', text_color='Red', font=('Helvetica', 15))],
                  [sg.Text(key='-DropUserSuccess-', text_color='Lightgreen', font=('Helvetica', 15))],
                  [sg.Button('Back to Administration', key='backtoadminis1', font=('Helvetica', 15),
                             button_color='FireBrick')]]
layoutGrantPermissions = [
    [sg.Text('Enter Username', font=('Helvetica', 15)), sg.Input(key='-InputUsernameGrant-', font=('Helvetica', 15))],
    [sg.Text(font=('Helvetica', 15))],
    [sg.Text('Grant All Privileges', font=('Helvetica', 15))],
    [sg.Radio('ALL PRIVILEGES', 1, key='-AP-', enable_events=True, font=('Helvetica', 15)),
     sg.Button('Reset', font=('Helvetica', 15))],
    # [sg.Checkbox('ALL PRIVILEGES', 1, key='-AP-')],
    [sg.Text('or Select from below', font=('Helvetica', 15))],
    [sg.Checkbox('SELECT', key='-SELECT-', font=('Helvetica', 15)),
     sg.Checkbox('INSERT', key='-INSERT-', font=('Helvetica', 15))],
    [sg.Checkbox('DROP', key='-DROP-', font=('Helvetica', 15)),
     sg.Checkbox('CREATE', key='-CREATE-', font=('Helvetica', 15))],
    [sg.Checkbox('DELETE', key='-DELETE-', font=('Helvetica', 15)),
     sg.Checkbox('UPDATE', key='-UPDATE-', font=('Helvetica', 15))],
    [sg.Checkbox('GRANT OPTION', key='-GRANTOPTION-', font=('Helvetica', 15))],
    [sg.Text('Choose all tables', font=('Helvetica', 15))],
    [sg.Radio('All Tables', 2, key='-AT-', enable_events=True, font=('Helvetica', 15)),
     sg.Button('Reset', key='-ResetTables-', font=('Helvetica', 15))],
    [sg.Text('or select from below', font=('Helvetica', 15))],
    [sg.Checkbox('Patient', key='-Patient-', font=('Helvetica', 15)),
     sg.Checkbox('Doctor', key='-Doctor-', font=('Helvetica', 15))],
    [sg.Checkbox('Room', key='-Room-', font=('Helvetica', 15)),
     sg.Checkbox('Staff', key='-Staff-', font=('Helvetica', 15))],
    [sg.Checkbox('Room Assignments', key='-RoomAss-', font=('Helvetica', 15)),
     sg.Checkbox('Disease', key='-Disease-', font=('Helvetica', 15))],
    [sg.Checkbox('Treatment', key='-Treatment-', font=('Helvetica', 15)),
     sg.Checkbox('Appointment', key='-Appointment-', font=('Helvetica', 15))],
    [sg.Checkbox('Bill', key='-Bill-', font=('Helvetica', 15))],
    [sg.Button('Grant', font=('Helvetica', 15))],
    [sg.Text(key='-GrantError-', text_color='Red', font=('Helvetica', 15))],
    [sg.Text(key='-GrantSuccess-', text_color='Lightgreen', font=('Helvetica', 15))],
    [sg.Button('Back to Administration', key='backtoadminis2', font=('Helvetica', 15), button_color='FireBrick')]]
# layoutViewPatients = [[sg.Button('View All')],
#                       [sg.Button('View By ID')],
#                       [sg.Button('View By Email')]]

viewpatientsdata = [
    [1, "abc", "def", "2021-10-21", "Male", "abc@gmail.com", "605098765", 169, 150, "SD-57069", "234-45-456"]]
viewpatientsheading = ["Patient ID", "First Name", "Last Name", "Birst Date", "Gender", "Email", "Phone Number",
                       "Height (cm)", "Weight (pounds)", "Address", "SSN"]
viewroomdata = [[101, "abc", "ed", "ed", "ed", 100.00]]
viewroomhead = ["Room ID", "Room Name", "Room Type", "Room Description", "Hospital Name", "Room Cost"]
layoutManageTables = [[sg.Text('Choose Table to update or delete:', font=('Helvetica', 15))],
                      [sg.Radio('Patient', 1, key='Patient', enable_events=True, font=('Helvetica', 15))],
                      # [sg.Radio('Doctor', 1, key='Doctor', enable_events=True)],
                      # [sg.Radio('Staff', 1, key='Staff', enable_events=True)],
                      [sg.Radio('Room', 1, key='Room', enable_events=True, font=('Helvetica', 15))],
                      # [sg.Radio('Room Assignments', 1, key='RoomAssignments', enable_events=True)],
                      # [sg.Radio('Disease', 1, key='Disease', enable_events=True)],
                      # [sg.Radio('Treatment', 1, key='Treatment', enable_events=True)],
                      # [sg.Radio('Appointment', 1, key='Appointment', enable_events=True)],
                      # [sg.Radio('Bill', 1, key='Bill', enable_events=True)],
                      [sg.Table(values=viewpatientsdata, headings=viewpatientsheading,
                                # max_col_width=25,
                                # background_color='white',
                                auto_size_columns=True,
                                # display_row_numbers=True,
                                justification='right',
                                num_rows=0,
                                font=('Helvetica', 15),
                                # alternating_row_color='black',
                                key='-viewpatienttable-',
                                row_height=25, visible=False)],
                      [sg.Table(values=viewroomdata, headings=viewroomhead,
                                # max_col_width=25,
                                # background_color='white',
                                auto_size_columns=True, font=('Helvetica', 15),
                                # display_row_numbers=True,
                                justification='right',
                                num_rows=0,
                                # alternating_row_color='black',
                                key='-viewroomtable-',
                                row_height=25, visible=False)],
                      [sg.Text('Enter ID to update or delete:', key="idupdel", visible=False, font=('Helvetica', 15)),
                       sg.Input(key='-PRID-', visible=False, font=('Helvetica', 15)),
                       sg.Button('Update', key='BtnUpdate', visible=False, font=('Helvetica', 15)),
                       sg.Button('Delete', key='BtnDelete', visible=False, font=('Helvetica', 15))],
                      [sg.Text('Enter height:', key='upheight', visible=False, font=('Helvetica', 15)),
                       sg.Input(key="upheightinput", visible=False, font=('Helvetica', 15))],
                      [sg.Text('Enter weight:', key='upweight', visible=False, font=('Helvetica', 15)),
                       sg.Input(key="upweightinput", visible=False, font=('Helvetica', 15))],
                      [sg.Button('Update', key="BtnUpdateP", visible=False, font=('Helvetica', 15))],
                      [sg.Text('Enter room cost:', key='uprcost', visible=False, font=('Helvetica', 15)),
                       sg.Input(key="uprcostinput", visible=False, font=('Helvetica', 15))],
                      [sg.Button('Update', key='BtnUpdateR', visible=False, font=('Helvetica', 15))],
                      [sg.Text(key="updelerror", text_color="Red", font=('Helvetica', 15))],
                      [sg.Text(key="updelsuccess", text_color="Lightgreen", font=('Helvetica', 15))],
                      [sg.Button('Back to Manage', key='backtomanage2', font=('Helvetica', 15),
                                 button_color='FireBrick')]]
treatmentorderdata = [["abc", "def", "ghi", "jkl", 0.5]]
treatmentorderheadings = ["Treatment Name", "Treatment Description", "treatment Cost", "Disease Name", "Death Rate"]
layoutViewTreatmentsOrder = [
    [sg.Text('Treatments by ordering treatment cost in ascending and death rate in descending',
             font=('Helvetica', 15))],
    [sg.Text('', key='-messtreatorder-', font=('Helvetica', 15))],
    [sg.Table(values=treatmentorderdata, headings=treatmentorderheadings,
              # max_col_width=25,
              # background_color='black',
              auto_size_columns=True, font=('Helvetica', 15),
              # display_row_numbers=True,
              justification='right',
              num_rows=0,
              # alternating_row_color='black',
              key='-treatordertable-',
              row_height=25, visible=False)],
    [sg.Button('Back to Manage', key='backtomanage4', font=('Helvetica', 15), button_color='FireBrick')]]
delviewroomdata = [[101, "abc", "ed", "ed", 100.00]]
delviewroomhead = ["Room ID", "Room Name", "Room Type", "Room Description", "Room Cost"]
layoutDeleteColumn = [[sg.Table(values=viewroomdata, headings=viewroomhead,
                                # max_col_width=25,
                                # background_color='black',
                                auto_size_columns=True, font=('Helvetica', 15),
                                # display_row_numbers=True,
                                justification='right',
                                num_rows=0,
                                # alternating_row_color='black',
                                key='-viewroomdeltable-',
                                row_height=25, visible=False)],[sg.Table(values=delviewroomdata, headings=delviewroomhead,
                                # max_col_width=25,
                                # background_color='black',
                                auto_size_columns=True, font=('Helvetica', 15),
                                # display_row_numbers=True,
                                justification='right',
                                num_rows=0,
                                # alternating_row_color='black',
                                key='-viewroomdelaftertable-',
                                row_height=25, visible=False)],
                      [sg.Text('Deleting "Hospital Name" column from table Room', font=('Helvetica', 15))],
                      [sg.Button('Go Ahead', key="yes", font=('Helvetica', 15)),
                       sg.Button('Cancel / Back to Manage', key="backtomanage3", font=('Helvetica', 15))],
                      [sg.Text(key='delcolerror', text_color='Red', font=('Helvetica', 15))],
                      [sg.Text(key='delcolsuccess', text_color='Lightgreen', font=('Helvetica', 15))]]

# user layouts
layoutUser = [
    [sg.Text('Enter Username', font=('Helvetica', 15)), sg.Input(key='-InputUsernameLogin-', font=('Helvetica', 15))],
    [sg.Text('Enter Password', font=('Helvetica', 15)),
     sg.Input(key='-InputPasswordLogin-', password_char='*', font=('Helvetica', 15))],
    [sg.Button('Login', font=('Helvetica', 15))],
    [sg.Text(key='-LoginError-', text_color='Red', font=('Helvetica', 15))]]
layoutUserMain = [[sg.Text('', key='-welcomemessage-', font=('Helvetica', 15))],
                  [sg.Button('View Appointments', key='ViewAppUser', font=('Helvetica', 15))],
                  [sg.Button('View Staff by Room', key='ViewStaffRoomUser', font=('Helvetica', 15))],
                  [sg.Button('View Patient Contact Info', key='ViewPatInfoUser', font=('Helvetica', 15))],
                  [sg.Button('View Patients Above Age', key='ViewPatAgeUser', font=('Helvetica', 15))]]
data = [["John", "test", "4654546565", "drer", "rtrtr", 101, "ward", '2021-34-34']]
# data=[[]]
headings = ["Patient Full Name", "Email", "Phone Number", "Disease", "Treatment", "Room No", "Room Name", "Start Date"]
layoutViewAppointmentsUser = [[sg.Text('', key='-mess-', font=('Helvetica', 15))],
                              [sg.Table(values=data, headings=headings,
                                        # max_col_width=25,
                                        # background_color='black',
                                        auto_size_columns=True, font=('Helvetica', 15),
                                        # display_row_numbers=True,
                                        justification='right',
                                        num_rows=1,
                                        # alternating_row_color='black',
                                        key='-apptable-',
                                        row_height=25)],
                      [sg.Button('Back to User Menu', key='backtoumenu', font=('Helvetica', 15),
                                 button_color='FireBrick')]]
ViewStaffRoomUserData = [["tes", "tes", "9342374837"]]
ViewStaffRoomUserHeadings = ["Staff Full Name", "Email", "Phone Number"]
layoutViewStaffRoomUser = [
    [sg.Text('Enter Room Number:', font=('Helvetica', 15)), sg.Input(key='-InputRoomNoUser-', font=('Helvetica', 15)),
     sg.Button('View Staff', key='BtnRoomsUser', font=('Helvetica', 15))],
    [sg.Text('', key='-messstaffroomuser-', font=('Helvetica', 15))],
    [sg.Table(values=ViewStaffRoomUserData, headings=ViewStaffRoomUserHeadings,
              # max_col_width=25,
              # background_color='black',
              auto_size_columns=True, font=('Helvetica', 15),
              # display_row_numbers=True,
              justification='right',
              num_rows=0,
              # alternating_row_color='black',
              key='-stafftable-',
              row_height=25, visible=False)],
                      [sg.Button('Back to User Menu', key='backtoumenu1', font=('Helvetica', 15),
                                 button_color='FireBrick')]]

patinfodata = [["abc", "def", "ghi"]]
patinfoheadings = ["Full Name", "Email", "Phone Number"]
layoutViewPatInfoUser = [
    [sg.Text("View Patient's contact information by First Name, Last Name or ID", font=('Helvetica', 15))],
    [sg.Text('Enter ID:', font=('Helvetica', 15)), sg.Input(key='-InputPatID-', font=('Helvetica', 15))],
    [sg.Text('or Enter First Name:', font=('Helvetica', 15)), sg.Input(key='-InputPatFN-', font=('Helvetica', 15))],
    [sg.Text('or Enter Last Name:', font=('Helvetica', 15)), sg.Input(key='-InputPatLN-', font=('Helvetica', 15))],
    [sg.Button('Get Info', key='BtnPatInfoUser', font=('Helvetica', 15))],
    [sg.Text('', key='-messpatinfouser-', font=('Helvetica', 15))],
    [sg.Table(values=patinfodata, headings=patinfoheadings,
              # max_col_width=25,
              # background_color='black',
              auto_size_columns=True, font=('Helvetica', 15),
              # display_row_numbers=True,
              justification='right',
              num_rows=0,
              # alternating_row_color='black',
              key='-patinfotable-',
              row_height=25, visible=False)],
                      [sg.Button('Back to User Menu', key='backtoumenu2', font=('Helvetica', 15),
                                 button_color='FireBrick')]
]

patagedata = [["abc", 26]]
patageheadings = ["Full Name", "Age"]
layoutViewPatAgeUser = [
    [sg.Text('Enter Age:', font=('Helvetica', 15)), sg.Input(key='-InputAgeUser-', font=('Helvetica', 15)),
     sg.Button('View Patients', key='BtnPatAgeUser', font=('Helvetica', 15))],
    [sg.Text('', key='-messpatageuser-', font=('Helvetica', 15))],
    [sg.Table(values=patagedata, headings=patageheadings,
              # max_col_width=25,
              # background_color='black',
              auto_size_columns=True, font=('Helvetica', 15),
              # display_row_numbers=True,
              justification='right',
              num_rows=0,
              # alternating_row_color='black',
              key='-patagetable-',
              row_height=25, visible=False)],
                      [sg.Button('Back to User Menu', key='backtoumenu3', font=('Helvetica', 15),
                                 button_color='FireBrick')]
]
# [psg.Text('Choose your Toppings',size=(20, 1), font='Lucida',justification='left')],
# [psg.Checkbox('Pepperoni',key='Pepperoni'), psg.Checkbox('Mushroom',key='Mushroom'),
#  psg.Checkbox('Corn',key='Corn'),psg.Checkbox('Cherry Tomatoes',key='Cherry Tomatoes'),psg.Checkbox('Olives',key='Olives')],

# ----------- Create actual layout using Columns and a row of Buttons
layout = [
    [sg.Text("Welcome to Hospital Management System", font=('Helvetica', 30), justification='center', key='-MESS-')],
    [sg.Column(layoutMain, key='-COLMain-'), sg.Column(layoutAdminLogin, visible=False, key='-COLAdmin-'),
     sg.Column(layoutUser, visible=False, key='-COLUser-'), sg.Column(layoutManage, visible=False, key='-COLManage-'),
     # sg.Column(layoutManagePatient, visible=False, key='-COLManagePatients-'),
     sg.Column(layoutManageTables, visible=False, key='-COLManageTables-'),
     # sg.Column(layoutManageDoctor, visible=False, key='-COLManageDoctors-'),
     # sg.Column(layoutManageOutPatientApp, visible=False, key='-COLManageOutPatientAppointments-'),
     # sg.Column(layoutManageInPatientApp, visible=False, key='-COLManageInPatientAppointments-'),
     # sg.Column(layoutManageDisease, visible=False, key='-COLManageDiseases-'),
     sg.Column(layoutManageTreatment, visible=False, key='-COLManageTreatments-'),
     # sg.Column(layoutManageRoom, visible=False, key='-COLManageRooms-'),
     # sg.Column(layoutManageStaff, visible=False, key='-COLManageStaff-'),
     # sg.Column(layoutManageRoomAssignments, visible=False, key='-COLManageRoomAssignments-'),
     # sg.Column(layoutManageBill, visible=False, key='-COLManageBills-'),
     sg.Column(layoutAdministration, visible=False, key='-COLAdministration-'),
     sg.Column(layoutAddNewUser, visible=False, key='-COLAddNewUser-'),
     sg.Column(layoutDropUser, visible=False, key='-COLDropUser-'),
     sg.Column(layoutGrantPermissions, visible=False, key='-COLGrantPermissions-'),
     sg.Column(layoutUserMain, visible=False, key='-COLLogin-'),
     sg.Column(layoutViewAppointmentsUser, visible=False, key='-COLViewAppUser-'),
     sg.Column(layoutViewStaffRoomUser, visible=False, key='-COLViewStaffRoomUser-'),
     sg.Column(layoutViewPatInfoUser, visible=False, key='-COLViewPatInfoUser-'),
     sg.Column(layoutViewPatAgeUser, visible=False, key='-COLViewPatAgeUser-'),
     sg.Column(layoutViewTreatmentsOrder, visible=False, key='-COLViewTreatmentsOrder-'),
     sg.Column(layoutViewNum, visible=False, key='-COLViewNum-'),
     sg.Column(layoutDeleteColumn, visible=False, key='-COLDeleteColumn-')
     ],
    [sg.Text()],
    [sg.Button('Main', font=('Helvetica', 15), button_color='blue'),
     sg.Button('Exit', font=('Helvetica', 15), button_color='red')]]

window = sg.Window('Hospital Management System', layout)

layout = 'Main'  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event in ['Main', 'Admin', 'User', 'Manage', 'Administration']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = event
        window[f'-COL{layout}-'].update(visible=True)
        if event == 'User':
            window[f'-InputUsernameLogin-'].update('')
            window[f'-InputPasswordLogin-'].update('')
    elif event == 'Backup Database':
        backup.backup()
        window['backup'].update('Database backed up successfully...!!')
    elif event in ['Manage Patients', 'Manage Doctors', 'Manage OutPatient Appointments',
                   'Manage InPatient Appointments', 'Manage Diseases', 'Manage Treatments', 'Manage Rooms',
                   'Manage Staff', 'Manage Room Assignments', 'Manage Bills', 'Manage Tables', 'ViewNum',
                   'Delete Column']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = event.replace(' ', '')
        window[f'-COL{layout}-'].update(visible=True)
        if event == 'ViewNum':
            res = common.get_numbers()
            if len(res) > 0:
                for entry in res:
                    if entry == 'RoomAss':
                        window[f'{entry}Num'].update("Number of Room Assignments: " + str(res[entry]))
                    else:
                        window[f'{entry}Num'].update("Number of " + entry + ": " + str(res[entry]))
        if event == 'Manage Tables':
            window['Patient'].reset_group()
            window['Room'].reset_group()
            window['-viewpatienttable-'].update(visible=False)
            window['-viewroomtable-'].update(visible=False)
            window['idupdel'].update(visible=False)
            window['-PRID-'].update(visible=False)
            window['BtnUpdate'].update(visible=False)
            window['BtnDelete'].update(visible=False)
            window['upheight'].update(visible=False)
            window['upheightinput'].update(visible=False)
            window['upweight'].update(visible=False)
            window['upweightinput'].update(visible=False)
            window['BtnUpdateP'].update(visible=False)
            window['BtnUpdateR'].update(visible=False)
            window['uprcost'].update(visible=False)
            window['uprcostinput'].update(visible=False)
            window['updelerror'].update('')
            window['updelsuccess'].update('')
        if event == 'Delete Column':
            res = room.view_all()
            window['-viewroomdeltable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
    elif event in ['backtoadmin', 'backtoadmin1']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = 'Admin'
        window[f'-COL{layout}-'].update(visible=True)
    elif event in ['backtomanage', 'backtomanage1', 'backtomanage2', 'backtomanage3', 'backtomanage4']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = 'Manage'
        window[f'-COL{layout}-'].update(visible=True)
    elif event in ['backtoadminis', 'backtoadminis1', 'backtoadminis2']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = 'Administration'
        window[f'-COL{layout}-'].update(visible=True)
    elif event in ['backtoumenu', 'backtoumenu1', 'backtoumenu2', 'backtoumenu3']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = 'Login'
        window[f'-COL{layout}-'].update(visible=True)
    elif event == "yes":
        res = room.delete_column()
        if res:
            window['delcolsuccess'].update('Deleted column successfully')
            res = room.view_all()
            window['-viewroomdeltable-'].update(visible=False)
            window['-viewroomdelaftertable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
        else:
            window['delcolerror'].update('Column could not be deleted')

    elif event in ['Patient', 'Doctor', 'Room', 'Staff', 'RoomAssignments', 'Disease', 'Treatment', 'Appointment',
                   'Bill']:
        print(event)
        if values['Patient']:
            res = patient.view_all()
            window['-viewroomtable-'].update(visible=False)
            window['idupdel'].update(visible=False)
            window['-PRID-'].update(visible=False)
            window['BtnUpdate'].update(visible=False)
            window['BtnDelete'].update(visible=False)
            window['uprcost'].update(visible=False)
            window['uprcostinput'].update(visible=False)
            window['BtnUpdateR'].update(visible=False)
            window['-viewpatienttable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
            window['idupdel'].update(visible=True)
            window['-PRID-'].update(visible=True, value='')
            window['BtnUpdate'].update(visible=True)
            window['BtnDelete'].update(visible=True)
        if values['Room']:
            res = room.view_all()
            window['-viewpatienttable-'].update(visible=False)
            window['idupdel'].update(visible=False)
            window['-PRID-'].update(visible=False)
            window['BtnUpdate'].update(visible=False)
            window['BtnDelete'].update(visible=False)
            window['upheight'].update(visible=False)
            window['upweight'].update(visible=False)
            window['upheightinput'].update(visible=False)
            window['upweightinput'].update(visible=False)
            window['BtnUpdateP'].update(visible=False)
            window['-viewroomtable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
            window['idupdel'].update(visible=True)
            window['-PRID-'].update(visible=True, value='')
            window['BtnUpdate'].update(visible=True)
            window['BtnDelete'].update(visible=True)
    elif event == 'BtnUpdate':
        if values['Patient']:
            window['upheight'].update(visible=True)
            window['upweight'].update(visible=True)
            window['upheightinput'].update(visible=True)
            window['upweightinput'].update(visible=True)
            window['BtnUpdateP'].update(visible=True)
        elif values['Room']:
            window['uprcost'].update(visible=True)
            window['uprcostinput'].update(visible=True)
            window['BtnUpdateR'].update(visible=True)
    elif event == 'BtnDelete':
        # sg.popup_ok_cancel("Are you sure to delete it?", auto_close=False)
        prid = values['-PRID-']
        if len(prid) == 0:
            window['updelerror'].update('Please enter ID.')
        else:
            if values['Patient']:
                res = patient.delete_patient(prid)
                if res:
                    window['updelsuccess'].update('Deleted successfully..!!')
                    res = patient.view_all()
                    window['-viewpatienttable-'].update(values=[list(ele) for ele in res], num_rows=len(res),
                                                     visible=True)
                else:
                    window['updelerror'].update("Couldn't delete the record")
            elif values['Room']:
                res = room.delete_room(prid)
                if res:
                    window['updelsuccess'].update('Deleted successfully..!!')
                    res = room.view_all()
                    window['-viewroomtable-'].update(values=[list(ele) for ele in res], num_rows=len(res),
                                                     visible=True)
                else:
                    window['updelerror'].update("Couldn't delete the record")

    elif event in ['BtnUpdateP', 'BtnUpdateR']:
        height = values['upheightinput']
        weight = values['upweightinput']
        rcost = values['uprcostinput']
        prid = values['-PRID-']
        if len(prid) == 0:
            window['updelerror'].update('Please enter ID.')
        else:
            if values['Patient']:
                if len(height) == 0 and len(weight) == 0:
                    window['updelerror'].update('Please enter height and weight.')
                elif len(height) == 0:
                    window['updelerror'].update('Please enter height.')
                elif len(weight) == 0:
                    window['updelerror'].update('Please enter weight.')
                else:
                    if not height.isdigit() and not weight.isdigit():
                        window['updelerror'].update('Please enter valid height in cms and weight in pounds.')
                    elif not height.isdigit():
                        window['updelerror'].update('Please enter valid height in cms.')
                    elif not weight.isdigit():
                        window['updelerror'].update('Please enter valid weight in pounds.')
                    else:
                        window['updelerror'].update('')
                        print(height, weight)
                        res = patient.update_patient(float(height), float(weight), int(prid))
                        if res:
                            window['updelsuccess'].update('Updated successfully..!!')
                            res = patient.view_all()
                            window['-viewpatienttable-'].update(values=[list(ele) for ele in res], num_rows=len(res),
                                                                visible=True)
                        else:
                            window['updelerror'].update("Couldn't update the record")
            elif values['Room']:
                if len(rcost) == 0:
                    window['updelerror'].update('Please enter room cost.')
                elif not rcost.isdigit():
                    window['updelerror'].update('Please enter valid room cost.')
                else:
                    window['updelerror'].update('')
                    print(rcost)
                    res = room.update_room(float(rcost), int(prid))
                    if res:
                        window['updelsuccess'].update('Updated successfully..!!')
                        res = room.view_all()
                        window['-viewroomtable-'].update(values=[list(ele) for ele in res], num_rows=len(res),
                                                         visible=True)
                    else:
                        window['updelerror'].update("Couldn't update the record")
    elif event in ['Back to Admin Menu', 'Back to Admin Menu0', 'Back to Admin Menu1', 'Back to Admin Menu2',
                   'Back to Admin Menu3', 'Back to Admin Menu4', 'Back to Admin Menu5', 'Back to Admin Menu6',
                   'Back to Admin Menu7', 'Back to Admin Menu8', 'Back to Admin Menu9']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = 'Admin'
        window[f'-COL{layout}-'].update(visible=True)
    elif event in ['Add New User', 'Drop User', 'Grant Permissions']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = event.replace(' ', '')
        window[f'-COL{layout}-'].update(visible=True)
    elif event == 'Add User':
        username = values['-InputUsername-']
        password = values['-InputPassword-']
        if len(username) <= 0 and len(password) <= 0:
            window['-AddUserError-'].update('Username and Password cannot be null')
        elif len(username) <= 0:
            window['-AddUserError-'].update('Username cannot be null')
        elif not username.isalpha():
            window['-AddUserError-'].update('Username should be only from a - z or A - Z')
        elif len(password) <= 0:
            window['-AddUserError-'].update('Password cannot be null')
        elif not password.isalpha():
            window['-AddUserError-'].update('Password should be only from a - z or A - Z')
        else:
            window['-AddUserError-'].update('')
            print(username, password)
            res = user.create_user(username, password)
            if res:
                window['-AddUserSuccess-'].update('User added successfully..!!')
            else:
                window['-AddUserError-'].update('User cannot be added. Make sure the user does not exists')
    elif event == 'Login':
        username = values['-InputUsernameLogin-']
        password = values['-InputPasswordLogin-']
        if len(username) <= 0 and len(password) <= 0:
            window['-LoginError-'].update('Username and Password cannot be null')
        elif len(username) <= 0:
            window['-LoginError-'].update('Username cannot be null')
        elif not username.isalpha():
            window['-LoginError-'].update('Username should be only from a - z or A - Z')
        elif len(password) <= 0:
            window['-LoginError-'].update('Password cannot be null')
        elif not password.isalpha():
            window['-LoginError-'].update('Password should be only from a - z or A - Z')
        else:
            window['-LoginError-'].update('')
            print(username, password)
            res = login.Login(username, password).validate()
            if res:
                window[f'-COL{layout}-'].update(visible=False)
                layout = event
                window[f'-COL{layout}-'].update(visible=True)
                window['-welcomemessage-'].update('Welcome, ' + username + '..!!')
            else:
                window['-LoginError-'].update('Login failed. Enter valid username and password')
    elif event == 'Drop':
        username = values['-InputUsernameDrop-']
        if len(username) <= 0:
            window['-DropUserError-'].update('Username cannot be null')
        elif not username.isalpha():
            window['-DropUserError-'].update('Username should be only from a - z or A - Z')
        else:
            window['-DropUserError-'].update('')
            print(username)
            res = user.drop_user(username)
            if res:
                window['-DropUserSuccess-'].update('User dropped successfully..!!')
            else:
                window['-AddUserError-'].update('User cannot be dropped. Make sure the user exists')
    elif event == 'Reset':
        window['-AP-'].reset_group()
    elif event == '-ResetTables-':
        window['-AT-'].reset_group()
    elif event == 'Grant':
        username = values['-InputUsernameGrant-']
        if len(username) <= 0:
            window['-GrantError-'].update('Username cannot be null')
        elif not username.isalpha():
            window['-GrantError-'].update('Username should be only from a - z or A - Z')
        else:
            window['-GrantError-'].update('')
            print(username)
            perm = []
            if values['-AP-']:
                print('ALL PRIVILEGES', username)
                perm.append('ALL PRIVILEGES')
            else:
                if values['-SELECT-']:
                    perm.append('SELECT')
                if values['-INSERT-']:
                    perm.append('INSERT')
                if values['-DROP-']:
                    perm.append('DROP')
                if values['-CREATE-']:
                    perm.append('CREATE')
                if values['-DELETE-']:
                    perm.append('DELETE')
                if values['-UPDATE-']:
                    perm.append('UPDATE')
                if values['-GRANTOPTION-']:
                    perm.append('GRANT OPTION')
            tab = []
            if values['-AT-']:
                print('ALL Tables', username)
                tab.append('*')
            else:
                if values['-Patient-']:
                    tab.append('Patient')
                if values['-Doctor-']:
                    tab.append('Doctor')
                if values['-Disease-']:
                    tab.append('Disease')
                if values['-Treatment-']:
                    tab.append('Treatment')
                if values['-Appointment-']:
                    tab.append('Appointment')
                if values['-Bill-']:
                    tab.append('Bill')
                if values['-Room-']:
                    tab.append('Room')
                if values['-RoomAss-']:
                    tab.append('RoomAssignments')
                if values['-Staff-']:
                    tab.append('Staff')

            if perm == '' and tab == '':
                window['-GrantError-'].update('Choose grant privileges and tables for the user')
            elif perm == '':
                window['-GrantError-'].update('Choose grant privileges for the user')
            elif tab == '':
                window['-GrantError-'].update('Choose tables for the user')
            else:
                print(','.join(perm), tab, username)
                res = user.grant_privileges(','.join(perm), tab, username)
                if res:
                    window['-GrantSuccess-'].update('Privileges are granted successfully...!!!')
                else:
                    window['-GrantError-'].update('Privileges could not be granted. Make sure the user exists.')

            # user.drop_user(username)
            # window['-DropUserSuccess-'].update('User added successfully..!!')
    elif event == 'ViewTreatmentsOrder':
        window[f'-COL{layout}-'].update(visible=False)
        layout = event
        window[f'-COL{layout}-'].update(visible=True)
        res = treatment.get_treatments_by_cost_asc_name_desc()
        window['-messtreatorder-'].update('')
        if len(res) == 0:
            window['-messpatageuser-'].update('No treatments', text_color='White')
        window['-treatordertable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)

    elif event in ['ViewAppUser', 'ViewStaffRoomUser', 'ViewPatInfoUser', 'ViewPatAgeUser']:
        window[f'-COL{layout}-'].update(visible=False)
        layout = event
        window[f'-COL{layout}-'].update(visible=True)
        # view
        if event == 'ViewAppUser':
            res, mess = login.Login(values['-InputUsernameLogin-'], values['-InputPasswordLogin-']).view_appointments(
                '2021-10-07')
            if mess == 'error':
                window['-mess-'].update('User does not have view permissions', text_color='Red')
            else:
                if len(res) == 0:
                    window['-mess-'].update('No appointments', text_color='White')
            window['-apptable-'].update(values=[list(ele) for ele in res], num_rows=len(res))
        if event == 'ViewStaffRoomUser':
            window[f'-InputRoomNoUser-'].update('')
            window[f'-messstaffroomuser-'].update('')
            window[f'-stafftable-'].update(visible=False)
        if event == 'ViewPatInfoUser':
            window[f'-InputPatID-'].update('')
            window[f'-InputPatFN-'].update('')
            window[f'-InputPatLN-'].update('')
            window[f'-messpatinfouser-'].update('')
            window[f'-patinfotable-'].update(visible=False)
        if event == 'ViewPatAgeUser':
            window[f'-InputAgeUser-'].update('')
            window[f'-messpatageuser-'].update('')
            window[f'-patagetable-'].update(visible=False)
    elif event == 'BtnRoomsUser':
        res, mess = login.Login(values['-InputUsernameLogin-'], values['-InputPasswordLogin-']).view_rooms(
            values['-InputRoomNoUser-'])
        if mess == 'error':
            window['-messstaffroomuser-'].update('User does not have view permissions', text_color='Red')
        else:
            if len(res) == 0:
                window['-messstaffroomuser-'].update('No staff', text_color='White')
        window['-stafftable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
    elif event == 'BtnPatInfoUser':
        fname = values['-InputPatFN-']
        lname = values['-InputPatLN-']
        id = values['-InputPatID-']
        if len(fname) <= 0 and len(lname) <= 0 and len(id) <= 0:
            window['-messpatinfouser-'].update('Please enter either first name, last name or ID', text_color='Red')
        # res, mess = [], ''
        if len(id) > 0:
            res, mess = patient.get_contact_info_by_id(values['-InputUsernameLogin-'], values['-InputPasswordLogin-'],
                                                       int(id))

            if mess == 'error':
                window['-messpatinfouser-'].update('User does not have view permissions', text_color='Red')
            else:
                if len(res) == 0:
                    window['-messpatinfouser-'].update('No contact information', text_color='White')
            window['-patinfotable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
        elif len(fname) > 0:
            res, mess = patient.get_contact_info_by_fname(values['-InputUsernameLogin-'],
                                                          values['-InputPasswordLogin-'],
                                                          fname)

            if mess == 'error':
                window['-messpatinfouser-'].update('User does not have view permissions', text_color='Red')
            else:
                if len(res) == 0:
                    window['-messpatinfouser-'].update('No contact information', text_color='White')
            window['-patinfotable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
        elif len(lname) > 0:
            res, mess = patient.get_contact_info_by_lname(values['-InputUsernameLogin-'],
                                                          values['-InputPasswordLogin-'],
                                                          lname)

            if mess == 'error':
                window['-messpatinfouser-'].update('User does not have view permissions', text_color='Red')
            else:
                if len(res) == 0:
                    window['-messpatinfouser-'].update('No contact information', text_color='White')
            window['-patinfotable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
    elif event == 'BtnPatAgeUser':
        age = values['-InputAgeUser-']
        if len(age) <= 0:
            window['-messpatageuser-'].update('Please enter age:', text_color='Red')
        else:
            res, mess = patient.get_patients_above_age(values['-InputUsernameLogin-'], values['-InputPasswordLogin-'],
                                                       int(age))
            window['-messpatageuser-'].update('')
            if mess == 'error':
                window['-messpatageuser-'].update('User does not have view permissions', text_color='Red')
            else:
                if len(res) == 0:
                    window['-messpatageuser-'].update('No patients under age 25', text_color='White')
            window['-patagetable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
window.close()
