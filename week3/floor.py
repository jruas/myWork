#This program takes in a float and outputs an int rounded down

import math

numberToFloor=float(input('Please insert a number: '))
flooredNumber=math.floor(numberToFloor)

print ('{} floored is {}'.format(numberToFloor,flooredNumber))