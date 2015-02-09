__author__ = 'stclaus'
import shelve

from person_start import Person
from manager import Manager

bob = Person('Bob Smith', 42, 40000, 'software')
sue = Person('Sue Jones', 45, 50000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()