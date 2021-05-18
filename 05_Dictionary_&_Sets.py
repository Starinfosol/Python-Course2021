######################## Start Dictionary & Sets functions #################################

# mydata = {
#     "first_name": "Shubham",
# "last_name": "verma",
# "DOB": "22/07/1994",
# "Designation": "Devloper",
# "Skills": "Electronic Engineer, (MBA) HR & Finance, Python Devloper, Javascript, C and working with : Django, Flask, Angular.",
# "Numbers": "2135433545"
# } 

# x = mydata["first_name"]
# y = mydata["last_name"]
# z = mydata["DOB"]
# a = mydata["Designation"]
# b = mydata["Skills"]

# print(mydata)
# print("First Name: ", x)
# print("Last Name: ", y)
# print("DOB: ", z)
# print("Designation: ", a)
# print("Skills: ", b)

# mydata['Numbers'] = [1354513554534513]              # change the dictionary no. (replace) it's working

# print(mydata.get("Numbers"))         #get is a specific search in the word in dictionary

#  Mathods

# mydic = {
#     "first_name": "Shubham",
# "last_name": "verma",
# "DOB": "22/07/1994",
# "friends list": {'aa':'as'},
# 1: 2
# }

# # print(mydic.keys())             # show all keys in Dictionary 
# print(list(mydic.keys()))          # by list
# print(list(mydic.values()))         # print the values of list 
# print(list(mydic.items()))          # print the (key, value) for all contents of the Dictionary


# print(mydic)
# updatedic = {
#     "first_name": "jaan",               # update name by dictionary
#     "OS": "Jarvis",
#     "oprationg": "jarvis",
#     "functions": "Jarvis"
# }
# mydic.update(updatedic)                 # update the Dictionary by adding key-value pairs from updatedic
# print(mydic)

# print(mydic.get("OS"))                  # print value associated with key "OS"
# print(mydic["OS2"])                     # print value associated with key "OS"

# # The difference between .get and [] sytax in Dictionary ? 

# print(mydic.get("OS2"))                  # Return None as OS2 is not present in the dictionary
# print(mydic["OS2"])                    # throws an error as OS2 is not present in the dictionary

####################### Sets in Python ########################


# a = {1, 2, 5, 5, 5}

# print(type(a))              # set not repeat items
# print(a)

#Importent  :this syntax will create an empty dictionary and not an empty

# a = {}
# print(type(a))              # set not repeat items

# An empty set can be created using the below syntax:

# b = set()
# print(type(b))

# Set Methods############

# b = set()
# print(type(b))

# Adding value

# b.add(4)
# b.add(5)
# b.add(5)                # Adding a value repeatedly does not change a set
# b.add((4, 6, 8))

# Accessing Elements
# b.add({4:5})                # cannot add list or dictionary to sets

# print(b)

# Length of the set
# print(len(b))           # print the length of set

# removel of an Item
# b.remove(5)             # removes 5 formt set b
# b.remove(15)                # throws an error while trying to remove 15(which is not prasent in the set)
# print(b)


# print(b.pop())          # remove the value by sets(delete)
# print(b.clear())          # delete all data bt set

######### union & intersection #################

# BY USING INTERNET

####################### Practice time #############################

# 01 Q> Write a progrem to create a dictionary of hindi woards with values as thier english translation provide user with an option to look it up! :
# Let's practice.......

# mydict = {
#     "pankha": "fan",
#     "Dabba": "box",
#     "Vastu": "Item"
# }

# print("Options are ", mydict.keys())
# a = input("Enter the Hindi Word\n")

# print("The meaning of your word is: ", mydict[a])

# Below line will not throw an error if the key is not present in the dictionary 

# print("The meaning of your word is: ", mydict.get(a)) 

###############################################################################################################

# 02 Q> Write a program to input eight numbers form the user and  display all the unique numbers(o)
# Let's practice.......

# num1 = int(input("Enter Number 1:\n"))
# num2 = int(input("Enter Number 2:\n"))
# num3 = int(input("Enter Number 3:\n"))
# num4 = int(input("Enter Number 4:\n"))
# num5 = int(input("Enter Number 5:\n"))
# num6 = int(input("Enter Number 6:\n"))
# num7 = int(input("Enter Number 7:\n"))
# num8 = int(input("Enter Number 8:\n"))

# s = {num1, num2, num3, num4, num5, num6, num7, num8}
# print(s)

###############################################################################################################

# 03 Q> Can we have a set with 18(int) and "18"(str) as a value in it?
# Let's practice.......

# s = {18, "18", 18.1}
# print(s)


###############################################################################################################

# 04 Q> What will be the length of following set s: s = set() \ s.add(20) \ s.add(20.0) \ s.add("20") => length of 5 after these opraters? 
# Let's practice.......

# s = set(20, 20.0, "20")
# print(len(s))

###############################################################################################################

# 05 Q> s ={} \ whats is the type of s?
# Let's practice.......

# s = {}
# print(type(s))

###############################################################################################################

# 06 Q> Create can empty dictionary Allow 4 friends to enter their favourite language as value and use keys as their names. assume that the name are unique.
# Let's practice.......

# favLang = {}

# a = input("Enter your favorite language Ansul\n")
# b = input("Enter your favorite language Ankit\n")
# c = input("Enter your favorite language Sonali\n")
# d = input("Enter your favorite language Harshita\n")

# favLang['ansul'] = a                        # Adding dic word
# favLang['ankit'] = b
# favLang['sonali'] = c
# favLang['harshita'] = d

# print(favLang)

###############################################################################################################

# 07 Q> If name of 2 friends are same what will happaned to the program in Problem 6:
# Let's practice.......

# favLang = {}

# a = input("Enter your favorite language Ansul\n")
# b = input("Enter your favorite language Ansul\n")

# favLang['ansul'] = a                        # Adding dic word
# favLang['ansul'] = b

# print(favLang)

###############################################################################################################

# 08 Q> If languages of two friends are same; what will happan to the program in python:
# Let's practice.......

# favLang = {}

# a = input("Enter your favorite language Ansul\n")
# b = input("Enter your favorite language Ankit\n")
# c = input("Enter your favorite language Sonali\n")
# d = input("Enter your favorite language Harshita\n")

# favLang['ansul'] = a                        # Adding dic word
# favLang['ankit'] = b
# favLang['sonali'] = c
# favLang['harshita'] = d

# print(favLang)

# So values same ho sakti h dictionary m

###############################################################################################################

# 09 Q> Can you change the values inside a list which is contained in set s = {8, 7, 12, "Shubham", [1, 2]}
# Let's practice.......

# Rong Queation  
# it is not a set
# and dont change value

########################## Done ####################################
