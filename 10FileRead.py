from sys import argv

script, file_name = argv

print "You select %s file." %file_name

open_file = open(file_name)
print open_file.read()

file_name = raw_input("new file to read > ")
open_file = open(file_name)
print open_file.read()
