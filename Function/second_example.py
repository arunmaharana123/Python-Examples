
def callME(number):
    print number
    number -= 1
    if number != 0:
        callME(number)
callME(10)


def getName(id):
    print "ID :", id
    return "Arun"

name = getName(1)
print "Name :", name
