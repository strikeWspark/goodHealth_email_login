import sqlite3
from datetime import datetime

conn = sqlite3.connect('sign_up_dbase.db')
cursor1 = conn.cursor()
print("databse openned ")
a= 123786
today = datetime.now()
cursor1.execute("""INSERT INTO OTPVerifier(OTP,Email,Creation_time) VALUES(?,?,?)""",(a,'test@gmail.com',today))
conn.commit()
print("Record added")

result = (conn.execute("SELECT * FROM OTPVerifier;"))
for i in result:
    print(i)
cursor1.close()
conn.close()
