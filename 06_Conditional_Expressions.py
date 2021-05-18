####################################### Conditional Expressions #############################################

# if-alif-else ladder in Python

# a = 45
# a = 15
# a = 25
# a = 18

# if(a>5):
#     print("The value of is grater than: 5")
# elif(a>10):
#     print("The value of is grater than: 10")
# elif(a>15):
#     print("The value of is grater than: 15")
# elif(a>17):
#     print("The value of is grater than: 17")
# elif(a>20):
#     print("The value of is grater than: 20")
# else:
#     print("The value is not greater than 5, 10, 15, 17, 20")

# print("Done")

# Multipale if Statements

# a = 25

# if(a>5):
#     print("The value of is grater than: 5")
# if(a>10):
#     print("The value of is grater than: 10")
# if(a>50):
#     print("The value of is grater than: 50")
# if(a>17):
#     print("The value of is grater than: 17")
# if(a>200):
#     print("The value of is grater than: 200")
# if(a>20):
#     print("The value of is grater than: 20")
# else:
#     print("The value is not greater than 5, 10, 50, 17, 200, 20")

# print("Done")

# Age greater than 18+

# age = int(input("Enter your age: "))

# if age>=18:
# if age>18:
#     print("Yes")
# else:
#     print("No")

#..........................................

# age = int(input("Enter your age: "))

# if age==18:
#     print("Equal to 18")
# if age<=18:
#     print("less than 18")
# if age>=18:
#     print("greater than 18")
# else:
#     print("you are not allowed")

# ................................. logical & relational condition .................

# age = int(input("Enter your age: "))

# if (age>35 and age<56):
#     print("You can work with us")
# else:
#     print("You can't work with us")

#..........................................

# age = int(input("Enter your age: "))

# if (age>35 or age<56):
#     print("You can work with us")
# else:
#     print("You can't work with us")

#............... In & IS function ...........................

# a = None

# if (a is None):
#     print("Yes")
# else:
#     print("No")



# a = [15, 151, 15, 5]

# if (15 in a):
#     print("Yes")
# else:
#     print("No")

############################################### Practice Time #################################################

# 01 Q> Write a program to find greatest of four numbers enterd by the user:
# Let's practice.......

# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# num3 = int(input("Enter Number 3: "))
# num4 = int(input("Enter Number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4 

# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) + " is greatest") 
# else:
#     print(str(f2) + " is greatest")    


###############################################################################################################

# 02 Q> Write a program of find out whether a student is pass or fail ,if it requirs total 40% and
#at least 33% in each subject to pass assume 4 subject and take marks as an input form the user:
# Let's practice.......

# sub1 = int(input("Enter first subject marks\n"))
# sub2 = int(input("Enter second subject marks\n"))
# sub3 = int(input("Enter third subject marks\n"))
# sub4 = int(input("Enter fourth subject marks\n"))

# if(sub1<33 or sub2<33 or sub3<33 or sub4<33):
#     print("you are fail because you have less than 33 % in one of the subjects")

# elif(sub1+sub2+sub3+sub4)/4 < 40:
#     print("you are fail due to total percentage less than 40")

# else:
#     print("Congatulations! You are passed the Exam")


###############################################################################################################

# 03 Q> A spam comment is definded as a text contaning following keywords:
#"make a lot of money", "buy now", "Subscribe this", "Click this", Write  a program to detect these spams:
# Let's practice.......

# text = input("Enter the text:\n")
# spam = False

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("Subscribe this" in text):
#     spam = True
# elif("Click this" in text):
#     spam = True
# else:
#     spam = False

# if (spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")

###############################################################################################################

# 04 Q> Write a program to find whether a givin username contain less than 10 characters or not:
# Let's practice.......

# x = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

# if(len(x) == 10):
#     print("Yes is equl to 10")
# else:
#     print("less than 10")


###############################################################################################################

# 05 Q> Write a program which finds out whether a given name is present in a list or not:
# Let's practice.......

# names = ["rohit", "jaan", "saneem", "jj", "rohan", "malik", "pandey", "ansul"]
# name = input("Enter the name to Check\n")

# if name in names:
#     print("Your name is present in the list")
# else:
#     print("Your name is not present in the list")


###############################################################################################################

# 06 Q> Write a program to calculate the grate of a student form his marks form the following scheme:
# 90-100 = Ex
# 80-90 = A
# 70-80 = B
# 60-70 = C
# 50-60 = D
# 40-50 = E
# 00<40 = F
# Let's practice.......

# marks = int(input("Enter your marks\n"))

# if marks>=90:
#     grade = "Ex"
# elif marks>=80:
#     grade = "A"
# elif marks>=70:
#     grade = "B"
# elif marks>=60:
#     grade = "C"
# elif marks>=50:
#     grade = "D"
# elif marks>=40:
#     grade = "E"
# else:
#     grade = "F"

# print("Your grade is " + grade)


###############################################################################################################

# 07 Q> Write a program to find out whether a given post is talking about "Shubham" or not:
# Let's practice.......

# post = input("Enter your post\n")

# if(post in "Shubham"):
#     print("Yes Shubham is abilable in this post")
# elif(post in "shubham"):
#     print("Yes Shubham is abilable in this post")
# elif(post in "SHUBHAM"):
#     print("Yes Shubham is abilable in this post")
# else:
#     print("Shubham is not prasent")


################################################# Done ########################################################
