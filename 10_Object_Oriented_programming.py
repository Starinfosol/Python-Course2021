########################################## Object-Oriented Programming ########################################################

# Solving a problem by creating objects is one of the most popular approaches in programming.
# This is called object-oriented programming.
# This concept focuses on using reusable code. (Implements DRY principle)

# class Number:
#     def sum(self):
#         return self.a + self.b


# num = Number()
# num.a = 52
# num.b = 24
# s = num.sum()
# print(s)

# ..................................................................................

# class RailwayForm:
#     formType = "RailwayForm"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")


# ShubhApplication = RailwayForm()
# ShubhApplication.name = "Shubham"
# ShubhApplication.train = "Pune expreess"
# ShubhApplication.printData()

############################################## OOP function working using class ####################################################

# class remote():
#     pass

# class Player:
#     def moveRight(self):
#         pass

#     def moveLeft(self):
#         pass

#     def moveTop(self):
#         pass

# remote1 = remote()
# Player1 = Player()

# if (remote1.isLeftPress()):
#     Player1.moveLeft()

# ..................................................


# ..................................................


########################################## copy code information ################################################

# Class
# A class is a blueprint for creating objects.

# The syntax of a class looks like this:

# Class Employee:		[classname is written in PascalCase]
# 	#methods & variables
# Object
# An object is an instantiation of a class. When class is defined, a template(info) is defined. Memory is allocated only after object instantiation.

# Objects of a given class can invoke the methods available to it without revealing the implementation details to the user.     #Abstraction & Encapsulation!
# Modelling a problem in OOPs

# We identify the following in our problem

# Noun -> Class -> Employee
# Adjective -> Attributes -> name,age,salary
# Verbs -> Methods -> getSalary(), increment()

# Class Attributes
# An attribute that belongs to the class rather than a particular object.
# Example:

# class Employee:
# 	company = "Google"	#Specific to each class
# harry = Employee()	#Object instantiation
# Shubham = Employee()	#Object instantiation
# print(harry.company)
# print(Shubham.company)
# Employee.company = "YouTube"	#changing class attribute
# print(harry.company)
# print(Shubham.company)

# ........................................................
##################### Instance Attributes##########################

# An attribute that belongs to the Instance (object)
# Assuming the class from the previous example:


# class Employee:
# 	company = "Google"	#Specific to each class
# harry = Employee()	#Object instantiation
# Shubham = Employee()	#Object instantiation

# harry.name = "Harry"
# harry.salary = 300

# Shubham.name = "Shubham verma"
# Shubham.salary = 500


# print("Company Name: ", str(harry.company))
# print("Employee Name: ", str(harry.name))
# print("Salary: ", harry.salary)

# print("Company Name: ", str(Shubham.company))
# print("Employee Name: ", str(Shubham.name))
# print("Salary: ", Shubham.salary)


# Employee.company = "YouTube"	#changing class attribute

# print("Company Name: ", str(harry.company))
# print("Employee Name: ", str(harry.name))
# print("Salary: ", harry.salary)

# print("Company Name: ", str(Shubham.company))
# print("Employee Name: ", str(Shubham.name))
# print("Salary: ", Shubham.salary)

# ......................instance class Attributes...................................................

# class Employee:
# 	company = "Google"
# 	salary = 100

# harry = Employee()	#Object instantiation
# Shubham = Employee()	#Object instantiation


# Employee.company = "YouTube"	#changing class attribute

# print(harry.salary)
# print(Shubham.salary)

# .................... Discribe - self ....................................................


# class Employee:
# 	company = "Google"
# 	def getSalary(self):
# 		print("Salary is 80k")

# Shubham = Employee()
# Shubham.getSalary()
# ............................

# class Employee:
# 	company = "Google"
# 	def getSalary(self):
# 		# print(f"Salary is {self.salary}")
# 		print(f"Salary for this employee working in {self.company} is {self.salary}")

# Shubham = Employee()
# Shubham.salary = 100000
# Shubham.getSalary()			# Employee.getSalary(Shubham)

# harry.name = “Harry”
# harry.salary = “30K”	#Adding instance attributes
# Note: Instance attributes take preference over class attributes during assignment and retrieval.

# harry.attribute1  :

# Is attribute1 present in object?
# Is attribute1 present in class?
# ‘self’ parameter

# self refers to the instance of the class.

# It is automatically passed with a function call from an object.

# harry.getSalary()

# here, self is harry and above line of code is equivalent to Employee.getSalary(harry)

# This function getsalary is defined as:

# class Employee:
# 	company = “Google”
# 	def getSalary(self):
# 		print(“Salary is not there”)
# Static method

# .............................. static mathod...................................................


# class Employee:
# 	company = "Google"
# 	def getSalary(self, signature):
# 		# print(f"Salary is {self.salary}")
# 		print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

# 	@staticmethod
# 	def greet():
# 		print("Good morning, sir")

#	@staticmethod
# 	def time():
# 		print("the time is .....clok")


# Shubham = Employee()
# Shubham.salary = 100000
# Shubham.getSalary("Thanks!")
# Shubham.greet()
# Shubham.time()

