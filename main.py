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

# ----------- Create the layouts this Window will display -----------
layoutMain = [[sg.Button('Admin'), sg.Button('User')]]
# layoutAdmin = [[sg.]]
layoutAdminLogin = [[sg.Button('Manage')],
                    [sg.Button('Administration')],
                    [sg.Button('Backup Database')],
                    [sg.Text(key='backup', text_color='Lightgreen', font=('Helvetica', 15))]]
layoutManage = [[sg.Button('View Number of Records in each table', key='ViewNum')],
                [sg.Button('Manage Tables')],
                [sg.Button('Delete Column')],
                # [sg.Button('Manage Patients')],
                # [sg.Button('Manage Doctors')],
                # [sg.Button('Manage OutPatient Appointments')],
                # [sg.Button('Manage InPatient Appointments')],
                # [sg.Button('Manage Diseases')],
                [sg.Button('Manage Treatments')],
                # [sg.Button('Manage Rooms')],
                # [sg.Button('Manage Staff')],
                # [sg.Button('Manage Room Assignments')],
                # [sg.Button('Manage Bills')]
                ]
layoutViewNum = [[sg.Text(key='PatientNum')],
                 [sg.Text(key='DoctorNum')],
                 [sg.Text(key='StaffNum')],
                 [sg.Text(key='RoomNum')],
                 [sg.Text(key='RoomAssNum')],
                 [sg.Text(key='DiseaseNum')],
                 [sg.Text(key='TreatmentNum')],
                 [sg.Text(key='AppointmentNum')],
                 [sg.Text(key='BillNum')]]
# layoutManagePatient = [[sg.Button('View Patients')],
#     #                    [sg.Button('Add Patient')],
#     #                    [sg.Button('Update Patient')],
#     #                    [sg.Button('Delete Patient')],
#                        [sg.Button('Back to Admin Menu')]
# ]
layoutManageDoctor = [[sg.Button('View Doctors')],
                      [sg.Button('Add Doctor')],
                      [sg.Button('Update Doctor')],
                      [sg.Button('Delete Doctor')],
                      [sg.Button('Back to Admin Menu')]]
layoutManageOutPatientApp = [[sg.Button('View OutPatient Appointments')],
                             [sg.Button('Add OutPatient Appointment')],
                             [sg.Button('Update OutPatient Appointment')],
                             [sg.Button('Delete OutPatient Appointment')],
                             [sg.Button('Back to Admin Menu')]]
layoutManageInPatientApp = [[sg.Button('View InPatient Appointments')],
                            [sg.Button('Add InPatient Appointment')],
                            [sg.Button('Update InPatient Appointment')],
                            [sg.Button('Delete InPatient Appointment')],
                            [sg.Button('Back to Admin Menu')]]
layoutManageDisease = [[sg.Button('View Diseases')],
                       [sg.Button('Add Disease')],
                       [sg.Button('Update Disease')],
                       [sg.Button('Delete Disease')],
                       [sg.Button('Back to Admin Menu')]]
layoutManageTreatment = [[sg.Button('View Treatments By Order', key="ViewTreatmentsOrder")],
                         # [sg.Button('Add Treatment')],
                         # [sg.Button('Update Treatment')],
                         # [sg.Button('Delete Treatment')],
                         # [sg.Button('Back to Admin Menu')]
                         ]
layoutManageRoom = [[sg.Button('View Rooms')],
                    [sg.Button('Add Room')],
                    [sg.Button('Update Room')],
                    [sg.Button('Delete Room')],
                    [sg.Button('Back to Admin Menu')]]
layoutManageStaff = [[sg.Button('View Staffs')],
                     [sg.Button('Add Staff')],
                     [sg.Button('Update Staff')],
                     [sg.Button('Delete Staff')],
                     [sg.Button('Back to Admin Menu')]]
layoutManageRoomAssignments = [[sg.Button('View Room Assignments')],
                               [sg.Button('Assign a Room')],
                               [sg.Button('Update Room Assignment')],
                               [sg.Button('Delete Room Assignment')],
                               [sg.Button('Back to Admin Menu')]]
layoutManageBill = [[sg.Button('View Bills')],
                    [sg.Button('Add Bill')],
                    [sg.Button('Update Bill')],
                    [sg.Button('Delete Bill')],
                    [sg.Button('Back to Admin Menu')]]
