############################################ Inheritance & more on OOPs ####################################################

# Inheritance is a way of creating a new class from an existing class.
# Syntax:


# class Employee:                                 # Base class
#     company = "Google"

#     def logData(self):
#         print("The is your Details")

# class Programmer(Employee):                     # Derived or child class
#     language = "Python"

#     def getLanguage(self):
#         print(f"The language is {self.language} company name {self.company}")

# e = Employee()
# e.logData()
# p = Programmer()
# p.getLanguage()


# ...............................................................


# We can use the methods and attributes of Employee in Programmer object.

# Also, we can overwrite or add new attributes and methods in the Programmer class.

# Type of Inheritance
# **********************************
# Single inheritance
# Multiple inheritance
# Multilevel inheritance

# **********************************

# Single inheritance occurs when child class inherits only a single parent class.
# Base -> Derived

# class Employee:                                 # Base class
#     company = "Google"

#     def logData(self):
#         print("The is your Details")

# class Programmer(Employee):                     # Derived or child class
#     language = "Python"

#     def getLanguage(self):
#         print(f"The language is {self.language} company name {self.company}")

# e = Employee()
# e.logData()
# p = Programmer()
# p.getLanguage()

# ...........................................................................................

# Multiple Inheritance :-
# Multiple inheritance occurs when the child class inherits from more than one parent class.

# class Employee:                                               # Base class
#     company = "Google"
#     ecode = 231135

# class Freelancer:                                             # Base class
#     company = "Youtube"
#     level = 25

# class Programmer(Employee, Freelancer):                       # Derived or child class
#     language = "Python"

# p = Programmer()
# # print(p.ecode)
# # print(p.level)
# # print(p.language)
# print(p.company)

# ...........................................................................................

# Multilevel Inheritance
# When a child class becomes a parent for another child class.

# class Samsung:
#     company = "Google"
#     language = "Javascript"

# class Employee(Samsung):
#     ecode = 231135

# class Programmer(Employee):
#     language = "Python"

# s = Samsung()
# e = Employee()
# pr = Programmer()
# print(pr.company)

# ..................................................................................................
# Super() method
# Super method is used to access the methods of a super class in the derived class.
# super().__init__()  #Calls constructor of the base class


# class Samsung:
#     company = "Google"
#     def takebreath(self):
#         print("I am Breathing.........")

# class Employee(Samsung):
#     ecode = 231135
#     def takebreath(self):
#         print("I am an Employee and i am Breathing.........")

# class Programmer(Employee):
#     language = "Python"
#     def takebreath(self):
#         super().takebreath()
#         print("I am Programmer and Breathing + + + + + .........")

# s = Samsung()
# s.takebreath()

# e = Employee()
# e.takebreath()

# pr = Programmer()
# pr.takebreath()

# ..............................................................................


# class Samsung:
#     company = "Google"
#     def takebreath(self):
#         print("I am Breathing.........")

# class Employee(Samsung):
#     ecode = 231135
#     def takebreath(self):
#         super().takebreath()
#         print("I am an Employee and i am Breathing.........")

# class Programmer(Employee):
#     language = "Python"
#     def takebreath(self):
#         super().takebreath()
#         print("I am Programmer and Breathing + + + + + .........")

# s = Samsung()
# s.takebreath()

# e = Employee()
# e.takebreath()

# pr = Programmer()
# pr.takebreath()

# .....................................................................................


# class Samsung:
#     company = "Google"
#     def __init__(self):
#         print("Hello frd i am printing the function")

#     def takebreath(self):
#         print("I am Breathing.........")

# class Employee(Samsung):
#     ecode = 231135
#     def takebreath(self):
#         super().__init__()
#         print("I am an Employee and i am Breathing.........")

# class Programmer(Employee):
#     language = "Python"
#     def takebreath(self):
#         super().takebreath()
#         print("I am Programmer and Breathing + + + + + .........")

# pr = Programmer()
# pr.takebreath()

# ......................................................................................

# Class methods
# A class method is a method which is bound to the class and not the object of the class.

# class Employee:
#     company = "TCS"
#     salary = 100000
#     location = "Pune"

#     # def changeSalary(self, sal):
#     #     self.salary = sal
#         # self.__class__.salary = sal                   # change class salary

#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal

# e = Employee()
# print(e.salary)

# e.changeSalary(150000)

# print(e.salary)
# print(e.salary)

# .......................................................................................
# @classmethod decorator is used to create a class method.
# Syntax to create a class method:

# class Employee:
#     company = "BhartGess"
#     salary = 100000
#     salarybonus = 50000
#     location = "Pune"

#     @property
#     def totalSalary(self):
#         return self.salary + self.salarybonus

#     @totalSalary.setter
#     def totalSalary(self, val):
#         self.salarybonus = val - self.salary

# e = Employee()
# print(e.totalSalary)
# e.totalSalary = 158000
# print(e.salary)
# print(e.salarybonus)


# ...................................................................

# @classmethod
# def (cls, p1, p2):
# 	#code
# @property decorators

# Consider the following class

# class Employee:
# 	@property
# 	def name(self):
# 		return self.ename
# if e = Employee() is an object of class employee, we can print (e.name) top print the ename/call name() function.

