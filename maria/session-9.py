# oop

from abc import ABC


class Person:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)


p1 = Person('Maria')
# print(p1.name) #dot yourself into fields

p1.printName()
print(p1)


class VIAStudent:
    where = 'VIA'

    def __init__(self):
        self.where += " Horsens"


print(VIAStudent.where)
print(VIAStudent().where)


# Class decorators -- @classmethod
# to decorate an ordinary method

class Person:
    TITLES = ('Software Engineer', 'System Analyst', 'Backend Engineer', 'Data Engineer')

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def fullname(self):
        return self.firstName + " " + self.lastName

    @classmethod
    def allowedTitlesStartingWith(cls, startsWith):  # class decorator
        return [t for t in cls.TITLES if t.startswith(startsWith)]

    @staticmethod
    def allowedTitlesEndWith(endsWith):  # static method
        return [t for t in Person.TITLES if t.endswith(endsWith)]


p2 = Person('Maria', 'Frandsen')
print(p2.fullname())
print(p2.allowedTitlesStartingWith('S'))
print(Person('M', 'F').allowedTitlesStartingWith('B'))
print(Person.allowedTitlesEndWith('r'))


class Car(object):
    def __init__(self):
        self._speed = 90

    @property  # class decorator - can use it to change/generate values
    # lets method behave like an attribute
    def speed(self):
        print('Your speed is ', self._speed)

    # @set
    # def set_speed(self, speed):
    #    self._speed = speed
    #    print('speed is now ', speed)

    @speed.setter
    def speed(self, value):
        self._speed = value
        print('speed is now ', value)


car = Car()
car.speed = 110


# first iteration
class V:
    pass  # placeholder for future code


class C(V):
    pass


class M(V):
    pass


# second iteration
class V:
    def __init__(self, n):
        self._n = n

    def getNumberOfTires(self):
        return self._n

    def setNumberOfTires(self, n):
        self._n = n

    def getDescription(self):
        return "A vehicle with " + self._n + " tire(s)"


class C(V):
    def __init__(self, plate_number, n):  # subclas constructor
        super().__init__(n)  # call the super class constructor
        self._plate_number = plate_number

    def setPlateNumber(self, plate_number):
        self._plate_number = plate_number

    def getDescription(self):
        return "A car with plate number : " + self._plate_number


class M(V):
    pass


c = C('123', 4)
print(c.getDescription())


# class DerivedClass(SuperClass1, SuperClass2)
# Multiple inheritance with Mixin semantics

class Contact:
    def __init__(self, name, email):
        self.email = email
        self.name = name


class MailSender:
    def sendMail(self, msg):
        print(msg)
        print("Sending: { " + msg + "} to " + self.email)


class EmailableContact(Contact, MailSender):
    pass


em = EmailableContact('maria', 'maria@usloge.dk')
em.sendMail("hi")


# exercise 9.1

class MyRecipe:
    def __init__(self, calories, cookTime):
        self.calories = calories
        self.cookTime = cookTime

    def cook(self, name):
        print(name + " " + self.cookTime + " " + self.calories)


class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name + " " + self.email


class AddressHolder:
    def __init__(self, street, post_code, city_str):
        self.street = street
        self.post_code = post_code
        self.city_str = city_str

    def __str__(self):
        return "street: " + self.street + " post code: " + self.post_code + " city str: " + self.city_str


class Friend(Contact, AddressHolder):
    def __init__(self, phoneNumber):
        Contact.__init__(self, "name", "email")
        AddressHolder.__init__(self, "street", "post_code", "city_str")
        self.phone_number = phoneNumber

    def __str__(self):
        return Contact.__str__(self) + " " + AddressHolder.__str__(self) + " " + self.phone_number


friend = Friend('1')
print(friend.__str__())


class Fish:
    def eat(self):
        print("generic food")

    def swim(self):
        return "swim in "


class Shark(Fish):
    def __init__(self, name, placeFound):
        super().__init__()
        self.name = name
        self.placeFound = placeFound

    def eat(self):
        print("Meat")

    def swim(self):
        print(super().swim() + self.placeFound)


class Dolphin(Fish):
    pass


s = Shark('bob shark', 'ocean')
s.swim()


class CaffeineDrink:
    def __init__(self, description, size):
        self.description = description
        self.size = size

    def drinkInfo(self):
        return " description: " + self.description + ", size: " + self.size

    # def getPrice(self):
    #    pass


class Tea(CaffeineDrink):
    def __init__(self, quantity):
        super().__init__(" black", "large")
        self.quantity = quantity

    def getDescription(self):
        return "quantity: " + str(self.quantity) + " " + self.drinkInfo()


tea = Tea(5)
print(tea.getDescription())
