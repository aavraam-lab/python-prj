#This is my first program in python. Trying various things and capabilities of python
from datetime import datetime
import getpass

todaysDate = datetime.today().strftime('%d-%m-%Y')
welcomeMessage = "Hello " + getpass.getuser() + ' , welcome!'
userActions = 0




print('\n-------------------------------------------------------------------')
print('Date: ', todaysDate)
print(welcomeMessage)
print('This program is just an introduction to Python programming language')
print('-------------------------------------------------------------------')

userName = input('What\'s your name dear: ')
userActions = userActions + 1
print('\nOkay ',userName,' let\'s start!')

userAge = int(input('What\'s your age: '))
userActions = userActions + 1


if(userAge < 18):
    print('>>So you are not an adult yet.\n')
else:   
    print('>>Oh you are an adult.\n')



print('You did a total of ',userActions,' actions. Perfect job!')
print('Goodbye, ', getpass.getuser(), ' || Program exiting...')







