#TASK FIVE
#No. 1: Write a program in Python to allow the error of syntax to be handled using exception handling.
try:
    eval(input("Write some syntactically faulty code:")) #I write 'a'=1 and it runs the except SyntaxError: block
except SyntaxError:
    print('there was a syntaxerror')
except:
    print('something else went wrong')
#%%No.2 
# Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
import sys
while True:
    try:
        f = open(sys.argv[1],'r')
        break
    except FileNotFoundError:
        print('The file was not found, double check the name and try again!')
    except:
        print('something else went wrong...did you pass a command line argument with file name?')
        break

#%% No.3
# Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
while True:
    try:
        x = input("enter a four digit number: ")
        if x.isnumeric() == False:
            raise Exception('okay this one is just not a number....')
        if len(x) != 4:
            raise Exception('The length is too short/long !!! Please provide only four digits')
        else:
            print('thank you!')
            break
    except Exception as y:
        print(y)
        print('please try again.')
#%%No.4
# Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

myUsername = 'imad'
myPassword = 'consultadd'

counter = 0
loggedin = False

while counter < 3 and loggedin == False:
    inputUsername = input('enter username: ')
    inputPassword = input('enter password: ')
    try:
        if inputUsername == myUsername:
            if inputPassword == myPassword:
                loggedin = True
                print('logged in successfully!')
            else:
                raise Exception('Wrong Password: Try again')
        else:
            raise Exception('Wrong Username: Try Again')
    except Exception as x:
        print(x)
        counter += 1
        print('You have ',2-counter+1, ' attempts left.')
if loggedin == False:
    print('too many attempts, account has been locked, please contact system admin :)')
    
#%% No.5
# Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling

# Thank you it was a good read.
#%% No.6

# Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

# PLEASE READ:
# Only the even length string? Words? or lines? I am once again not sure what
# this question is asking for so I am offering two solutions, one which selects
# words of even length and one which selects lines of even length.

f = open('doc.txt')
myText = f.read()
f.close()
byline = myText.split('\n')
byword = []
for i in byline:
    byword += i.split(' ')
evenfilter = lambda x : (len(x) % 2) == 0
evenline = list(filter(evenfilter, byline))
evenwords = list(filter(evenfilter, byword))
print(evenline)
print(evenwords)
#OUTPUT:
# ['Where you need to return the data string']
# ['am', 'file', 'need', 'to', 'return', 'data', 'string', 'is', 'of', 'even', 'length', 'Make', 'sure', 'return', 'in', 'same', 'link', 'as', 'it', 'is', 'present.']
