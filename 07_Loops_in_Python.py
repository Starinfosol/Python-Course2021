################################################# Loops ########################################################

# two type of loop:

# 01--> while loop
# 02--> for loop


################# while loop ###################


# i = 0

# while i < 10:
#     print("Yes " + str(i))
#     i = i + 1
# print("Done")



#..................................................

# i = 1

# while i<=50:
#     print(i)
#     i = i + 1
# print("Done")

#..................................................

# fruites = ["banana", "greapes", "Mango", "annanas"]
# i = 0
# while i<len(fruites):
#     print(fruites[i])
#     i = i + 1


################# for loop ###################


# fruites = ["banana", "greapes", "Mango", "annanas"]

# for items in fruites:           # print the multiple items in list form 
#     print(items)

################# Range function ###################

# for i in range(8):
#     print(i)

#........................

# for i in range(1, 8):
#     print(i)

#...........................

# for i in range(5, 8):
#     print(i)

#..........................

# for i in range(1, 8, 2):
#     print(i)

################# for loop with else ###################

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# for item in l:
#     print(item)
# else:
#     print("Done")

#....................................

# for item in range(10):
#     print(item)
# else:
#     print("Done")

################# Break statment ###################

# for item in range(10):
#     print(item)
#     if item == 5:
#         break

#...................................

# for item in range(10):
#     print(item)
#     if item == 5:
#         break
# else:
#     print("Done")

################# continues statment ###################

# for item in range(10):
    
#     if item == 5:
#         continue
#     print(item)

################# pass statment ###################

# i = 4
# if i>5:
#     pass                              # none(function pause) 
# print("I am the best")

# #......................................

# i = 4
# while i>5:
#     pass                          ## none(function pause) 
# print("I am the best")

#..............................................

# def sum(a, b):
#     pass                                # pass cmd is using for pause the function(function pause) 

############################################### Practice Time #################################################

# 01 Q> Write a program to print multiplcation table of given number using for loop:
# Let's practice.......

# num = int(input("Enter the number: "))
# for i in range(1, 11):
    # print(str(num) + " X " + str(i) + " = " + str(i*num))
    # print(f"{num} X {i} = {i*num}")                           # using f string function

###############################################################################################################

# 02 Q> Write a program to great all the person name stored in a list l1 and which start with 5: l1 = ["Nily", "prank", "prince", "harsh"] 
# Let's practice.......

# l1 = ["Nily", "prank", "prince", "harsh"]
# for name in l1:
#     if name.startswith("p"):
#         print("Hello " + name)

###############################################################################################################

# 03 Q> Write a program to print multiplcation table of given number using while loop:
# Let's practice.......

# num = int(input("Enter the number: "))
# i = 0
# while i <= 10:
    # print(str(num) + " X " + str(i) + " = " + str(i*num))
    # print(f"{num} X {i} = {i*num}")                           # using f string function
    # i = i + 1
###############################################################################################################

# 04 Q> Write a program to find whether a given number is prime or not:
# Let's practice.......

# num = int(input("Enter the number: "))
# prime = True
# for i in range(2, num):
#     if (num%i == 0):
#         prime = False
#         break
# if prime:    
#     print("This no is prime")
# else:
#     print("This no is not prime")

###############################################################################################################

# 05 Q> Write a program to find the sum of first n natural number using while loop:
# Let's practice.......

# num = int(input("Enter a number: "))  
  
# if num < 0:  
#    print("Enter a positive number")  
# else:  
#    sum = 0  
#    # use while loop to iterate un till zero  
#    while(num > 0):  
#        sum += num  
#        num -= 1  
#    print("The sum is",sum) 

#....................................................................

# num = int(input("Enter the number: "))
# natural = 0
# for i in range(1, num + 1):
#     natural = natural + i
# print(f"The Natural of this number is: {natural}")

###############################################################################################################

# 06 Q> Write a program to calculate the factorial of a given number using for loop:
# Let's practice.......

# n! =  1 X 2 X 3 X 4 X 5 X 6 X 7 X 8 X 9........n              # fectorial Desribe
# 5! =  1 X 2 X 3 X 4 X 5                                       # fectorial Desribe

# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print(f"The factorial of this number is: {factorial}")

###############################################################################################################

# 07 Q> Write a program to print the following star pattern: for n = 
#         *
#       * * *
#     * * * * *
# Let's practice.......

# n = 3

# for i in range(3):
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1))

###############################################################################################################

# 08 Q> Write a program to print the following star pattern: for n = 3
#  *
#  **
#  ***
# Let's practice.......

# n = 4

# for i in range(4):
    # print("*" * i)
    # print("*" * (i+1))

###############################################################################################################

# 09 Q> Write a program to print the following star pattern: for n = 3: 
#  * * *
#  *   *
#  * * *
# Let's practice.......
 


###############################################################################################################

# 10 Q> Write a program to print multification table of n using for loop in reversed order:
# Let's practice.......





################################################# Done ########################################################


