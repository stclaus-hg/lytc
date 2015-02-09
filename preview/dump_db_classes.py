__author__ = 'stclaus'

import shelve

db = shelve.open('class-shelve')

for key in db.keys():
    print(key, '=>', db[key].name, db[key].pay)

bob = db['bob']
print(bob.last_name())
print(db['tom'].last_name())
db.close()