layoutAdministration = [[sg.Button('Add New User')],
                        [sg.Button('Drop User')],
                        [sg.Button('Grant Permissions')]]
layoutAddNewUser = [[sg.Text('Enter Username'), sg.Input(key='-InputUsername-')],
                    [sg.Text('Enter Password'), sg.Input(key='-InputPassword-')],
                    [sg.Button('Add User')],
                    [sg.Text(key='-AddUserError-', text_color='Red', font=('Helvetica', 15))],
                    [sg.Text(key='-AddUserSuccess-', text_color='Lightgreen', font=('Helvetica', 15))]]
layoutDropUser = [[sg.Text('Enter Username'), sg.Input(key='-InputUsernameDrop-')],
                  [sg.Button('Drop')],
                  [sg.Text(key='-DropUserError-', text_color='Red', font=('Helvetica', 15))],
                  [sg.Text(key='-DropUserSuccess-', text_color='Lightgreen', font=('Helvetica', 15))]]
layoutGrantPermissions = [[sg.Text('Enter Username'), sg.Input(key='-InputUsernameGrant-')],
                          [sg.Text()],
                          [sg.Text('Grant All Privileges')],
                          [sg.Radio('ALL PRIVILEGES', 1, key='-AP-', enable_events=True), sg.Button('Reset')],
                          # [sg.Checkbox('ALL PRIVILEGES', 1, key='-AP-')],
                          [sg.Text('or Select from below')],
                          [sg.Checkbox('SELECT', key='-SELECT-'), sg.Checkbox('INSERT', key='-INSERT-')],
                          [sg.Checkbox('DROP', key='-DROP-'), sg.Checkbox('CREATE', key='-CREATE-')],
                          [sg.Checkbox('DELETE', key='-DELETE-'), sg.Checkbox('UPDATE', key='-UPDATE-')],
                          [sg.Checkbox('GRANT OPTION', key='-GRANTOPTION-')],
                          [sg.Text('Choose all tables')],
                          [sg.Radio('All Tables', 2, key='-AT-', enable_events=True),
                           sg.Button('Reset', key='-ResetTables-')],
                          [sg.Text('or select from below')],
                          [sg.Checkbox('Patient', key='-Patient-'), sg.Checkbox('Doctor', key='-Doctor-')],
                          [sg.Checkbox('Room', key='-Room-'), sg.Checkbox('Staff', key='-Staff-')],
                          [sg.Checkbox('Room Assignments', key='-RoomAss-'), sg.Checkbox('Disease', key='-Disease-')],
                          [sg.Checkbox('Treatment', key='-Treatment-'),
                           sg.Checkbox('Appointment', key='-Appointment-')],
                          [sg.Checkbox('Bill', key='-Bill-')],
                          [sg.Button('Grant')],
                          [sg.Text(key='-GrantError-', text_color='Red', font=('Helvetica', 15))],
                          [sg.Text(key='-GrantSuccess-', text_color='Lightgreen', font=('Helvetica', 15))]]
# layoutViewPatients = [[sg.Button('View All')],
#                       [sg.Button('View By ID')],
#                       [sg.Button('View By Email')]]

viewpatientsdata = [
    [1, "abc", "def", "2021-10-21", "Male", "abc@gmail.com", "605098765", 169, 150, "SD-57069", "234-45-456"]]
viewpatientsheading = ["Patient ID", "First Name", "Last Name", "Birst Date", "Gender", "Email", "Phone Number",
                       "Height (cm)", "Weight (pounds)", "Address", "SSN"]
