__author__ = 'stclaus'

from person_start import Person

class Manager(Person):
    def __init__(self, name, age, pay=0, job=None):
        super(Manager, self).__init__(name, age, pay, 'manager')

    def give_raise(self, percent, bonus=0.1):
        super(Manager, self).give_raise(percent+bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 40000, 'software')
    sue = Person('Sue Jones', 45, 50000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)
    print(sue, sue.pay, sue.last_name())

    for person in (bob, sue, tom):
        person.give_raise(.10)
        print(person)
