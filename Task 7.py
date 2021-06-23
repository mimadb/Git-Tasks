#TASK Seven
#%% No.1
# Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.
C = 50
H = 30
myInput = input('Enter your comma separated values: ')
myList = myInput.split(',')
myList = map(int,myList)
for D in myList:
    print("For input ",D)
    Q = (2 * C * D / H) ** 0.5
    print('The output is ', Q)
#Am i supposed to be using classes/objects for this?

#%% No.2 
# Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length**2

x = Square(5)
y = Shape()
print(y.area())
print(x.area())
#%% No.3
# Create a class to find three elements that sum to zero from a set of n real numbers
class finder():
    def __init__(self,numbers):
        self.numbers = numbers
    def find(self):
        found = []
        for i in range(len(self.numbers)):
            for j in range(i+1,len(self.numbers)):
                for k in range(j+1,len(self.numbers)):
                    if self.numbers[i]+self.numbers[j]+self.numbers[k] == 0:
                        found.append((self.numbers[i],self.numbers[j],self.numbers[k]))
        return(found)
mylist = [-3,-2,-1,0,1,2,5]
x = finder(mylist)
print(x.find())
        #Output: [(-3, -2, 5), (-3, 1, 2), (-2, 0, 2), (-1, 0, 1)]
#%%No.4
# Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
        while self.minutes > 59:
            self.minutes += -60
            self.hours += 1
    def addTime(self,other):
        self.minutes += other.minutes
        self.hours += other.hours
        while self.minutes > 59:
            self.minutes += -60
            self.hours += 1
    def displayTime(self):
        print('the current time is: ', self.hours, ':',self.minutes)
    def displayMinute(self):
        print('Current time in minutes: ', self.hours * 60 + self.minutes)      
        
x = Time(4,50)
y = Time(2,75)
x.displayTime()
y.displayTime()
y.displayMinute()
y.addTime(x)
y.displayTime()
#%% No.5
# Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.
class Person:
    def __init__(self,age):
        self.age = age
        if age < 0:
            print('Age is not valid, setting age to 0')
            self.age = 0
    def yearPasses(self, years):
        self.age += years
    def amIOld(self):
        if self.age < 13:
            print('You are young!')
        elif self.age <= 19:
            print('You are a teenager!')
        else:
            print('its okay youre not that old...')

Imad = Person(9)
Imad.amIOld()
Imad.yearPasses(8)
Imad.amIOld()
Imad.yearPasses(50)
Imad.amIOld()
print(Imad.age)