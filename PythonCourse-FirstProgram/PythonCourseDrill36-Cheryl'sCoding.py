# -*- coding: cp1252 -*-
#Assign an integer to a variable.
x = 88

#Assign a string to a variable.
y = "Sally"

#Assign a float to a variable.
myfloat = 8

#Use the print function and .format()notation to print out the variable you assigned.
print x
print y
print myfloat
print '%d' % (x,)
print '%f' % (myfloat,)
print '%-10s' % (y,)

#Use the operators +, - , * , / , +=, ­= , %.

x = 39
y = 52
z = 0

print x + y
print y - x
print x * y
print y / x

z = x + y
print "Line 1 - Value of z is ", z

z = x = y
print "Line 2 - Value of z is ", z

z = x * y
print "Line 3 - Value of z is ", z

z = x / y
print "Line 4 - Value of z is ", z

z += x
print "Line 5 - Value of z is ", z

z -= x
print "Line 6 - Value of z is ", z

z % x
print "Line 7 - Value of z is ", z

#More practice with +=, ­= , % operators

z = 5
z = z - x
z -= x
print z

w = 2
w = w + y
w += y
print w

a = 7
a = a % w
a %= w
print a

#Use logical operators and, or, not.

x = 1
y = 3
z = 5

print 1, x == 1
print 2, x == 2
print 3, x == 1 and y == 3
print 4, x == 2 and y == 3
print 5, not x == 3 and y == 3
print 6, x == 3 or y == 1
print 7, x == 3 and y == 1
print 8, not (x == 3 and y == 1)
print 9, not x == 3 and y == 1

print x == (x or y)
print y == (x or y)
print x == (x and y)
print y == (x and y)

#Use conditional statements if, elif, else.

#Start if statement
if x==86:
    print 'x = 86'
#If x does not equal 86, but equals 42, run this
elif x==42:
    print 'x = 42'
#If it's not equal to 86 or 42, run this
else:
    print 'x does not equal 86 or 42'

#Use a while loop

count = 0
while (count < 25):
   print 'The count is:', count
   count = count + 1

print "Good-bye!"

count = 0
print 'Hello!'
while (count < 60):
   print 'The count is:', count
   count = count + 3

print "Good-bye!"

#Use a for loop

for letter in 'Czechoslovakia':
   print 'Current Letter :', letter

print "Holy moley! You can spell Czechoslovakia!"

#Create a list and iterate through the list using a for loop to print each item out on a new line

animals = ['aardvark', 'bear',  'cat', 'dog', 'elephant', 'fox', 'goat', 'horse', 'impala', 'jackal', 'kangaroo', 'llama', 'mole', 'numbat', 'ostrich', 'pig', 'quail', 'rabbit', 'snake', 'tiger', 'unicorn', 'vulture', 'walrus', 'xerus', 'yak', 'zebra']
for animal in animals:
   print 'Current animal :', animal

print "That's a list of animals from A to Z!"

#Create a tuple and iterate through it using a for loop to print each item out on a new line

tup1 = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylavnia', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
for state in tup1:
    print 'Current state :', state

print "Congratulations! You know the name of every state in the United States of America!"

#Define a function that returns a string variable

#Function definition
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

#Call the function you defined above and print the result to the shell
printme("This is the theme song of Portland and Seattle:")
printme("I'm singin' in the rain, just singing in the rain")
printme("What a glorious feeling, I'm happy again")
printme("I'm laughing at the clouds so dark above")
printme("The sun's in my heart and I'm ready for love")
printme("Let the stormy clouds chase everyone from the place")
printme("Come on with the rain, I've a smile on my face")
printme("I'll walk down the lane with a happy refrain")
printme("And singin', just singin' in the rain")



