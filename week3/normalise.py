#This program reads in a string and strips any leading or trailing spaces. 
#The program also convert the string to lower case
#The program also output the lenght of the input and output strings.
#Author: Joana Ruas

rawString=input('Please insert a string: ')
normalisedString=rawString.strip().lower()

lengthRS=len(rawString)
lengthNS=len(normalisedString)

print ('The string normalised is {}'.format(normalisedString))
print ('We have reduced the input string from {} to {}'.format(lengthRS,lengthNS)
)