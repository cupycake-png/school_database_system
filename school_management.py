import mysql.connector # import the module needed to connect to the database
import sys # sys for exiting the program
import os # os for clearing the terminal
import time # time for waiting - time.sleep()

"""You can use any MySQL database for this program, you'll need the mysql connector module to use it though.
You can install that by 'pip install mysql-connector' in command prompt, make sure you have pip in your PATH variables.
If you dont know to do that, i suggest searching it up.

You'll need to have your database set up in a specific way, since this program is only customisable by changing the actual code
and there is no setup to choose how you want your database to be.

Your database will need to have 2 tables, one called "student" and another called "teacher".
Each table will need 5 columns.

student: firstName, lastName, gender, age, class
teacher: firstName, lastName, gender, profession, class

They need to be spelt the same as i've done there. After you've setup your MySQL database you can connect it below. 
Change the 'host', 'user', 'passwd' and 'database' variable values to work with your database.
"""

# Connecting to the database
try:
	db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="password", database="testdb")
except:
	print("Cannot connect to database, please check the database credentials are correct and that you have a stable internet connection!")
	time.sleep(5)
	sys.exit()

# Create a cursor object
mycursor = db.cursor()

#mycursor.execute("INSERT INTO student (firstName, lastName, gender, age, class) VALUES ('Charlie', 'Moran', 'Male', 13, '9R')")
#-------------------------------------------------------------------------------------------------------------------------------#
# Classes of the students with their functions
class Student():
	def __init__(self): # On the construction method it asks for what you want to do inside the student class
		
		# os.system('cls' if os.name == 'nt' else 'clear') means clearing the terminal window
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Student choices:\n")
		print("1) Add Student\n2) Delete Student\n3) Search for Student\n4) See all Students\n5) Back to main\n")
		
		try:
			choice = int(input("\n>>> "))
		except:
			Student()


		if(choice == 1):
			Student.addStudent()

		elif(choice == 2):
			Student.deleteStudent()

		elif(choice == 3):
			Student.searchStudent()

		elif(choice == 4):
			Student.allStudents()

		elif(choice == 5):
			print('\n')
			ask()

		else:
			print('\n')
			Student()

	def addStudent():
		# Gets all the details and querys the database to insert the characters into the columns
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Add a Student.\n")

		firstName = str(input("First Name >>> "))
		lastName = str(input("Last Name >>> "))
		gender = str(input("Gender >>> "))

		try:
			age = int(input("Age >>> "))
		except:
			print('\nIncorrect value type for Age, please try again\n')
			time.sleep(1)
			Student()

		_class = str(input("Class >>> "))

		confirm = input("\nAre you sure the details are correct (y/n): ")

		if(confirm == "y" or confirm == "Y"):
			mycursor.execute('INSERT INTO student (firstName, lastName, gender, age, class) VALUES ("{}", "{}", "{}", "{}", "{}")'.format(firstName, lastName, gender, age, _class))
			db.commit()
			print('\n')
			Student()

		else:
			print('\n')
			print("NOT SAVED, NOT CONFIRMED")
			print('\n')
			time.sleep(2)
			Student()

	def deleteStudent():
		# Gets the details of the first and last name and deletes the row with those values
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Delete a Student.\n")

		firstName = str(input("First Name >>> "))
		lastName = str(input("Last Name >>> "))

		confirm = input("\nAre you sure the details are correct (y/n): ")

		if(confirm == "y" or confirm == "Y"):
			mycursor.execute('DELETE FROM student WHERE firstName = "{}" AND lastName = "{}"'.format(firstName, lastName))
			db.commit()
			print('\n')
			Student()

		else:
			print('\n')
			print("NOT SAVED, NOT CONFIRMED")
			print('\n')
			time.sleep(2)
			Student()

	def searchStudent():
		# Searches for students, i split this up into 5 parts for each category you could search
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Search for a Student.\n")
		print("Choices:\n1) First Name\n2) Last Name\n3) Gender\n4) Class\n5) Age\n6) Back to main")

		try:
			choice = int(input("\n>>> "))
		except:
			Student.searchStudent()

		if(choice == 1):
			# This is searching for students by the first name
			os.system('cls' if os.name == 'nt' else 'clear')
			firstName = str(input("First Name >>> "))
			
			mycursor.execute('SELECT * FROM student WHERE firstName = "{}"'.format(firstName))
			students = mycursor.fetchall()
			
			for row in students:
				print("Fullname:", row[0] + " " + row[1] + " | Class:", row[4])

			input('\n>>>')

			print('\n')
			Student()

		elif(choice == 2):
			# This is searching for students by the last name
			os.system('cls' if os.name == 'nt' else 'clear')
			lastName = str(input("Last Name >>> "))

			mycursor.execute('SELECT * FROM student WHERE lastName = "{}"'.format(lastName))
			students = mycursor.fetchall()
			
			for row in students:
				print("Fullname:", row[0] + " " + row[1] + " | Class:", row[4])

			input('\n>>>')

			print('\n')
			Student()

		elif(choice == 3):
			# This is searching for students by gender
			os.system('cls' if os.name == 'nt' else 'clear')
			gender = str(input("Gender >>> "))

			mycursor.execute('SELECT * FROM student WHERE gender = "{}"'.format(gender))
			students = mycursor.fetchall()
			
			for row in students:
				print("Fullname:", row[0] + " " + row[1] + " | Class:", row[4])

			input('\n>>>')

			print('\n')
			Student()

		elif(choice == 4):
			# This is searching for students by class
			os.system('cls' if os.name == 'nt' else 'clear')
			_class = str(input("Class >>> "))

			mycursor.execute('SELECT * FROM student WHERE class = "{}"'.format(_class))
			students = mycursor.fetchall()
			
			for row in students:
				print("Fullname:", row[0] + " " + row[1] + " | Class:", row[4])

			input('\n>>>')

			print('\n')
			Student()

		elif(choice == 5):
			# This is searching for students by age
			os.system('cls' if os.name == 'nt' else 'clear')

			try:
				age = int(input("Age >>> "))
			except:
				print('\nIncorrect value type, please try again\n')
				time.sleep(1)
				Student()


			mycursor.execute('SELECT * FROM student WHERE age = "{}"'.format(age))
			students = mycursor.fetchall()

			for row in students:
				print("Fullname:", row[0] + " " + row[1] + " | Class:", row[4])

			input('\n>>>')

			print('\n')
			Student()

		elif(choice == 6):
			print('\n')
			ask()

		else:
			print('\n')
			Student.searchStudent()

	def allStudents():
		# Returns all the students in the database
		os.system('cls' if os.name == 'nt' else 'clear')

		mycursor.execute("SELECT * FROM student")
		students = mycursor.fetchall()

		for row in students:
				print("Fullname:", row[0] + " " + row[1] + " | Class:", row[4])

		input('\n>>>')

		print('\n')
		Student()

