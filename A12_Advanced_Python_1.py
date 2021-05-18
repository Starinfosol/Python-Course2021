########################################## Advanced Python 1 ######################################################

# Exception Handling in Python
# There are many built-in exceptions that are raised in Python when something goes wrong.

# Exceptions in Python can be handled using a try statement. The code that handles the exception is written in except clause.

# '''
# try:
# 	#code		#Code that might throw an exception
# except Exception as e:
# 	print(e)
# .......................................................................

# while(True):
#     print("Press q to quit")
#     a = input("Enter a number: ")
#     if a == 'q':
#         break
#     try:
#         print("Trying...")
#         a = int(a)
#         if a>6:
#             print("You entered a number greater than 6")
#     except Exception as e:
#         print(f"Your input resulted in an error: {e}")

# print("Thanks for playing this game")

# .........................................................................
# When the exception is handled, the code flow continues without program interruption.

# We can also specify the exceptions to catch like below:

# '''
# try:
# 	#code
# except ZeroDivisionError:
# 	#code
# except TypeError:
# 	#code
# except:
# 	#code 	(All other exceptions are handled here)
# '''
# Handling diffent exception :-

# try:
#     a = int(input("Enter the Number: "))
#     c = 1/a
#     print(c)
# except Exception as e:
#     print("Exception Accoured")
#     print(e)

# print("Thanks for using this code!")

# ......................................................................

# try:
#     a = int(input("Enter the Number: "))
#     c = 1/a
#     print(c)
# except ValueError as e:
#     print("Please inter a valid value")


# except ZeroDivisionError as e:
#     print("Make sure you are not dividing by 0")


# print("Thanks for using this code!")

# ...........................................................................
# Raising Exceptions

# def incriment(num):
#     try:
#         return int(num) + 1
#     except:
#         raise ValueError("This is not good")

# a = incriment(42)
# print(a)

# ....................................................................
# We can raise custom exceptions using the raise keyword in python.

# try with else clause

# Sometimes we want to run a piece of code when try was successful.

# '''
# try:
# 	#some code
# except:
# #some code
# else:
# 	#Code	(This is executed only if the try was successful)
# '''
# try with finally

# try:
#     i = int(input("Enter the number: "))
#     c = 1/i
#     print(c)
# except Exception as e:
#     print(e)
# else:
#     print("We where Successful")


# .....................................................................................

# Python offers a finally clause which ensures execution of a piece of code irrespective of the exception.

# '''
# try:
# 	#some code
# except:
# 	#some code
# finally:
# 	#some code		(executed regardless of error!)
# '''


# try:
#     i = int(input("Enter the number: "))
#     c = 1/i
#     print(c)
# except Exception as e:
#     print(e)
#     exit()
# finally:
#     print("We are Done!")

# print("Thanks for using the program")

#.....................................................................................
# if __name__==’__main__’ in Python
# __name__ evaluates to the name of the module in Python from where the program is ran.

# If the module is being run directly from the command line, the __name__ is set to string “__main__”.

# def greet(name):
#     print(f"Good Morining, {name}")

# if __name__ == "__main__":

#     n = input("Enter your Name: ")
#     greet(n)

#...................................................................................
# Thus this behavior is used to check whether the module is run directly or imported to another file.

# The global keyword

# a = 54                  # Global variable

# def fun1():
#     a = 8               # Local variable
#     print(a)

# fun1()
# print(a)    
#....................................................................................

# a = 54                  # Global variable

# def fun1():
#     global a
#     print(f"print statment 1 : {a}")
#     a = 8               # Local variable if global keyword is not used
#     print(f"print statment 2 : {a}")

# fun1()
# print(f"print statment 3 : {a}") 

# global keyword is used to modify the variable outside of the current scope.
#.......................................................................................
# enumerate function in Python

# list1 = [5, 56, 385, False, True, 3.450, "Shubham"]
# index = 0

# for item in list1:
#     print(index, item)
#     index += 1


################ enumerate function in Python ###############


# list1 = [5, 56, 385, False, True, 3.450, "Shubham"]
# index = 0

# for index, item in enumerate(list1):
#     print(index, item)

#.........................................................................................
# The enumerate function adds counter to an iterable and returns it.

# for i, item in list1:
#     print(i, item)            #Prints the items of list1 with index!
# List comprehensions

# List comprehensions is an elegant way to create lists based on existing lists.

# list1 = [1, 7, 12, 11, 22]

# list2 = [i for item in list1 if item>8]
#............................................................................................

# a = [1, 7, 12, 11, 22, 685, 653, 835]
# b =[]

# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

# Shortcut to write the same .........................................................

# a = [1, 7, 12, 11, 22, 685, 653, 835]
# b =[i for i in a if i%2==0]
# print(b)

############################################### Practice Time #################################################

# 01 Q> Write a program to open three files 1.txt, 2.txt, and 3.txt. if any of these files are not present, a message without exiting the program must be printed prompting the same.
# Let's practice.......

# def readFile(filename):
#     try:
#         with open(filename, "r") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"File {filename} is not found")
        
# readFile("1.txt")
# readFile("2.txt")
# readFile("poems.txt")

###############################################################################################################

# 02 Q> Write a program to print the third, fifth, and seventh elements from a list using the enumerate function.
# Let's practice.......

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index, item in enumerate(l):
#     if index==2 or index== 4 or index==6:
#         # print(index, item)
#         print(f"The {index + 1}th element is {item}")

###############################################################################################################

# 03 Q> Write a list comprehension to print a list that contains the multiplication table of a user-entered number.
# Let's practice.......

# num = int(input("Enter your number: "))

# table = [num*i for i in range(1, 11)]
# print(table)

###############################################################################################################

# 04 Q> Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ZeroDivisionError.
# Let's practice.......

# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))

# try:
#     print(a/b)
# except:
#     print("Infinite")

###############################################################################################################

# 05 Q> Store the multiplication tables generated in problem 3 in a file named Tables.txt.
# Let's practice.......

# num = int(input("Enter your number: "))

# table = [num*i for i in range(1, 11)]
# print(table)
# with open("tables.txt", "a") as f:
#     f.write(str(table))
#     f.write('\n')

################################################# Done ########################################################
