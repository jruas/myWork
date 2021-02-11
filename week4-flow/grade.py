#This program reads in
# a students percentage
#and prints out the
# corresponding grade

percentage=float(input('Please insert the percentage: '))


if percentage < 40:
   print('Fail')
elif percentage <50:
   print('Pass')
elif percentage <60:
   print('Merit 2')
elif percentage <70:
   print('Merit 1')
else:
   print ('Distinction')