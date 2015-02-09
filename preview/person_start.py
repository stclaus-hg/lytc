__author__ = 'stclaus'

class Person(object):
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s: %s, %s>' % (self.__class__.__name__, self.name, self.job, self.pay)

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 40000, 'software')
    sue = Person('Sue Jones', 45, 50000, 'hardwate')

    print(bob.last_name())
    sue.give_raise(10)
    print(sue.pay)
