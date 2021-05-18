###################### Welcome to String Function ###############################

# Hello Friends I am here.....

# Concatenating String [+]

# a = "Shubham "
# b = "verma"
# text = a + b
# print(text)

# x = "hey "
# y = "friends "
# taxt = x + y
# print(taxt)

# Accessing part of a String

# text = "I am best"

# print(len(text))

# '''0123456
# Shubham
# -7-6-5-4-3-2-1'''

# print(text[0])
# print(text[1])
# print(text[3])

# print(text[-1])
# print(text[-2])
# print(text[-3])

# Slicing

# text = "I Love You"

# print(text[0:5])
# print(text[2:5])
# print(text[2: ])
# print(text[2:1])
# print(text[ :2])
# print(text[ :10:2]) # Scip function


# Capitalize String Function Capitalize()

# text = "i love you"
# x = text.capitalize()
# print(x)

# Convert to Upper Case

# text = "i love you"
# x = text.upper()
# print(x)

# Convert to lower Case

# text = "I LOVE YOU"
# x = text.lower()
# print(x)

# Get the length of a String len()

# text = "I am the best"
# print(len(text))
# print(text.endswith("best"))      # Show True & False
# print(text.count("t"))              # Counting Woards
# print(text.count("the"))              # Counting Woards
# print(text.find("the"))              # Find Woards

# Replacing Part of String replace()

# string.replace(old, new)

# text = "Hello World"
# x = text.replace("World", "Everyone")
# print(x)

#Escape Sequence

# text = "I think \n he is good"    #new line :- \n
# print(text)

# text = "I think he \t is good"     # TAb :- \t
# print(text)

# text = "I think he \' is good"     # singlesquence:- \'
# print(text)

# text = "I think \\ is good"     # backslash \\
# print(text)


######################### Practice time ##################################

# 01 Q> Write a python program to dispaly a user enterd name followed by good morning using input() function:
# Let's practice.......

# name = input("Enter your name\n")
# print("Good Morning, " + name)

# 02 Q> Write a program to fill in a letter template given below with name and other(including Self):
# Let's practice.......

# letter = '''Dear Hiring Manager :


# Earlier this month, I made the decision to begin looking for a new career opportunity and I believe my experience is a strong match for the responsibilities pertaining to this role, and I’m pleased to submit my application for the position.
# I’m looking for a new company to challenge me and grow my skill set in <|Skill|>.

# Total Exp. : <|Total_Exp|>
# Relevant Exp. : <|Relevant_Exp|>
# Current company : <|Current_company|>
# Current location : <|Current_location|>
# Current Salary : <|Current_Salary|>
# Expected Salary : <|Expected_Salary|>
# Notice Period : <|Notice_Period|>
# Contact No : <|Contact_No|>
# Alternate Contact Number : <|Alternate_Contact_Number|>
# Skype ID : <|Skype_ID|>
# Email ID : <|Email_ID|>

# I am included my  LinkedIn Profile for further information.
# LinkedIn : <|LinkedIn_Profile|>

# My resume is attached. If I can provide you with any further information on my background and qualifications, please let me know.
# I look forward to hearing from you. Thank you for your consideration.

# Sincerely,
# <|NAME|>

# Date: <|DATE|>
# '''
# name = input("Enter your Name\n")
# Total_Exp = input("Enter your Total Exp.: ")
# Relevant_Exp = input("Enter your Relevant Exp.: ")
# Current_company = input("Enter your Current company: ")
# Current_location = input("Enter your Current location: ")
# Current_Salary = input("Enter your Current Salary: ")
# Expected_Salary = input("Enter your Expected Salary: ")
# Notice_Period = input("Enter your Notice Period: ")
# Contact_No = input("Enter your Contact No: ")
# Alternate_Contact_Number = input("Enter your Alternate Contact Number: ")
# Skype_ID = input("Enter your Skype ID: ")
# Email_ID = input("Enter your Email ID: ")
# Skill = input("Enter your Skill: ")
# LinkedIn_Profile = input("Enter your LinkedIn Profile: ")
# date = input("Enter Date: ")

# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|Total_Exp|>", Total_Exp)
# letter = letter.replace("<|Relevant_Exp|>", Relevant_Exp)
# letter = letter.replace("<|Current_company|>", Current_company)
# letter = letter.replace("<|Current_location|>", Current_location)
# letter = letter.replace("<|Current_Salary|>", Current_Salary)
# letter = letter.replace("<|Expected_Salary|>", Expected_Salary)
# letter = letter.replace("<|Notice_Period|>", Notice_Period)
# letter = letter.replace("<|Contact_No|>", Contact_No)
# letter = letter.replace("<|Alternate_Contact_Number|>", Alternate_Contact_Number)
# letter = letter.replace("<|Skype_ID|>", Skype_ID)
# letter = letter.replace("<|Email_ID|>", Email_ID)
# letter = letter.replace("<|Skill|>", Skill)
# letter = letter.replace("<|LinkedIn_Profile|>", LinkedIn_Profile)
# letter = letter.replace("<|DATE|>", date)

# print(letter)


# 03 Q> Write a program to detect double space in a string:
# Let's practice.......

# text = '''The Maharashtra government on Tuesday moved the Supreme Court challenging the Bombay high court order
#  directing CBI probe against former home minister Anil Deshmukh.
#  “We have filed an  appeal on behalf of state government against the Bombay high court of yesterday,” 
#  said Maharashtra standing counsel Sachin Patil.'''

# print(text.find("  "))   # Detect Dual Space

# 04 Q> Replace the double space form problem 3 with single spaces:
# Let's practice.......

# text = text.replace("  ", " ")      # replace dual space to singal space
# print(text)


# 05 Q> Write a program to formet the following letter using escape sequence characters: letter = "Dear Shubham,This is my program!Thanks" :
# Let's practice.......

# letter = "Dear Shubham,\n\tThis is my program! \nThanks"        # Formating letter using \n & \t
# print(letter)

################################## Done ##########################################