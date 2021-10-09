import os
import pipes
from os.path import exists

# file_exists = exists(path_to_file)
# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databases names one on each line and assigned to DB_NAME variable.
import credentials


def backup():
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_USER_PASSWORD = credentials.PASSWORD
    # DB_NAME = '/backup/dbnameslist.txt'
    DB_NAME = 'HospitalManagementSystem'
    # BACKUP_PATH = '/Users/mohankrishnatummala/Documents/Viju/Info Retrieval/Assignments/Project/HMS'
    BACKUP_Path = './'
    # Getting current DateTime to create the separate backup folder like "20180817-123433".
    # DATETIME = time.strftime('%Y%m%d-%H%M%S')
    # TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

    db = DB_NAME
    dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(
        BACKUP_Path) + "/" + db + ".sql"
    os.system(dumpcmd)
    # gzipcmd = "gzip " + pipes.quote(BACKUP_Path) + "/" + db + ".sql"
    # os.system(gzipcmd)

    print("")
    print("Backup script completed")
    print("Your backups have been created in '" + BACKUP_Path + "' directory")


def restore():
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_USER_PASSWORD = credentials.PASSWORD
    # DB_NAME = '/backup/dbnameslist.txt'
    DB_NAME = 'HospitalManagementSystem'
    # BACKUP_PATH = '/Users/mohankrishnatummala/Documents/Viju/Info Retrieval/Assignments/Project/HMS'
    BACKUP_Path = './'
    # Getting current DateTime to create the separate backup folder like "20180817-123433".
    # DATETIME = time.strftime('%Y%m%d-%H%M%S')
    # TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

    file_exists = exists(BACKUP_Path + "/" + DB_NAME + ".sql")
    if file_exists:
        db = DB_NAME
        # dumpcmd = "mysql -u " + DB_USER + " -h " + DB_HOST + " '" + DB_USER + "$" + DB_NAME + "'  < "+DB_NAME+".sql"
        dumpcmd = "mysql -h " + DB_HOST + " -u " + DB_USER + " -p " + DB_USER_PASSWORD + " < " + db + ".sql"
        os.system(dumpcmd)
    else:
        print("Backup the database first to restore")
    # gzipcmd = "gzip " + pipes.quote(BACKUP_Path) + "/" + db + ".sql"
    # os.system(gzipcmd)

    print("")
    print("Backup script completed")
    print("Your backups have been created in '" + BACKUP_Path + "' directory")


# restore()
