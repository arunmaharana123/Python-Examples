# -*- coding: utf-8 -*-

from sys import argv

script, file_name = argv

print "You selected %s file" %file_name

file_object = open(file_name, 'w')

type = raw_input("type here... >")
file_object.write(type)
file_object.close()
