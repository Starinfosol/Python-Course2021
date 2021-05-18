############################################### Advanced Python 2 ########################################################
# Virtual Environment

# An environment that is same as the system interpreter but is isolated from the other python environments on the system.

# Installation

# To use virtual environments, we write

# pip install virtualenv          #Installs the package

# We create a new environment using:

# virtualenv myprojectenv             #Creates a new venv

# The next step after creating the virtual environment is to activate it.
# .............................................
# For MacOS/linux users: source myprojectenv/bin/activate
# For windows powershell users: .\myprojectenv\Scripts\activate.ps1
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

# import flask # flask - 0.5.2
# import pandas as pd
# import pygame
# ..................................................
# We can now use this virtual environment as a separate python installation.

# pip freeze command

# pip freeze returns all the packages installed in a given python environment along with the versions.

# “pip freeze > requirements.txt”

# The above command creates a file named requirements.txt in the same directory containing the output of pip freeze.

# We can distribute this file to other users and they can recreate the same environment using:

# pip install –r requirements.txt

# Lambda functions

# def func(a):
#     return a+5

# func = lambda a: a+5
# square = lambda x: x*x
# sum = lambda a, b, c: a+b+c

# x = 3
# print(func(x)) # Prints 8
# print(square(x)) # Prints 9
# print(sum(x, 1, 2)) # Prints 6

# ....................................................................
# Functions created using an expression using the lambda keyword

# Syntax:

# lambda arguments: expressions (can be used as a normal function)

# Example:

# Square = lambda x: x*x
# Square(6)	#returns 36
# Sum = lambda a,b,c: a+b+c
# Sum(1,2,3)	#returns 6
# bin method(Strings)

# Creates a string from iterable objects

# l = [“apple”, “mango”, “banana”]
# “,and,”.join(l)
# The above line will return “apple, and, mango, and, banana”
# .............................................................................

# l = ["Camera", "Laptop", "Phone", "ipad", "Hard Disk", "Nvidia Graphic 3080 card"]

# # sentence = "~~".join(l)
# # sentence = "==".join(l)
# sentence = "\n".join(l)
# print(sentence)
# print(type(sentence))

# ............................................................................
# Format method(Strings)
# .................................

# name = "Harry"
# channel = "CodeWithHarry"
# type = "Coding"
# # a = f"This is {name}"
# # a = "This is {}".format(name)
# # a = "This is {} and his channel is {}".format(name, channel)
# # a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
# a = "This is {} and his {} channel is {}".format(name, channel, type)

# print(a)

# .........................................
# Formats the values inside the string into the desired output

# template.format(p1, p2, …)        #p1, p2 … are the arguments

# The syntax for format looks like:

# “{} is a good {}”.format(“Harry”,”boy”) – 1
# “{1} is a good {0}”.format(“Harry”, “boy”) – 2
# Output for 1:

# Harry is a good boy

# Output for 2:

# boy is a good Harry

# Map, Filter & Reduce
# Map applies a function to all the items in an input_list.
############# Map ############

# def square(num):
#     return num*num

# l = [1, 2, 4]
# # Method 1
# l2 = []
# for item in l:
#     l2.append(square(item))
# print(l2)

# # Method 2

# print(list(map(square, l)))

#################### Filter ######################

# Filter Syntax: list(filter(function, list))
# def greater_than_5(num):
#     if num > 5:
#         return True
#     else:
#         return False

# g10 = lambda num: num>10

# l = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]
# print(list(filter(greater_than_5, l)))
# print(list(filter(g10, l)))

#################### Reduce ######################

# from functools import reduce

# sum = lambda a, b: a+b

# l = [1, 2, 3, 4]
# val = reduce(sum, l)
# print(val)

# Syntax:

# map(function, input_list)             #function can be lambda function

# Filter creates a list of items for which the function returns true.

# list(filter(function))            #function can be a lambda function


# Reduce applies a rolling computation to sequential pair of elements.

# from functools import reduce

# val = reduce(function, list1)        #function can be a lambda function

# If the function computes sum of two numbers and the list is [1, 2, 3, 4]

############################################### Practice Time #################################################

# 01 Q> Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
# Let's practice.......

# Done................

###############################################################################################################

# 02 Q> Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and the phone number is 99999888”
# Let's practice.......

# name = input("Enter your name: ")
# marks = input("Enter your marks: ")
# phone = input("Enter you phone Number: ")

# template = "The name of the student is {}, his marks are {} and phone number is {} "
# # template = f"The name of the student is {name}, his marks are {marks} and phone number is {phone} "
# output = template.format(name, marks, phone)
# print(output)

###############################################################################################################

# 03 Q> A list contains the multiplication table of 7. Write a program to convert it to a vertical string of the same numbers (7,14,….)
# Let's practice.......

# l = [str(i*7) for i in range(1, 11)]
# print(l)

# verticalTable = "\n".join(l)
# print(verticalTable)

#.....................................

# e = int(input("Enter the number: "))

# l = [str(i*e) for i in range(1, 11)]
# # print(l)

# verticalTable = "\n".join(l)
# print(verticalTable)

###############################################################################################################

# 04 Q> Write a program to filter a list of numbers that are divisible by 5.
# Let's practice.......

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 54, 23, 55, 90, 60]

# a = filter(lambda a: a%5==0, l)
# print(list(a))

###############################################################################################################

# 05 Q> Write a program to find the maximum of the numbers in a list using the reduce function.
# Let's practice.......

# from functools import reduce
# l = [3, 8, 455, 2, 5, 45]

# a = reduce(max, l)
# print(a)

###############################################################################################################

# 06 Q> Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.
# Let's practice.......

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '''<!doctype html>
#         <html lang="en">
#         <head>
#             <!-- Required meta tags -->
#             <meta charset="utf-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

#             <!-- Bootstrap CSS -->
#             <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

#             <title>Hello, world!</title>
#         </head>
#         <body>
#             <h1>Hello, world!</h1>
#             <div class="alert alert-primary" role="alert">
#         A simple primary alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-secondary" role="alert">
#         A simple secondary alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-success" role="alert">
#         A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-danger" role="alert">
#         A simple danger alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-warning" role="alert">
#         A simple warning alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-info" role="alert">
#         A simple info alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-light" role="alert">
#         A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-dark" role="alert">
#         A simple dark alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#             <!-- Optional JavaScript -->
#             <!-- jQuery first, then Popper.js, then Bootstrap JS -->
#             <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
#             <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
#             <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
#         </body>
#         </html>'''

# if __name__ == "__main__":
#     app.run(debug=True)

###############################################################################################################

# 07 Q> Explore the flask module and create a web server using flask and Python.
# Let's practice.......

# Done in 6 question

################################################# Done ########################################################
