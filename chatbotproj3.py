import os
import sys
import numpy as np

os.system('color 3f') 

print('Hello! I\'m Elth. I\'m your personal assistant.!') 
print('Before starting please tell me your first name')

firstName = input()

print('Please tell me your last name')

lastName = input()

print('Your name is, ' + firstName + " " + lastName + '!!')
print()
print('And your gender?')
print('Type \'M\' for Male and any other key for Female ')
geninput = input()

if geninput=='m' or geninput=='M':
	print('You are Male')
else:
	 print('You are Female')

print()
numage = True
while numage:
	print('May I know your age?')
	age = input()
	if age.isdigit() == False:
		numage = True
		print('I couldn\'t quite get how that response can be your age :/ Please enter your valid age.')
		
	else:
		numage = False
		print('Your age is ' + age)

print()		
print('Congratulations! Registration Successful!')
print()
print()
print('Now, enter your First Name again.')
firstName2 = input()

if firstName == firstName2:
    print('Enter your Last Name again')
    lastName2 = input()
    if lastName == lastName2:
        print('Hello ' + firstName + ' ' + lastName + ', How are you? For a sample of my work I can show you how to make a transpose of a 3X3 matrix.')


       

else:
    print('Seems like you have not registered. Please start new registration. Thank you.')
    print('Enter any key to exit')
    input('')
    sys.exit()

a = [ [0] * 3 for i in range(3) ]
for i in range (3):
    for j in range(3):
        print("Enter Element:",i,j)
        a[i][j] = int(input())

print(np.matrix(a))

def transpose(a): 
     for i in range(3): 
        for j in range(i+1, 3): 
            a[i][j], a[j][i] = a[j][i], a[i][j]

transpose(a)
print()
print()
print(np.matrix(a))
print('Enter any key to exit')
input('')