#Guessing a number
#Author: Joana Ruas


NumToGuess=2                                     #defining the correct answer
guess=int(input('Please insert a number: '))     #taking a number as input for comparison    

while guess != NumToGuess:       
    if guess>NumToGuess:
        print('Too high')                
        guess=int(input('Please try again: '))       #Answer if not correct
    elif guess<NumToGuess:
        print('Too low')
        guess=int(input('Please try again: '))

print('Well done! Yes the number was {}.'. format(NumToGuess)) #Answer if correct