viewroomdata = [[101, "abc", "ed", "ed", "ed", 100.00]]
viewroomhead = ["Room ID", "Room Name", "Room Type", "Room Description", "Hospital Name", "Room Cost"]
layoutManageTables = [[sg.Text('Choose Table to update or delete:')],
                      [sg.Radio('Patient', 1, key='Patient', enable_events=True)],
                      # [sg.Radio('Doctor', 1, key='Doctor', enable_events=True)],
                      # [sg.Radio('Staff', 1, key='Staff', enable_events=True)],
                      [sg.Radio('Room', 1, key='Room', enable_events=True)],
                      # [sg.Radio('Room Assignments', 1, key='RoomAssignments', enable_events=True)],
                      # [sg.Radio('Disease', 1, key='Disease', enable_events=True)],
                      # [sg.Radio('Treatment', 1, key='Treatment', enable_events=True)],
                      # [sg.Radio('Appointment', 1, key='Appointment', enable_events=True)],
                      # [sg.Radio('Bill', 1, key='Bill', enable_events=True)],
                      [sg.Table(values=viewpatientsdata, headings=viewpatientsheading,
                                # max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                # display_row_numbers=True,
                                justification='right',
                                num_rows=0,
                                alternating_row_color='black',
                                key='-viewpatienttable-',
                                row_height=25, visible=False)],
                      [sg.Table(values=viewroomdata, headings=viewroomhead,
                                # max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                # display_row_numbers=True,
                                justification='right',
                                num_rows=0,
                                alternating_row_color='black',
                                key='-viewroomtable-',
                                row_height=25, visible=False)],
                      [sg.Text('Enter ID to update or delete:', key="idupdel", visible=False),
                       sg.Input(key='-PRID-', visible=False), sg.Button('Update', key='BtnUpdate', visible=False),
                       sg.Button('Delete', key='BtnDelete', visible=False)],
                      [sg.Text('Enter height:', key='upheight', visible=False),
                       sg.Input(key="upheightinput", visible=False)],
                      [sg.Text('Enter weight:', key='upweight', visible=False),
                       sg.Input(key="upweightinput", visible=False)],
                      [sg.Button('Update', key="BtnUpdateP", visible=False)],
                      [sg.Text('Enter room cost:', key='uprcost', visible=False),
                       sg.Input(key="uprcostinput", visible=False)],
                      [sg.Button('Update', key='BtnUpdateR', visible=False)],
                      [sg.Text(key="updelerror", text_color="Red")],
                      [sg.Text(key="updelsuccess", text_color="Lightgreen")]]
treatmentorderdata = [["abc", "def", "ghi", "jkl", 0.5]]
treatmentorderheadings = ["Treatment Name", "Treatment Description", "treatment Cost", "Disease Name", "Death Rate"]
layoutViewTreatmentsOrder = [
    [sg.Text('Treatments by ordering treatment cost in ascending and death rate in descending')],
    [sg.Text('', key='-messtreatorder-', font=('Helvetica', 15))],
    [sg.Table(values=treatmentorderdata, headings=treatmentorderheadings,
              # max_col_width=25,
              background_color='black',
              auto_size_columns=True,
              # display_row_numbers=True,
              justification='right',
              num_rows=0,
              alternating_row_color='black',
              key='-treatordertable-',
              row_height=25, visible=False)]]
layoutDeleteColumn = [[sg.Table(values=viewroomdata, headings=viewroomhead,
                                # max_col_width=25,
                                background_color='black',
                                auto_size_columns=True,
                                # display_row_numbers=True,
                                justification='right',
                                num_rows=0,
                                alternating_row_color='black',
                                key='-viewroomdeltable-',
                                row_height=25, visible=False)],
                      [sg.Text('Deleting "Hospital Name" column from table Room')],
                      [sg.Button('Go Ahead', key="yes"), sg.Button('Cancel')],
                      [sg.Text(key='delcolerror', text_color='Red')],
                      [sg.Text(key='delcolsuccess', text_color='Lightgreen')]]

# user layouts
layoutUser = [[sg.Text('Enter Username'), sg.Input(key='-InputUsernameLogin-')],
              [sg.Text('Enter Password'), sg.Input(key='-InputPasswordLogin-', password_char='*')],
              [sg.Button('Login')],
              [sg.Text(key='-LoginError-', text_color='Red', font=('Helvetica', 15))]]
layoutUserMain = [[sg.Text('', key='-welcomemessage-', font=('Helvetica', 15))],
                  [sg.Button('View Appointments', key='ViewAppUser')],
                  [sg.Button('View Staff by Room', key='ViewStaffRoomUser')],
                  [sg.Button('View Patient Contact Info', key='ViewPatInfoUser')],
                  [sg.Button('View Patients Above Age', key='ViewPatAgeUser')]]
data = [["John", "test", "4654546565", "drer", "rtrtr", 101, "ward", '2021-34-34']]
# data=[[]]
headings = ["Patient Full Name", "Email", "Phone Number", "Disease", "Treatment", "Room No", "Room Name", "Start Date"]
layoutViewAppointmentsUser = [[sg.Text('', key='-mess-', font=('Helvetica', 15))],
                              [sg.Table(values=data, headings=headings,
                                        # max_col_width=25,
                                        background_color='black',
                                        auto_size_columns=True,
                                        # display_row_numbers=True,
                                        justification='right',
                                        num_rows=1,
                                        alternating_row_color='black',
                                        key='-apptable-',
                                        row_height=25)]]
