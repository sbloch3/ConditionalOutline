'''
This outline will help solidify concepts from the Conditionals lesson.
Fill in this outline as the instructor goes through the lesson.
'''
from pickle import TRUE

#1) Make a int variable named a. Now make an if statement, and if a is more than
#5, print out "a is more than 5."
a = 6
if a > 5:
    print("a is more than 5")

#2) Make a boolean variable named b. Now make an if statement, and if b is True
#print out "b is True."
b = True
if b:
    print("b is True")
#3) Make an int variable named c. Now make an if/elif statement, and if c is 
#more than 0, print "c is positive". Else if c is less than 0, print "c is
#negative".
c = 1
if c > 0:
    print("c is positive")
    
else:
    print("c is negative")    

#4) Make an int variable named d. Now make an if/elif/else statement, and if 
#d is more than 0, print "d is positive". Else if d is less than 0, print "c is
#negative". Else, print "d is zero".
d = 1
if d > 0:
    print("d is positive")

elif d < 0:
    print("d is negative")
    
else:
    print("d is zero")
        
#5) Make an if statement with any comparison, with a common SYNTAX error.
s = 1
if s>0