# ...............................................................................................
# Sometimes we need a function that doesn’t use the self-parameter. We can define a static method like this:

# @staticmethod	#decorator to mark greet as a static method
# def greet():
# 	print(“Hello user”)

###################################### constructor ################################################
# __init__() constructor

# __init__() is a special method which runs as soon as the object is created.

# __init__() method is also known as constructor.

# It takes self-argument and can also take further arguments.

# For Example:

# class Employee:
# 	def __init__(self,name):
# 		self.name = name
# 	def getSalary(self):
# 		#Some code…
# harry = Employee(“Harry”)	#Object can be instantiated using constructor like this!

# class Employee:
# 	company = "Google"

# 	def __init__(self, name, salary, subunit):
# 		self.name = name
# 		self.salary = salary
# 		self.subunit = subunit
# 		print("Employee is created!")

# 	def getDetails(self):
# 		print(f"The Name of the Employee is {self.name}")
# 		print(f"The Salary of the Employee is {self.salary}")
# 		print(f"The Subunit of the Employee is {self.subunit}")

# 	def getSalary(self, signature):
# 		# print(f"Salary is {self.salary}")
# 		print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

# 	@staticmethod
# 	def greet():
# 		print("Good morning, sir")

# 	@staticmethod
# 	def time():
# 		print("the time is .....clok")

# Shubham = Employee("Shubham verma", 100000, "You tube")
# Shubham.getDetails()

############################################### Practice Time #################################################

# 01 Q> Create a class programmer for storing information of a few programmers working at Microsoft.
# Let's practice.......

# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(f"The Name of the {self.company} Programmer is {self.name} and the Product is {self.product}")


# Shubham = Programmer("Shubham", "Skype")
# Lokesh = Programmer("Lokesh", "Github")
# Shubham.getInfo()
# Lokesh.getInfo()

###############################################################################################################

# 02 Q> Write a class calculator capable of finding square, cube and the square root of a number.
# Let's practice.......

# class Calculator:
#     def __init__(self, num):
#         self.number = num				# number or num ek hi bat h

#     def square(self):
#         print (f"The value of {self.number} square is {self.number**2}")

#     def squareRoot(self):
#         print (f"The value of {self.number} squareRoot is {self.number**0.5}")

#     def cube(self):
#         print (f"The value of {self.number} cube is {self.number**3}")

# a = Calculator(3)
# a.square()
# a.squareRoot()
# a.cube()

###############################################################################################################

# 03 Q> Create a class with a class attribute a; create an object from it and set a directly using object.a=0 Does this change the class attribute
# Let's practice.......

# class sample:
# 	a = "Shubham"

# obj = sample()
# obj.a = "vikky"
# # sample.a = "vikky"
# print(sample.a)
# print(obj.a)

###############################################################################################################

# 04 Q> Add a static method in problem 2 to greet the user with hello.
# Let's practice.......

# class Calculator:
#     def __init__(self, num):
#         self.number = num				# number or num ek hi bat h

#     def square(self):
#         print(f"The value of {self.number} square is {self.number**2}")

#     def squareRoot(self):
#         print(f"The value of {self.number} squareRoot is {self.number**0.5}")

#     def cube(self):
#         print(f"The value of {self.number} cube is {self.number**3}")

#     @staticmethod
#     def greet():
#         print("****************Hello there welcome to the best calcutator of the word!****************")


# a = Calculator(3)
# a.greet()
# a.square()
# a.squareRoot()
# a.cube()

###############################################################################################################

# 05 Q> Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.
# Let's practice.......

# class Train:
# 	def __init__(self, name, fare, seats):
# 		self.name = name
# 		self.fare = fare
# 		self.seats = seats

# 	def getStatus(self):
# 		print("***********************************************************")
# 		print(f"The Name of the train is {self.name}")
# 		print(f"The Seats Available in the train is {self.seats}")
# 		print("***********************************************************")

# 	def fareInfo(self):
# 		print(f"The Price of the ticket is Rs. {self.fare}")

# 	def bookTicket(self):
# 		if(self.seats>0):
# 			print(f"Your Ticket has been Booked! Your Seat number {self.seats}")
# 			self.seats = self.seats - 1
# 		else:
# 			print("Sorry train is full kaindly try in tatkal Ticket")

# 	def cancelTicket(self):
# 		pass

# intercity = Train("Intercity Express: 14015", 90, 300)
# intercity.getStatus()
# intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()

###############################################################################################################

# 06 Q> Can you change the self parameter inside a class to something else (say ‘harry’)? Try changing self to ‘slf’ or ‘harry’ and see the effects.
# Let's practice.......

# class sample:
# 	a = "Shubham"
# 	def __init__(jarvis, name):
# 		jarvis.name = name

# obj = sample("Shubham")
# print(obj.name)

# #....................................................

# class sample:
# 	a = "Shubham"
# 	def __init__(self, name):
# 		self.name = name

# obj = sample("Shubham")
# print(obj.name)

################################################# Done ########################################################
