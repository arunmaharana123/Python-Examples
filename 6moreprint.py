# -*- coding: utf-8 -*-

dots = "." * 10
print dots

name = "Arun"
surname = "Maharana"

print name,
print surname


age = 27
salary = 14864.00

#print "Hi, My name is ", name, "and", age, "years old", "and My salary is", salary
print "Hi, My name is %r and %r years old. I am working in a company and getting %r rupees. \nThank You" %(name, age, salary)
