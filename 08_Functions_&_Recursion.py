########################################### Function & Recursion ########################################################

# marks1 = [65, 58, 85, 84, 56]
# parcentage1 = (sum(marks1)/500)*100

# marks2 = [58, 55, 75, 85, 56]
# parcentage2 = (sum(marks2)/500)*100

# print(parcentage1, parcentage2)

#...................................................................

# marks1 = [65, 58, 85, 84, 56]
# parcentage1 = ((marks1[0] + marks1[1] + marks1[2] + marks1[3] + marks1[4])/500)*100

# marks2 = [58, 55, 75, 85, 56]
# parcentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3] + marks2[4])/500)*100

# print(parcentage1, parcentage2)

#...............................................................

# def percent(marks):
#     return ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/500)*100

# marks1 = [65, 58, 85, 84, 56]
# parcentage1 = percent(marks1)

# marks2 = [58, 55, 75, 85, 56]
# parcentage2 = percent(marks2)

# print(parcentage1, parcentage2)

#................................................................

# def greet(name):
#     print("Good Day, "+ name)

# greet("Shubham")

#.................................................................

# def mySum(num1, num2):
#     return num1 + num2

# s = mySum(6, 52)
# print(s)

#................................................................

# def greet(name="Stranger"):             # Default paramiter value
#     print("Good Day, "+ name)

# greet("Shubham")
# greet()

############################################## Recursion ####################################################

# n! = 1*2*3*4*5......n  factoriyal value

# n = int(input("Enter the Number: "))
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

#..................................................

# n! = [1*2*3*4*5......n-1] *n


# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return(product)
# f = factorial_iter(5)
# print(f)

#..................................................

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return(product)

# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     return n* factorial_recursive(n-1)

# # f = factorial_iter(5)
# f = factorial_recursive(5)
# print(f)

############################################### Practice Time #################################################

# 01 Q> Write a program using function to find greatest of three numbers:
# Let's practice.......

# def maximum(num1, num2, num3):
#     if (num1>num2):
#         if (num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3

# m = maximum(45, 5, 55)
# print("The value of the maxmium is: "+ str(m))    

###############################################################################################################

# 02 Q> Write a python program using function to convert celsius to fahrenheit: 
# Let's practice.......

# def farh(cel):
#     return (cel * (9/5)) + 32
# c = 45
# f = farh(c)
# print("celsius to fahrenheit temprature is: " + str(f))

###############################################################################################################

# 03 Q> How do you prevent a python print() function to print a new line at the end:
# Let's practice.......

# print("Hello", end=" ")
# print("How", end=" ")
# print("are", end=" ")
# print("you", end=" ")

###############################################################################################################

# 04 Q> Write a recursive function to calculate the sum of first n natural number:
# Let's practice.......

# n! = (n-1)! * n
# sum(n) = sum(n-1) + n

# Python program to find the sum of natural using recursive function

# def recur_sum(n):
#    if n <= 1:
#        return n
#    else:
#        return n + recur_sum(n-1)

# # change this value for a different result
# num = 16

# if num < 0:
#    print("Enter a positive number")
# else:
#    print("The sum is",recur_sum(num))

###############################################################################################################

# 05 Q> Write a python function to printfirt n line of the following pattern for n=3
#   * * *
#   * * 
#   * 
 # Let's practice.......

# n = 3
# for i in range(n):
    # print("*" * (n-i))            # print * n-i times
    # print(i)

###############################################################################################################

# 06 Q> Write a python function which convert inch to cms:
# Let's practice.......

# inches = float(input('Enter the Height in inches to convert into centimeters:'))
# centi_meters = inches * 2.54
# centi_meters = round(centi_meters,2)
# print(inches,'Inches =', centi_meters,'Centimeters')

###############################################################################################################

# 07 Q> Write a python function to remove a given word form string and stap it at the some time:
# Let's practice.......

# this = "   I am the best   "
# print(this)
# print(this.strip())                     # this function use to remove the extra space: strip()

# def remove_and_strip(string, word):
#     newStr = string.replace(word, "")               # remove the particular word function
#     return newStr.strip()
# this = "   I am the best   "
# n = remove_and_strip(this, "best")
# print(n)

###############################################################################################################

# 08 Q> Write a python function to print multipfction table of a given number:
# Let's practice.......

# num = int(input("Enter the number: "))

# print("Multiplication Table of", num)
# for i in range(1, 11):
#    print(num,"X",i,"=",num * i)

################################################# Done ########################################################


