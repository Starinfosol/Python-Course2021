################################################# Files ########################################################

# Use open function to read the content of a file!
# f = open('sample.txt', 'r')
# f = open('sample.txt') # by default mode is r
# data = f.read() # read the conetnt of file
# data = f.read(5) # only selected content read the file(read first file chartacter)
# print(data)
# f.close()       # Close the file

############################################## Read line function ####################################################

# f = open('sample.txt', 'r')
# data = f.readline()
# print(data)
# f.close()      

#..................................................

#  r  = reading
#  w  = writing
#  a  = appending
#  +  = updateing

# f = open('sample.txt')
# # read first line
# data = f.readline()
# print(data)
# # read second line
# data = f.readline()
# print(data)
# # read third line
# data = f.readline()
# print(data)
# # read fourth line
# data = f.readline()
# print(data)
# f.close() 

#..................................................

#  r  = reading
#  w  = writing
#  a  = appending
#  +  = updateing
#  rb = will open for read for binary mode
#  rt = will open the read in text mode

########################################## Write  ################################################

# f = open('another.txt', 'w')
# f.write("Please write this to the file")
# f.close()

#..................................................

#  a  = appending
# create file and write the txt in file(format/create file after write) 

# f = open('another.txt', 'a')
# f.write("Please write this to the file")
# f.close()

############################################ with function ############################################

# open txt file function

# with open('another.txt', 'r') as f:
#     a = f.read()
# print(a)

# write the file

# with open('another.txt', 'w') as f:
#     a = f.write("me")

############################################### Practice Time #################################################

# 01 Q> Write a program to read the text form a given file 'poem.txt' and find out weather it continues the word twikle twikle:
# Let's practice.......

# f = open('poems.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("twinkle is prasent")
# else:
#     print("twinkle is not prasent")
# f.close()

###############################################################################################################

# 02 Q> The game() function in a program lets a user play a game and returns the score as intger . 
# you need to read a file 'th.txt' which is either blank or contains the previous hi score tou need to write a program
# to upadate the high score whenever game() break the high score:
# Let's practice.......

# def game():
#     return 6464

# score = game()
# with open("High_score.txt") as f:
#     High_scorestar = f.read()

# if High_scorestar == "":
#     with open("High_score.txt", 'w') as f:
#         f.write(str(score))

# elif int(High_scorestar)<score:
#     with open("High_score.txt", 'w') as f:
#         f.write(str(score))

###############################################################################################################

# 03 Q> Write a program to genrate multification table form 2 to 20 and write it to the diffent files. pleace this file in a folder for a 13 year old: 
# Let's practice.......

# print single table 
# for i in range(2, 21):
#     with open(f"tables/Multification table{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}")
#             if j!=10:
#                 f.write('\n')
#     break

#...................................................................

# # print Multiple table 
# for i in range(2, 21):
#     with open(f"tables/Multification table{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}")
#             if j!=10:
#                 f.write('\n')
    
###############################################################################################################

# 04 Q> A file contain a word "Donkey" miltiple times you need to write a program which replace this word with ###### by updateing the some file:
# Let's practice.......

# Change perticular word in txt file

# with open("sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey", "*&^%OI!@#$%")

# with open("sample.txt", 'w') as f:
#     f.write(content)

###############################################################################################################

# 05 Q> repeat program 4 for a list of such word to be centord:
# Let's practice.......

# words = ["abc", "def", "fgh", "ijk", "lmn"]

# with open("sample.txt") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "*&^%OI!@#$%")
    
#     with open("sample.txt", 'w') as f:
#         f.write(content)

###############################################################################################################

# 06 Q> Write a program to nine a log file and find out weather it contains "python".
# Let's practice.......

# with open("log.txt") as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("Yes python is prasent")
# else:
#     print("Python is not prasent")

###############################################################################################################

# 07 Q> Write a program to find out the line number where python is prasent form ques 6.
# Let's practice.......

# content = True
# i = 1
# with open("log.txt") as f:
#     while content:

#         content = f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"Yes python is prasent on line number {i}")
#         i+=1

###############################################################################################################

# 08 Q> Write a program to make a copy of a text file "this.txt".
# Let's practice.......

# with open("log.txt") as f:
#     content = f.read()

# with open("copylog.txt", 'w') as f:
#     f.write(content)

###############################################################################################################

# 09 Q> Write a program to find out whether a file is identical & matches the content of another file:
# Let's practice.......

# file1 = "sample.txt"
# file2 = "another.txt"

# with open(file1) as f:
#     f1 = f.read()

# with open(file2) as f:
#     f2 = f.read()

# if f1 == f2:
#     print("files are identical")
# else:
#     print("files is not identical")

###############################################################################################################

# 10 Q> Write a program to wipe out the content of a file using python:
# Let's practice.......

# filename = "sample.txt"
# with open(filename, "w") as f:                  # format file content
#     f.write("")

###############################################################################################################

# 11 Q> Write a python program to rename a file to "removed_by_python.txt": 
# Let's practice.......

# import os

# oldname = "sample2.txt"
# newname = "removed_by_python.txt"

# with open(oldname) as f:
#     content = f.read()

# with open(newname, 'w') as f:
#     f.write(content)

# os.remove(oldname)

################################################# Done ########################################################


