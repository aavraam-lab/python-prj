#Simple script testing multiple things alongside studying
from datetime import datetime

PI = 3.14

print('Todays date: ', datetime.today().strftime('%d-%m-%Y'))


x = input('\nPlease give me the radius of a circle: ')
try:
    radius = float(x)
    print('The perimeter: ', PI*(radius*radius), ' units')
    print('The area: ', 2*PI*radius, ' square units\n')
except:
    print('*** Error, that was not a number ***')


x = input('Please give me your name: ')
y = input ('Please give me your surname: ')

print('Going backwaaaards: ',x[::-1],' ',y[::-1],'\n')

names = ['Mary','John','George','Maria','Jason','Jackson','Jayleen']

print('I have a list of ',len(names),' names')
print('The names at odd positions printed: ')
print('   -->', names[::2])
print('The names at even positions printed: ')
print('   -->', names[1::2])


#String split based upon delimiter
x = input('Give me a filename with extension to it: ')
print('File type: ',x.split("."))

#Extract elements from tuple (non-callable)
exam = (11,12,2014)
(day,month,year) = exam
print('The examination will be held on : ', day, month, year) 



















