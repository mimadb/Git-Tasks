#############################
#          TASK TWO         #
#############################
#%% No.1:
#Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “Python Training” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
#string.
x = int(input("Enter your number:"))
if x % 3 == 0:
    print('Consultadd', end='')
if x % 3 == 0 and x % 5 == 0:
    print(' - ', end='')
if x % 5 == 0:
    print('Python Training', end='')

#%% No.2:
#Write a program in Python to perform the following operator based task:
#
#Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If User Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2
#respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as
#soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#NOTE: At a time a user can only perform one action.
print("1 - Addition")
print("2 - Subtraction")
print("3 - Division")
print("4 - Multiplication")
print("5 - Average")
choice = int(input("Choose an operation:"))

num1 = float(input("Input first number:"))
num2 = float(input("Input second number:"))
answer = [num1 + num2, num1-num2, num1/num2, num1*num2]

if choice == 5:
    first = float(input("Input third number:"))
    second = float(input("Input fourth number:"))
    answer.append((num1+num2+first+second)/4)

print("Your answer is: ", answer[choice-1])
if answer[choice-1]<0:
    print("NEGATIVE")
#I was a little confused about the "enter two MORE numbers as first and second for calculating the average"
#So I interpretted it as we are taking average of 4 numbers.

#%% No. 3:
#Write a program in Python to implement the given flowchart:
a = 10
b = 20
c = 30
avg = (a+b+c)/3
print("avg = ",avg)
if avg>a and avg>b and avg>c:
    print("avg is higher than a,b,c")
    #...This is not actually ever going to happen for any a,b,c though.
elif avg>a and avg>b:
    print("avg is higher than a,b")
    #the diagram includes c in this one, assuming its a typo
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is just higher than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print("avg is just higher than c")

#%% No. 4:
#Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”
while 1:
    x = int(input("Enter your number:"))
    if x < 0:
        print("It's Over")
        break
    if x > 0:
        print("Good Going")

#%% No. 5:
#Write a program in Python which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200.

#Assuming the range is inclusive of endpoints
mylist = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        mylist.append(i)
print("Here are your numbers:", mylist)

#%%No. 6:
#What is the output of the following code examples:
    
#6a: TypeError: 'int' object is not iterable
#6b: 0 error 1 error 2 
#6c: NameError: name 'Break' is not defined
    #Assuming that typo was unintentional, it would print the numbers 0 1 2 3 4 

#%% No. 7:
#Write a program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)
#Could have also used range(6) and ommitted the condition i==6.

#%% No. 8:
#Write a program that accepts a string as an input from the user and calculate the number of digits
#and letters.
mystring = input("Write something:")
a = 0
n = 0
for i in mystring:
    if i.isalpha():
        a += 1
    if i.isnumeric():
        n += 1
print("Letters:",a,"\n Digits:",n)

#%% No. 9:
#Write a program such that it asks users to “guess the lucky number”. If the correct number is
#guessed the program stops, otherwise it continues forever.
#Modify the program so that it asks users whether they want to guess again each time. Use two
#variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
#to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
#The program continues as long as a user has not answered “no” and has not guessed the correct
#number)
import random
import time
random.seed(time.time())
number = random.randint(0, 10)
print("Generating random number between 0 and 10")


while True:
    guess = int(input("Guess the lucky number:"))
    if guess == number:
        print("Correct!")
        break
    if input("Try again?").casefold() == "no":
        break
        
#%% No.10:
#Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the
#correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
#After the fifth guess it stops and prints “Game over!”.
import random
import time
random.seed(time.time())
number = random.randint(0, 10)
print("Generating random number between 0 and 10")

counter = 1
while counter < 6:
    print("Take a guess, attempt number ",counter)
    guess = int(input())
    if guess == number:
        print("Good guess!")
    elif counter != 5:
        print("Try again!")
    counter += 1
    
print("Game Over!")
#%% No. 11:
#In the previous question, insert break after the “Good guess!” print statement. break will terminate
#the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”.
import random
import time
random.seed(time.time())
number = random.randint(0, 10)
print("Generating random number between 0 and 10")
counter = 1
while counter < 6:
    print("Take a guess, attempt number ",counter)
    guess = int(input())
    if guess == number:
        print("Good guess!")
        break
    elif counter != 5:
        print("Try again!")
    elif counter == 5:
        print("Sorry but that was not very successful...")
    counter += 1
    
print("Game Over!")