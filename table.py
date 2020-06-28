import sqlite3

conn = sqlite3.connect('sign_up_dbase.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE Register
       (NAME          TEXT     NOT NULL,
       Password      CHAR(13) NOT NULL,
       Mobile NUMBER(10)      NOT NULL,
       Email       CHAR(35));''')
print(" Register Table created successfully")

conn.execute('''CREATE TABLE OTPVerifier
       (OTP     NUMBER(6)      NOT NULL,
       Email       CHAR(35),
       Creation_time DATETIME);''')
print("Table crated successfully")

conn.close()
