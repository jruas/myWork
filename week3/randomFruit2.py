#This program prints out a random fruit
#Author: Joana Ruas

import random
fruits=('Apple','Orange','Banana','Pear')

# we want a random between 0 and lenght-1
index=random.randint(0,len(fruits)-1)

fruit=fruits[index]
print('A random fruit is {}'.format(fruit))