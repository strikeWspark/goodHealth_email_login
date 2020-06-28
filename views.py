from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse 
import sqlite3
from datetime import datetime
import re
import smtplib
import email.utils
from email.mime.text import MIMEText
import random
import math

  

def myView(request):
	return render(request,'email.html')


def mysendotp(request):
	flag = 0
	entered_email = request.POST['email']
	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	if(re.search(regex,entered_email)):
		conn = sqlite3.connect('sign_up_dbase.db')
		result = (conn.execute("SELECT Email FROM Register;"))
		for i in result:
				print(i[0])
				if(entered_email == i[0]):
					flag = 1
	else:
		return HttpResponse("Invalid Email")				
				
	if(flag == 1):
		print(entered_email)
		sendmail(entered_email)
		return render(request,'enter_otp.html')
	else:
		return HttpResponse("You're not allowed to login")	
	
	

def mysubmitotp(request): 
	today = datetime.now()
	creationTime = datetime.now()
	email = request.POST['email']
	otp = (request.POST['otp'])
	SUCCESS_MESSAGE = "<h1>Welcome "+ email + "</h1>"
	INCORRECT_OTP = "Incorrect OTP !!!"
	
	conn = sqlite3.connect('sign_up_dbase.db')
	cursor1 = conn.cursor()
	print(real_otp)
	print("databse openned ")
	today = datetime.now().strftime('%y-%m-%d %H:%M:%S')
	cursor1.execute("""INSERT INTO OTPVerifier(OTP,Email,Creation_time) VALUES(?,?,?)""",(real_otp,email,today))
	conn.commit()
	print("Record added")
	
	if(otp == real_otp):
		print("you entered the right otp")
		
	else:
		print("Incorrect otp")
		return HttpResponse(INCORRECT_OTP)
#	string = ""  string[:19]
	
	query = "SELECT Creation_time FROM OTPVerifier WHERE Email ='"+email+ "' LIMIT 1;"
	result = conn.execute(query)
	for i in result:
#		string = i
		creationTime = i[0]
	
		print(i[0])
	
	#diff = 	formatDateTime(today) - formatDateTime(creationTime)
	#print(diff)
	#print(creationTime[:19])
	name = ""
	username = conn.execute("SELECT NAME FROM Register WHERE Email ='"+email+ "' LIMIT 1;")
	for i in username:
		name = i[0]
	cursor1.close()
	conn.close()
	
	return HttpResponse(SUCCESS_MESSAGE +"<h1>"+ name + "</h1>")

def formatDateTime(dateTimeStr):
	strippedDateTime = dateTimeStr[:19]
	return datetime.strptime(strippedDateTime, '%y-%m-%d %H:%M:%S')

def  otpgenerator():
	digits = [i for i in range(0,10)]
	global real_otp
	random_str = ""
	
	for i in range(6):
		i = math.floor(random.random() * 10)
		random_str += str(digits[i])
	
	real_otp = random_str
	#print(random_str)
	
	return random_str


def sendmail(email):
	sender = "your_usernme"
	receiver = [email]
	otp = otpgenerator()
	message = "Your OTP is : " + str(otp)

	#msg = MIMEText(message)
	#msg['To'] = email.utils.formataddr(('Recipient', receiver)) 
	#msg['From'] = email.utils.formataddr(('Author', sender))
	#msg['Subject'] = 'OTP for your login'

	try:
		smtp_obj = smtplib.SMTP('smtp.gmail.com:587')
		smtp_obj.ehlo()
		#smtp_obj.set_debuglevel(True)
		smtp_obj.starttls()
		smtp_obj.login(sender, "passowrd")
		smtp_obj.sendmail(sender, receiver, message)
		print("OTP sent successfully")
	except Exception as error:
		print(error)
		print("Error while sending otp")
	finally:
		smtp_obj.quit()

real_otp = 0		