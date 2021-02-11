# Program keeps reading numbers until the user enters 0.
#it will then pring back out again and print the average.

numbers =[]

# first number then we check if it is 0 in the while loop.
number=int(input('Please enter a number (0 to quit): '))

while number!=0:
    numbers.append(number)

# read the next number and check if it is zero.
    number=int(input('Please enter a number(0 to quit): '))
for value in numbers:
    print(value)

#Average to be a float
average=float(sum(numbers)/len(numbers))
print ('The average is {} '. format(average))