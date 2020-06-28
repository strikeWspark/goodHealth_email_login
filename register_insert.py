import sqlite3

conn = sqlite3.connect('sign_up_dbase.db')
print("Datbase openned")
cursor1 = conn.cursor()
#conn.execute("INSERT INTO Register \
#(NAME,Password,Mobile,Email) VALUES('SAURABH','qwerty','789654130','tripathi@gmail.com')")
#conn.execute("INSERT INTO Register \
#(NAME,Password,Mobile,Email) VALUES('SAURABH','qwerty','789654130','gtpstripathi@gmail.com')")
#conn.execute("INSERT INTO Register \
#(NAME,Password,Mobile,Email) VALUES('SAURABH','qwerty','789654130','shubhtripathiji@gmail.com')")
#conn.execute("INSERT INTO Register \
#(NAME,Password,Mobile,Email) VALUES('Alfredo','@123#','7866641307','kstripathi7@gmail.com')")

conn.commit()
print("Record added successfully")

result = (conn.execute("SELECT Email FROM Register;"))
for i in result:
    print(i[0])
cursor1.close()
conn.close()