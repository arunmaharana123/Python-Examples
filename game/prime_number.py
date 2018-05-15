
import math

def check_prime(number):
    first = 2
    result = 0
    print math.sqrt(number)
    while first < math.sqrt(number):
        if (number % first) == 0:
            result = 1
            break
        else:
            pass
        first += 1

    if result == 1:
        print "Not a prime number"
    else:
        print "Is a prime number"

while True == True:
    check_prime(int(raw_input("> ")))
