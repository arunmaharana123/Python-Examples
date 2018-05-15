# -*- coding: utf-8 -*-

no = 1
name = "Arun"
age = 27
salary = 14864.00

if 0 < salary < 20000:
    print "Not Good"
else:
    print "Good"

#print "Hi, My name is ", name, "and", age, "years old", "and My salary is", salary
print "Hi, My name is %r and %r years old. I am working in a company and getting %r rupees. \nThank You" %(name, age, salary)


""" If statement example"""
if age > 18:
    print "You have VoterID card."
else:
    print "You don't have voterID card."

""" If-Else statement example"""
def calculate(age):
    if age > 50:
        print "You have to take rest."
    elif age > 30:
        print "Time to marry someone. Find Here..."
    elif age > 18:
        print "You are growing faster."
    else:
        print "You are a child."

input = int(raw_input("> "))
calculate(input)
