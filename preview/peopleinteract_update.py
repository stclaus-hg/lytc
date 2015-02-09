import shelve
from person_start import Person

__author__ = 'stclaus'

fieldnames = ('name', 'age', 'pay', 'job')
maxfield = max([len(field) for field in fieldnames])
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? =>')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        curval = getattr(record, field)
        newval = input('\t[%s]=%s\n\t\tnew=>?' % (field, curval))
        if newval:
            setattr(record, field, eval(newval))
    db[key] = record
db.close()