# @.getters and @.setters

# The method name with @property decorator is called getter method.

# We can define a function + @name.setter decorator like below:


# class Employee:
#     company = "BhartGess"
#     salary = 100000
#     salarybonus = 50000
#     location = "Pune"

#     @property
#     def totalSalary(self):
#         return self.salary + self.salarybonus

#     @totalSalary.setter
#     def totalSalary(self, val):
#         self.salarybonus = val - self.salary

# e = Employee()
# print(e.totalSalary)
# e.totalSalary = 158000
# print(e.salary)
# print(e.salarybonus)

# ................................................................................

# @name.setter
# def name(self, value):
# 	self.ename = value

# ...............................................

# Operator overloading in Python

# Operators in python can be overloaded using dunder methods.

# These methods are called when a given operator is used on the objects.

# Operators in python can be overloaded using the following methods:
# *************************************************
# p1 + p2 -> p1.__add__(p2)

# p1 – p2 -> p1.__sub__(p2)

# p1 * p2 -> p1.__mul__(p2)

# p1 / p2 -> p1.__truediv__(p2)

# p1 // p2 -> p1.__floordiv__(p2)


# class Number:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, num2):
#         print("Let's add")
#         return self.num + num2.num

#     def __mul__(self, num2):
#         print("Let's Multiply")
#         return self.num * num2.num

# n1 = Number(4)
# n2 = Number(6)
# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul)

# Other dunder/magic methods in Python

# __str__() -> used  to set what gets displayed upon calling str(obj)

# __len__() -> used to set what gets displayed upon calling .__len__() or len(obj)

# class Number:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, num2):
#         print("Let's add")
#         return self.num + num2.num

#     def __mul__(self, num2):
#         print("Let's Multiply")
#         return self.num * num2.num

#     def __str__(self):
#         return f"Decimal Number: {self.num}"

#     def __len__(self):
#         return 1

# n = Number(9)
# print(n)
# print(len(n))

############################################### Practice Time #################################################

# 01 Q> Create a class C-2d vector and use it to create another class representing a 3-d vector.
# Let's practice.......

# class c2dVec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"


# class c3dVec(c2dVec):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


# v2d = c2dVec(1, 3)
# v3d = c3dVec(1, 9, 7)

# print(v2d)
# print(v3d)

###############################################################################################################

# 02 Q> Create a class pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.
# Let's practice.......

# class Animals:
#     animalType = "kkkkk"

# class Pets:
#     color = "White"

# class Dog():
#     @staticmethod
#     def bark():
#         print("Bow Bow!")

# d = Dog()
# d.bark()

###############################################################################################################

# 03 Q> Create a class Employee and add salary and increment properties to it.
# Write a method SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.
# Let's practice.......

# class Employee:
#     salary = 100000
#     increment = 1.5
#     @property
#     def salaryAftarincrement(self):
#         return self.salary*self.increment

#     @salaryAftarincrement.setter
#     def salaryAftarincrement(self, sai):
#         self.increment = sai/self.salary

# e = Employee()
# print(e.salaryAftarincrement)

# print(e.increment)
# e.salaryAftarincrement = 200000
# print(e.increment)

###############################################################################################################

# 04 Q> Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them.
# Let's practice.......

# class Complex:
#     def __init__(self, i, r):
#         self.real = r
#         self.imaginary = i

#     def __add__(self, c):
#         return complex(self.real + c.real, self.imaginary + c.imaginary)

#     def __mul__(self, c):
#         mulreal = self.real*c.real - self.imaginary*c.imaginary
#         mulImg = self.real*c.imaginary + self.imaginary*c.real
#         return complex(mulreal, mulImg)

#     def __str__(self):
#         return f"{self.real}r + {self.imaginary}i"   

# c1 = Complex(1, 4)        
# c2 = Complex(8, 5)        
# print(c1 + c2)
# print(c1 * c2)

###############################################################################################################

# 05 Q> Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them.
# Let's practice.......

# class Vector:
#     def __init__(self, vec):
#        self.vec = vec
    
#     def __str__(self):
#         str1 = "" 
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index +=1
#         return str1[:-1]

#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)
    
#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum

# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# print(v1+v2)
# print(v1*v2)

###############################################################################################################

# 06 Q> Write __str__() method to print the vector as follows:
# 7i + 8j + 10k

# Assume vector of dimension 3 for this problem.
# Let's practice.......

# class Vector:
#     def __init__(self, vec):
#        self.vec = vec
    
#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
 

# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# print(v1)
# print(v2)


###############################################################################################################

# 07 Q> Override the __len__() method on vector of problem 5 to display the dimension of the vector.
# Let's practice.......

# class Vector:
#     def __init__(self, vec):
#        self.vec = vec
    
#     def __str__(self):
#         str1 = "" 
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index +=1
#         return str1[:-1]

#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)
    
#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum
    
#     def __len__(self):
#         return len(self.vec)

# v1 = Vector([1, 4, 6, 6])
# v2 = Vector([1, 6, 9])
# print(len(v1))
# print(len(v2))


################################################# Done ########################################################
