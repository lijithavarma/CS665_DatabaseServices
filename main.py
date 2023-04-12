from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPlainTextEdit
import sys
import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost", user="root", password="P@ssw0rd1230909", database="employeemanagementsystemdb")

app = QApplication(sys.argv)

w = QWidget()
w.resize(900, 600)
w.setWindowTitle("Employee Management System")

textbox = QPlainTextEdit(w)
textbox.move(240, 20)
textbox.resize(650, 560)
textbox.show()

def on_click_button1():
	mycursor = mydb.cursor()
	mycursor.execute("select * from employee")
	myresult = mycursor.fetchall()
	result = "id\tuser_id\trole_id\tdepartment_id\tstatus\tnote\tcode\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Employee Table\n\n" + result)

def on_click_button2():
	mycursor = mydb.cursor()
	mycursor.execute("select * from user")
	myresult = mycursor.fetchall()
	result = "id\trole_id\tfirstName\tlastName\tusername\temail\t\tdob\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("User Table\n\n" + result)

def on_click_button3():
	mycursor = mydb.cursor()
	mycursor.execute("select * from role")
	myresult = mycursor.fetchall()
	result = "id\ttitle\tdescription\ttype\tcontent\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Role Table\n\n" + result)

def on_click_button4():
	mycursor = mydb.cursor()
	mycursor.execute("select * from organization")
	myresult = mycursor.fetchall()
	result = "id\ttitle\tsummary\tstatus\tcontent\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Organization Table\n\n" + result)

def on_click_button5():
	mycursor = mydb.cursor()
	mycursor.execute("select id from user")
	user_id = mycursor.fetchall()
	mycursor.execute("select id from organization")
	organization_id = mycursor.fetchall()
	mycursor.execute("select id from role")
	role_id = mycursor.fetchall()

	mycursor = mydb.cursor()
	sql = "insert into employee (user_id, role_id, department_id, status, note, code) values (%s, %s, %s, %s, %s, %s)"
	val = (user_id[random.randint(0, len(user_id) - 1)][0], role_id[random.randint(0, len(role_id) - 1)][0], organization_id[random.randint(0, len(organization_id) - 1)][0], random.randint(1,10), "employee", "code")
	mycursor.execute(sql, val)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from employee")
	myresult = mycursor.fetchall()
	result = "id\tuser_id\trole_id\tdepartment_id\tstatus\tnote\tcode\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Employee Table\n\n" + result)

def on_click_button6():
	mycursor = mydb.cursor()
	mycursor.execute("select id from role")
	role_id = mycursor.fetchall()

	sql = "insert into user (role_id, first_name, last_name, username, email, dob) values (%s, %s, %s, %s, %s, %s)"
	num = random.randint(1, 100)
	year = random.randint(1980, 2000)
	val = (role_id[random.randint(0, len(role_id) - 1)][0], "firstname", "lastname" + str(num), "fl" + str(num), "fl" + str(year) + "@gmail.com", str(year) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(1, 28)))

	mycursor.execute(sql, val)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from user")
	myresult = mycursor.fetchall()
	result = "id\trole_id\tfirstName\tlastName\tusername\temail\t\tdob\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("User Table\n\n" + result)

def on_click_button7():
	mycursor = mydb.cursor()
	sql = "insert into role (title, description, type, content) values (%s, %s, %s, %s)"
	val = ("Manager", "executive level", "Executive", "This is another manager")
	mycursor.execute(sql, val)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from role")
	myresult = mycursor.fetchall()
	result = "id\ttitle\tdescription\ttype\tcontent\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Role Table\n\n" + result)

def on_click_button8():
	mycursor = mydb.cursor()
	sql = "insert into organization (title, summary, status, content) values (%s, %s, %s, %s)"
	val = ("Organization", "org", random.randint(1, 10), "This is organizaton")
	mycursor.execute(sql, val)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from organization")
	myresult = mycursor.fetchall()
	result = "id\ttitle\tsummary\tstatus\tcontent\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Organization Table\n\n" + result)

def on_click_button9():
	mycursor = mydb.cursor()
	sql = "delete from employee where code='code'"
	mycursor.execute(sql)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from employee")
	myresult = mycursor.fetchall()
	result = "id\tuser_id\trole_id\tdepartment_id\tstatus\tnote\tcode\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Employee Table\n\n" + result)

def on_click_button10():
	mycursor = mydb.cursor()
	sql = "delete from user where first_name='firstname'"
	mycursor.execute(sql)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from user")
	myresult = mycursor.fetchall()
	result = "id\trole_id\tfirstName\tlastName\tusername\temail\t\tdob\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("User Table\n\n" + result)

