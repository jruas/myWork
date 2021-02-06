# This program reads in two numbers and divides the first one by the second and give the integer result and the remainder
# Author: Joana Ruas

x=int(input ('Please insert a number'))
y=int(input ('Please insert a second number'))
a1=int(x/y)
a2=x%y


print ('{} divided by {} is {} and the remainer is {}' .format (x, y, (a1), a2))