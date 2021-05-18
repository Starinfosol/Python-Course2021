################################### Lists & tuples #########################################

# Create List using []

# x = [1, 2, 3, 4, 5]
# print(x)        # print list

# x[0] = 52       # change the value of list caractor

# print(x)        # print list
# print(x[0])     # single value print
# print(x[1])     # Accroding to print by order 
# print(x[2])     # Accroding to print by order


# we can create a listwith items of Differents types

# c = [44, "Shubham", True, 6.9]
# print(c)

# List Slicing

# Friends = ["Shubham", "Jaan", "Saneem", "jj", "Ansul"]

# print(Friends[0:4])
# print(Friends[-4:])

# List Methods(importent function)

l1 = [1, 8, 7, 2, 21, 15]
print(l1)

# l1.sort()                     # badhte kram m arrenge karna(short the list)
# l1.reverse()                  # reverses the list
# l1.append(45)                 # add at the end of the list
# l1.append(52)                 # add at the end of the list
# l1.append(43)                 # add at the end of the list (most importtent function)
l1.insert(2, 544)             # inserts 544 at index 2
# l1.pop(2)                     # will delete elements at index 2 and return its value
# l1.remove(21)                 # Remove 21 form the list(delete)
print(l1)

# ....................................................

# tuples
# creating a tuples using()
# t = (1, 2, 3, 4, 5)

# t1 = ()     # Empty tuple
# t1 = (1)           # Wrong way to declarea tuple with single element
# t1 = (1,)       # Tuple with single element 

# printing the elements of a tuple

# print(t[0])

# Cannot update the value of a tuple

#.....................

# Tuples method

# creating a tuples using()
# t = (1, 2, 3, 4, 4, 4, 5)


# print(t.count(4))  # count the variables
# print(t.index(1))  # search the variables


# Checking if an item exists

# x = [122, 255, 655, 355, 355, 855, 457]

# print(122 in x)         # True
# print(35 in x)          # false

# Extending a list 

# x = [122, 255, 655, 355, 355, 855, 457]
# y = [556, 52, 25, 23658, 2558, 25]

# x.extend(y)
# print(x)

#.......................................
# x = [122, 255, 655, 355, 355, 855, 457]
# y = [556, 52, 25, 23658, 2558, 25]

# x.update(y)   not working this function
# print(x)
#........................................

###################################  Practice time  #############################################

# 01 Q> Write a program to store seven fruits in a list entered by the user:
# Let's practice.......

# f1 = input("Enter Fruit Number 1: ")
# f2 = input("Enter Fruit Number 2: ")
# f3 = input("Enter Fruit Number 3: ")
# f4 = input("Enter Fruit Number 4: ")
# f5 = input("Enter Fruit Number 5: ")
# f6 = input("Enter Fruit Number 6: ")
# f7 = input("Enter Fruit Number 7: ")

# myfruitslist = [f1, f2, f3, f4, f5, f6, f7]
# print(myfruitslist)


# 02 Q> Write a program to accept marks of 6 students and display them in a sorted manner:
# Let's practice.......


# m1 = int(input("Enter marks for student Number 1: "))  # convrt string to int 
# m2 = int(input("Enter marks for student Number 2: "))
# m3 = int(input("Enter marks for student Number 3: "))
# m4 = int(input("Enter marks for student Number 4: "))
# m5 = int(input("Enter marks for student Number 5: "))
# m6 = int(input("Enter marks for student Number 6: "))

# mylist = [m1, m2, m3, m4, m5, m6]
# mylist.sort()                       # Arrenge the list
# print(mylist)


# 03 Q> Check that a tuple connot be changed in pyhton:
# Let's practice.......

# x = [5, 2, 6, 4, 8]
# x[0] = 52


# 04 Q> Write a program to sun a list with 4 numbers:
# Let's practice.......

# a = [5, 2, 6, 4]
# print(a[0] + a[1] + a[2] + a[3])
# print(sum(a))

# 05 Q> Write a program to count the number of was in the following tuple: a = (7, 0, 8, 0, 0, 2, 5, 8, 6)
# Let's practice.......

# a = [7, 0, 8, 0, 0, 2, 5, 8, 6]
# print(a.count(0))                 # particular kisi no ko trace karna
# print(len(a))                     # total list count karna

############################ Done ############################################