def on_click_button11():
	mycursor = mydb.cursor()
	sql = "delete from role where content='This is another manager'"
	mycursor.execute(sql)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from role")
	myresult = mycursor.fetchall()
	result = "id\ttitle\tdescription\ttype\tcontent\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Role Table\n\n" + result)

def on_click_button12():
	mycursor = mydb.cursor()
	sql = "delete from organization where title='Organization'"
	mycursor.execute(sql)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from organization")
	myresult = mycursor.fetchall()
	result = "id\ttitle\tsummary\tstatus\tcontent\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("Organization Table\n\n" + result)

def on_click_button13():
	print("haha")
	mycursor = mydb.cursor()
	sql = "update user set first_name='David' where first_name='John'"
	mycursor.execute(sql)
	mydb.commit()

	mycursor = mydb.cursor()
	mycursor.execute("select * from user")
	myresult = mycursor.fetchall()
	result = "id\trole_id\tfirstName\tlastName\tusername\temail\t\tdob\n"
	for x in myresult:
		for y in x:
			result += str(y) + "\t"
		result += "\n"
	textbox.setPlainText("User Table\n\n" + result)

label1 = QLabel(w)
label1.setText('Read Employee Table')
label1.move(20, 20)
label1.show()

button1 = QPushButton(w)
button1.setText('Click')
button1.move(140, 17)
button1.show()

label2 = QLabel(w)
label2.setText('Read User Table')
label2.move(20, 48)
label2.show()

button2 = QPushButton(w)
button2.setText('Click')
button2.move(140, 45)
button2.show()

label3 = QLabel(w)
label3.setText('Read Role Table')
label3.move(20, 76)
label3.show()

button3 = QPushButton(w)
button3.setText('Click')
button3.move(140, 73)
button3.show()

label4 = QLabel(w)
label4.setText('Read Organization Table')
label4.move(20, 104)
label4.show()

button4 = QPushButton(w)
button4.setText('Click')
button4.move(140, 101)
button4.show()

label5 = QLabel(w)
label5.setText('Insert 1 column in employee table')
label5.setWordWrap(True)
label5.move(20, 132)
label5.show()

button5 = QPushButton(w)
button5.setText('Click')
button5.move(140, 129)
button5.show()

label6 = QLabel(w)
label6.setText('Insert 1 column in user table')
label6.setWordWrap(True)
label6.move(20, 165)
label6.show()

button6 = QPushButton(w)
button6.setText('Click')
button6.move(140, 162)
button6.show()

label7 = QLabel(w)
label7.setText('Insert 1 column in role table')
label7.setWordWrap(True)
label7.move(20, 198)
label7.show()

button7 = QPushButton(w)
button7.setText('Click')
button7.move(140, 195)
button7.show()

label8 = QLabel(w)
label8.setText('Insert 1 column in organization table')
label8.setWordWrap(True)
label8.move(20, 231)
label8.show()

button8 = QPushButton(w)
button8.setText('Click')
button8.move(140, 228)
button8.show()

label9 = QLabel(w)
label9.setText('Delete 1 column in employee table')
label9.setWordWrap(True)
label9.move(20, 265)
label9.show()

button9 = QPushButton(w)
button9.setText('Click')
button9.move(140, 262)
button9.show()

label10 = QLabel(w)
label10.setText('Delete 1 column in user table')
label10.setWordWrap(True)
label10.move(20, 297)
label10.show()

button10 = QPushButton(w)
button10.setText('Click')
button10.move(140, 294)
button10.show()

label11 = QLabel(w)
label11.setText('Delete 1 column in role table')
label11.setWordWrap(True)
label11.move(20, 330)
label11.show()

button11 = QPushButton(w)
button11.setText('Click')
button11.move(140, 327)
button11.show()

label12 = QLabel(w)
label12.setText('Delete 1 column in organization table')
label12.setWordWrap(True)
label12.move(20, 363)
label12.show()

button12 = QPushButton(w)
button12.setText('Click')
button12.move(140, 360)
button12.show()

label13 = QLabel(w)
label13.setText('Update firstName "John" to "David" in user table')
label13.setWordWrap(True)
label13.move(20, 395)
label13.resize(100, 35)
label13.show()

button13 = QPushButton(w)
button13.setText('Click')
button13.move(140, 392)
button13.show()

button1.clicked.connect(on_click_button1)
button2.clicked.connect(on_click_button2)
button3.clicked.connect(on_click_button3)
button4.clicked.connect(on_click_button4)
button5.clicked.connect(on_click_button5)
button6.clicked.connect(on_click_button6)
button7.clicked.connect(on_click_button7)
button8.clicked.connect(on_click_button8)
button9.clicked.connect(on_click_button9)
button10.clicked.connect(on_click_button10)
button11.clicked.connect(on_click_button11)
button12.clicked.connect(on_click_button12)
button13.clicked.connect(on_click_button13)

w.show()

app.exec_()