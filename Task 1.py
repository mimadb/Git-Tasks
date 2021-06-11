#############################
#          TASK ONE         #
#############################
#%% No.1:
#Create three variables in a single line and assign values to them in 
#such a manner that each one of them belongs to a different data type.
a, b, c = 1, 2.01, "Consultadd"
#%% No.2:
# Create a variable of type complex and swap it with another variable of 
#type integer.
a = 1 + 2j
a = 8
#Not sure if this is what this problem is looking for, it is worded a bit
#ambiguously, if the integer was supposed to be stored in another variable,
# the solution in problem 3 works for this.
#%% No.3:
# 3. Swap two numbers using a third variable and do the same task without 
#using any third variable.
a = 2
b = 3
tempvar = a
a = b
b = tempvar

#%% No.3b:

a = 2
b = 3
a, b = b, a

#%% No.4:
#Write a program that takes input from the user and prints it using 
#both Python 2.x and Python 3.x Version.

#%%Python 3.x version
x = input()
print(x)

#%% Python 2.x version
x = raw_input()
print x

#%% No. 5:
#Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.
x = int(input("Enter the first number: "))
y = int(input("Enter the second number number: "))
z = x + y
result = z + 30
print(result)
#%% No. 6:
#Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc
x = eval(input("Enter value to have its data type checked:"))
print("The data type of the input value is :", type(x).__name__)

#%% No. 7:
#Create Variables using formats such as Upper CamelCase, Lower CamelCase,
# SnakeCase and UPPERCASE.
MyVariableName = "Upper Camel Case"
myVariableName = "Lower Camel Case"
my_variable_name = "Snake Case"
MYVARIABLENAME = "Why are you screaming?"
# Funny thing: Uppercase-named variables do not show up on Spyder's variable explorer
# I found this explanation why:
#https://stackoverflow.com/questions/36486853/variable-not-available-at-spyders-variable-explorer-when-naming-it-with-upper-c
#%% No. 8:
#If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?

#Yes. A variable can be reassigned to refer to another data type.
# Why?
# Unlike in for example C++ (int, double, char etc...), python does not require declaring variable types 
# In Python, variables are "dynamically typed"
#
#   Example:
#
#In [38]: a = 2
#
#In [39]: a = [5 , 4]
#
#In [40]: print(a)
#[5, 4]


