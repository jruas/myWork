#This program puts 10 random numbers into a queu(list).
#The program than outputs all the values in the list.
#then take the numbers from the queu one at the time


import random
queue= []
runs=10
rangeTo=100

for n in range(0, runs):
    queue.append(random.randint (0,rangeTo))
print("queue is {}" . format(queue))

while len(queue) !=0:
    currentNumber=queue.pop(0)
    print("Current Number is {} and the queue is {}" . format(currentNumber,queue))

print("the queue is now empty")