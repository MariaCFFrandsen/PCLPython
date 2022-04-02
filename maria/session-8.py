import json
import math
# for loop

def functionforprints():
    for i in range(1, 11):
        print('%d x 5 = %d' % (i, i * 5))


def listprints():
    l = range(1, 11)
    for i in l:
        print('%d x 5 = %d' % (l[i - 1], l[i - 1] * 5))


# listprints()
'''
hetero_list = [0, 'en', 2, 3, 'four', 5, 6, 7, 8, 9]
print(hetero_list[1])
print(hetero_list[-1])
print(hetero_list[:3])
print(hetero_list[3:])
print(hetero_list[3:-3])
'''
# tuples
WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


# print(WEEKDAYS[3])

# Dictionary


# d1 = {'code': 'PCL1', 'titel': 'python'}
# print(d1['code'])
# print(d1.get('code'))
# d1.clear()  # clean all

def factorial():
    number = input("write a number")
    print(math.factorial(int(number)))

def factorial2():
    number = input("write a number")
    res = 0
    for i in range(int(number)):
        res = res * i

def dumpcoffee():
    gtg_dd = {'drink': 'coffee', 'price': 7.0}
    json.dumps(gtg_dd)

# Exercises 8

def exercise8():
    print('This program prints a string 5 times')
    for count in range(5):
        print('Python is cool')


def exercise81():
    for count in range(10):
        print('Maria %d', 293197)


def exercise81():
    wish = input("what do you wish for?")
    number = input("how many of that do you wish for?")
    for count in range(int(number)):
        print(wish)


def sumImperative():
    x = 0
    for i in range(1, 6):
        x = x + i
    print(x)

def printuntiluneven():
    number = input("enter a number")
    while int(number) % 2 == 0:
        print('your number was ', number)
        number = input("enter a number")
    print('bye for now!')

def groupList(l, gLength):
    iterative = int(len(l)/gLength)
    list = []
    for i in range(0, iterative):
        list.append(l[gLength * i:gLength * (i + 1)])
    print(list)


d1 = {'bob': 'iot', 'dora': 'interactive design', 'paw petrol': 'data engineering'}
#change bob's special to data engineering

d1['bob'] = 'data engineering'
print(d1.get('bob'))

#Add a new entry for "Farmer Pickles" with specialization "Climate Engineering"
d1.update({'Farmer Pickles': 'Climate Engineering'})
print(d1.get('Farmer Pickles'))

#print doras specialization
d1.get('dora')

#Print all the keys. Don’t worry about the format.
for key, value in d1.items():
    print(key)

#Using the imperative coding styleimplement a program that allow users to enter
# a number that represents a shape and then calculates the area accordingly.

def calArea():
    width = int(input('enter width'))
    length = int(input('enter length'))
    print('area of firkant = ', width * length)
