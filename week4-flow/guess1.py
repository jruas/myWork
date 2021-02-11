#Guessing a number
#Author: Joana Ruas


NumToGuess=2                                     #defining the correct answer
guess=int(input('Please insert a number: '))     #taking a number as input for comparison    

while guess != NumToGuess:                       #comparing the number from input with the correct answer. Code will run while numbers are different
    guess=int(input('Please try again: '))       #Answer if not correct

print('Well done! Yes the number was {}.'. format(NumToGuess)) #Answer if correct