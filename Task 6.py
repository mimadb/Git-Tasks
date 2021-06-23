#TASK SIX
#%% No.1
# Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.
myInput = input('type some text:')
uppercase = [i for i in myInput if i.isupper()]
print('the uppercase letters in the text you typed are: \n',uppercase)
#%% No.2
# Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.

students = eval(input('Enter a list of students in list notation (eval() command will be performed):'))
subjects = eval(input('Enter a list of subjects in list notation (eval() command will be performed):'))
myDict = dict(zip(students,subjects))

#%% No.3
#Learn More about Yield, next and Generators

#Ignore this I'm just playing around with some of this stuff
def Generator():
    i = 1
    while i < 20:
        yield i*i
        i += 1
for i in Generator():
    print(i)
    #print('and the next number is ... ',next(Generator))
#next(Generator) does not work....
iterator = Generator()
for i in iterator:
    print(i)
    print('and the next number is ... ',next(iterator))
#It works when the output of Generator() is stored somewhere
#Output:
# 1
# and the next number is ...  4
# 9
# and the next number is ...  16
# 25
# and the next number is ...  36
# 49
# and the next number is ...  64
# 81
# and the next number is ...  100
# 121
# and the next number is ...  144
# 169
# and the next number is ...  196
# 225
# and the next number is ...  256
# 289
# and the next number is ...  324
# 361
#%%No.4
# Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
def Reverse(string):
    counter = 0
    while counter < len(string):
        yield(string[-counter-1])
        counter += 1
iterator = Reverse(input('enter string to be reversed.'))
reverse = ''
for i in iterator:
    reverse += i
#%%No.5
# Write an example on decorators.

#Defining decorators to state the name of a function and when its done for debugging purposes.
def myNameIs(func):
    def returned1(*args):
        print('Hi! Im a function and my name is ', func.__name__)
        func(*args)
    return returned1

def imDone(func):
    def returned2(*args):
        func(*args)
        print('Hi!', func.__name__, 'here, im all done!')
    return returned2


@myNameIs
def testfunction1(msg):
    print(msg)


@imDone
def testfunction2(msg):
    print(msg)


@myNameIs
@imDone
def testfunction3(msg):
    print(msg)


testfunction1('Hello Consultadd')

testfunction2('Howdy Consultadd')

testfunction3('Greetings Consultadd')
#Note @myNameIs applies to @imDone and so testfunction3's first printed line has func.__name__ = 'returned2'