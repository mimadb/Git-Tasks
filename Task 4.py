#TASK FOUR
#No. 1: Write a program to reverse a string.
voutput = ""
for i in range(len(myStr)-1,-1,-1):
    output += myStr[i]
print(output)
#%%No.2 
#Write a function that accepts a string and prints the number of uppercase letters and lowercase
#letters.
myStr = input("enter your string:")
lrcs = 0
upcs = 0
for i in myStr:
    if i.isupper():
        upcs += 1
    if i.islower():
        lrcs += 1
print('No. of uppercase letters: ', upcs, '\n', 'No. of lowercase letters:', lrcs)
#%%No.3
#Create a function that takes a list and returns a new list with unique elements of the first list.
myList = eval(input("Enter your list:"))
print(list(set(myList)))
#%% No.4
#Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.
from functools import reduce
myInput = input("Enter a hyphen-separated sequence of words: ")
myList = myInput.split('-')
myList.sort()
print(reduce(lambda x,y : x + '-' + y, myList))
#%% No.5
#Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.
print(input("Enter your string:").upper())
#%% No.6
#Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.
def myFunction(a,b):
    print(int(a)+int(b))
#myFunction(2,'3')
#%% No.7
#Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.
def myFunction(a,b):
    m = max(len(a),len(b))
    if len(a) >= m:
        print(a)
    if len(b) >= m:
        print(b)
#myFunction('asdf','qwerty')
#%% No.8
#Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).
def myFunction():
    print(tuple([(lambda x : x**2)(i) for i in range(21)]))
myFunction()
#Why is this a function if there is no variable input required for it?
#Should the 20 in the question be changed into an arbitrary parameter?
#%% No. 9
#Write a function called showNumbers that takes a parameter called limit. It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers.

def showNumbers(limit):
    parity = ['EVEN', 'ODD']
    for i in range(limit+1):
        print(i, parity[i % 2])
#showNumbers(20)
#%% no. 10
#Write a program which uses filter() to make a list whose elements are even numbers between 1
#and 20 (both included)
print(list(filter(lambda x : (x+1) % 2, [i for i in range(21)] )))
#%% No.11
#Write a program which uses map() and filter() to make a list whose elements are squares of even
#numbers in [1,2,3,4,5,6,7,8,9,10].
myList = list(filter(lambda x : (x+1) % 2, [i for i in range(1,11)] ))
print(list(map(lambda x : x**2, myList)))
#%% No.12
#Write a function to compute 5/0 and use try/except to catch the exceptions
try:
    x = 5/0
    print(x)
except:
    print('something went wrong!!')
#%% No. 13
#Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce()
myList = [i for i in range(1,8)]
output = reduce(lambda x, y : str(x) + str(y),myList)
print(output)
#%% No. 14
#Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.
#From what? a user input list? I will simply do this for numbers from 1 to 1000 but comment out a version which takes input
myList = [i for i in range(1,1000)]
#myList = eval(input("Enter your list:"))
output = list(filter(lambda x : x % 3 != 0 and x % 7 == 0,myList))
print(output)
#%% No. 15
#Write a program in Python to multiply the elements of a list by itself using a traditional function
#and pass the function to map() to complete the operation.
testlist = [i for i in range(1,10)]
def mysquare(x):
    return x**2
output = list(map(mysquare,testlist))
print(output)
#%% No. 16
#What is the output of the following codes:
#(i)
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
#OUTPUT:
#2
#%%
#(ii) 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()
#OUTPUT
#after f
#after f?
#Traceback NameError: name 'f' is not defined.