#-------------------------------------------------------------------------------------------------------------------------------#
# Classes of teacher with the functions
class Teacher():
	# The teacher class is basically just a copy of the student class, just with one different thing (the profession instead of age)
	def __init__(self):
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Teacher choices:\n")
		print("1) Add Teacher\n2) Delete Teacher\n3) Search for Teacher\n4) See all Teachers\n5) Back to main\n")
		
		try:
			choice = int(input("\n>>> "))
		except:
			Teacher()

		if(choice == 1):
			Teacher.addTeacher()

		elif(choice == 2):
			Teacher.deleteTeacher()

		elif(choice == 3):
			Teacher.searchTeacher()

		elif(choice == 4):
			Teacher.allTeachers()

		elif(choice == 5):
			print('\n')
			ask()

		else:
			print('\n')
			Teacher()

	def addTeacher():
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Add a Teacher.\n")

		firstName = str(input("First Name >>> "))
		lastName = str(input("Last Name >>> "))
		gender = str(input("Gender >>> "))
		profession = str(input("Profession >>> "))
		_class = str(input("Class >>> "))

		confirm = input("\nAre you sure the details are correct (y/n): ")

		if(confirm == "y" or confirm == "Y"):
			mycursor.execute('INSERT INTO teacher (firstName, lastName, gender, profession, class) VALUES ("{}", "{}", "{}", "{}", "{}")'.format(firstName, lastName, gender, profession, _class))
			db.commit()
			print('\n')
			Teacher()

		else:
			print('\n')
			print("NOT SAVED, NOT CONFIRMED")
			print('\n')
			time.sleep(2)
			Teacher()

	def deleteTeacher():
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Delete a Teacher.\n")

		firstName = str(input("First Name >>> "))
		lastName = str(input("Last Name >>> "))

		confirm = input("\nAre you sure the details are correct (y/n): ")

		if(confirm == "y" or confirm == "Y"):
			mycursor.execute('DELETE FROM teacher WHERE firstName = "{}" AND lastName = "{}"'.format(firstName, lastName))
			db.commit()
			print('\n')
			Teacher()

		else:
			print('\n')
			print("NOT SAVED, NOT CONFIRMED")
			print('\n')
			time.sleep(2)
			Teacher()

	def searchTeacher():
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Search for a Teacher.\n")
		print("Choices:\n1) First Name\n2) Last Name\n3) Gender\n4) Class\n5) Profession\n6) Back to main")

		try:
			choice = int(input("\n>>> "))
		except:
			Teacher.searchTeacher()

		if(choice == 1):
			# This is searching for teachers by the first name
			os.system('cls' if os.name == 'nt' else 'clear')
			firstName = str(input("First Name >>> "))
			
			mycursor.execute('SELECT * FROM teacher WHERE firstName = "{}"'.format(firstName))
			teachers = mycursor.fetchall()
			
			for row in teachers:
				print("Fullname:", row[0] + " " + row[1] + " | Profession:", row[3])

			input('\n>>>')

			print('\n')
			Teacher()

		elif(choice == 2):
			# This is searching for teachers by the last name
			os.system('cls' if os.name == 'nt' else 'clear')
			lastName = str(input("Last Name >>> "))

			mycursor.execute('SELECT * FROM teacher WHERE lastName = "{}"'.format(lastName))
			teachers = mycursor.fetchall()
			
			for row in teachers:
				print("Fullname:", row[0] + " " + row[1] + " | Profession:", row[3])

			input('\n>>>')

			print('\n')
			Teacher()

		elif(choice == 3):
			# This is searching for teachers by gender
			os.system('cls' if os.name == 'nt' else 'clear')
			gender = str(input("Gender >>> "))

			mycursor.execute('SELECT * FROM teacher WHERE gender = "{}"'.format(gender))
			teachers = mycursor.fetchall()
			
			for row in teachers:
				print("Fullname:", row[0] + " " + row[1] + " | Profession:", row[3])

			input('\n>>>')

			print('\n')
			Teacher()

		elif(choice == 4):
			# This is searching for teachers by class
			os.system('cls' if os.name == 'nt' else 'clear')
			_class = str(input("Class >>> "))

			mycursor.execute('SELECT * FROM teacher WHERE class = "{}"'.format(_class))
			teachers = mycursor.fetchall()
			
			for row in teachers:
				print("Fullname:", row[0] + " " + row[1] + " | Profession:", row[3])

			input('\n>>>')

			print('\n')
			Teacher()

		elif(choice == 5):
			# This is searching for teachers by profession
			os.system('cls' if os.name == 'nt' else 'clear')
			profession = str(input("Profession >>> "))

			mycursor.execute('SELECT * FROM teacher WHERE profession = "{}"'.format(profession))
			teachers = mycursor.fetchall()

			for row in teachers:
				print("Fullname:", row[0] + " " + row[1] + " | Profession:", row[3])

			input('\n>>>')

			print('\n')
			Teacher()

		elif(choice == 6):
			print('\n')
			ask()

		else:
			print('\n')
			Teacher.searchTeacher()

	def allTeachers():
		os.system('cls' if os.name == 'nt' else 'clear')

		mycursor.execute("SELECT * FROM teacher")
		teachers = mycursor.fetchall()

		for row in teachers:
			print("Fullname:", row[0] + " " + row[1] + " | Profession:", row[3])

		input('\n>>>')

		print('\n')
		Teacher()

#-------------------------------------------------------------------------------------------------------------------------------#
os.system('cls' if os.name == 'nt' else 'clear')

# starts it and defines a ask function i can refer to when finished a section
def ask():
	os.system('cls' if os.name == 'nt' else 'clear')

	print("School Management System!")
	print('\n')


	print("Choices:\n1) Students\n2) Teachers\n3) Exit\n")

	try:
		choice = int(input("\n>>> "))
	except:
		ask()

	if(choice == 1):
		# Go down the student choices
		Student()

	elif(choice == 2):
		# Go down to teacher choices
		Teacher()

	elif(choice == 3):
		sys.exit()

	else:
		ask()

# call the function to start it up
ask()

# Just to be safe, save all the queries it has
db.commit()