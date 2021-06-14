#TASK THREE
#No. 1: Create a list of 10 elements of four different data types like int, string, complex and float.

mylist = [1,2.5,3+2j,"Consultadd",5,3.5,9+3j,5,5,5]

#%%No.2 
#Create a list of size 5 and execute the slicing structure
mylist = [0,1,2,3,4]
print(mylist[:2])
print(mylist[2:])
print(mylist[2:4])
print(mylist[0:5:2])

#%%No.3
#Write a program to get the sum and product of all the items in a given list.
mylist = eval(input("Write your list:"))
#mylist = [1,2,3,4,5]

mysum = sum(mylist)
print("Sum:",mysum)
prod = 1
for i in mylist:
    prod = prod * i
print("Product", prod)
#%% No.4
#Find the largest and smallest number from a given list.

#mylist = [5,2,8,123,4,-2,56,21,-104]
mylist = eval(input("Write your list:"))

mymin = min(mylist)
mymax = max(mylist)
print("Min:",mymin,"\n","Max:",mymax)

#%% No.5
# Create a new list which contains the specified numbers after removing the even numbers from a
#predefined list.

mylist = eval(input("Write your list:"))
#mylist = [1,2,3,4,5,6,7,8,22,33,44,55,66]

for i in mylist:
    if i % 2 == 0:
        mylist.remove(i)
        
#%% No.6
#Create a list of elements such that it contains the squares of the first and last 5 elements between
#1 and30 (both included).
mylist = list(range(1,6))+list(range(25,31))
mylist = list(map(lambda x:x**2, mylist))
print(mylist)

#%% No.7
#Write a program to replace the last element in a list with another list.
mylist = eval(input("Write your first list:"))
listtoadd = eval(input("Write your second list:"))

mylist.pop(-1)
mylist += listtoadd
print(mylist)
#%%  No.8
#Create a new dictionary by concatenating the following two dictionaries:
a = eval(input("Write your first dictionary:"))
b = eval(input("Write your second dictionary:"))
#a = {1:10,2:20}
#b = {3:30,4:40}
newdict = dict(a)
newdict.update(b)
#%%  No.9
#Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
#and n(both 1 and n included).
n = int(input("Enter the value of n: "))
mydict = {i:i*i for i in range(1,n+1)}

#%% No.10
#Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
numbers = input("Write down your numbers (comma sep): ")
mylist = numbers.split(",")
mytuple = tuple(mylist)