ViewStaffRoomUserData = [["tes", "tes", "9342374837"]]
ViewStaffRoomUserHeadings = ["Staff Full Name", "Email", "Phone Number"]
layoutViewStaffRoomUser = [
    [sg.Text('Enter Room Number:'), sg.Input(key='-InputRoomNoUser-'), sg.Button('View Staff', key='BtnRoomsUser')],
    [sg.Text('', key='-messstaffroomuser-', font=('Helvetica', 15))],
    [sg.Table(values=ViewStaffRoomUserData, headings=ViewStaffRoomUserHeadings,
              # max_col_width=25,
              background_color='black',
              auto_size_columns=True,
              # display_row_numbers=True,
              justification='right',
              num_rows=0,
              alternating_row_color='black',
              key='-stafftable-',
              row_height=25, visible=False)]]
patinfodata = [["abc", "def", "ghi"]]
patinfoheadings = ["Full Name", "Email", "Phone Number"]
layoutViewPatInfoUser = [[sg.Text("View Patient's contact information by First Name, Last Name or ID")],
                         [sg.Text('Enter ID:'), sg.Input(key='-InputPatID-')],
                         [sg.Text('or Enter First Name:'), sg.Input(key='-InputPatFN-')],
                         [sg.Text('or Enter Last Name:'), sg.Input(key='-InputPatLN-')],
                         [sg.Button('Get Info', key='BtnPatInfoUser')],
                         [sg.Text('', key='-messpatinfouser-', font=('Helvetica', 15))],
                         [sg.Table(values=patinfodata, headings=patinfoheadings,
                                   # max_col_width=25,
                                   background_color='black',
                                   auto_size_columns=True,
                                   # display_row_numbers=True,
                                   justification='right',
                                   num_rows=0,
                                   alternating_row_color='black',
                                   key='-patinfotable-',
                                   row_height=25, visible=False)]
                         ]

patagedata = [["abc", 26]]
patageheadings = ["Full Name", "Age"]
layoutViewPatAgeUser = [
    [sg.Text('Enter Age:'), sg.Input(key='-InputAgeUser-'), sg.Button('View Patients', key='BtnPatAgeUser')],
    [sg.Text('', key='-messpatageuser-', font=('Helvetica', 15))],
    [sg.Table(values=patagedata, headings=patageheadings,
              # max_col_width=25,
              background_color='black',
              auto_size_columns=True,
              # display_row_numbers=True,
              justification='right',
              num_rows=0,
              alternating_row_color='black',
              key='-patagetable-',
              row_height=25, visible=False)]
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
     sg.Column(layoutManageDoctor, visible=False, key='-COLManageDoctors-'),
     sg.Column(layoutManageOutPatientApp, visible=False, key='-COLManageOutPatientAppointments-'),
     sg.Column(layoutManageInPatientApp, visible=False, key='-COLManageInPatientAppointments-'),
     sg.Column(layoutManageDisease, visible=False, key='-COLManageDiseases-'),
     sg.Column(layoutManageTreatment, visible=False, key='-COLManageTreatments-'),
     sg.Column(layoutManageRoom, visible=False, key='-COLManageRooms-'),
     sg.Column(layoutManageStaff, visible=False, key='-COLManageStaff-'),
     sg.Column(layoutManageRoomAssignments, visible=False, key='-COLManageRoomAssignments-'),
     sg.Column(layoutManageBill, visible=False, key='-COLManageBills-'),
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
    [sg.Button('Main'), sg.Button('Exit')]]

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
        if event == 'Delete Column':
            res = room.view_all()
            window['-viewroomdeltable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
    elif event == "yes":
        res = room.delete_column()
        if res:
            window['delcolsuccess'].update('Deleted column successfully')
            res = room.view_all()
            window['-viewroomdeltable-'].update(values=[list(ele) for ele in res], num_rows=len(res), visible=True)
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
                else:
                    window['updelerror'].update("Couldn't delete the record")
            elif values['Room']:
                res = room.delete_room(prid)
                if res:
                    window['updelsuccess'].update('Deleted successfully..!!')
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
