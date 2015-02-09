import shelve

__author__ = 'stclaus'

fieldnames = ('name', 'age', 'pay', 'job')
maxfield = max([len(field) for field in fieldnames])
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? =>')
    if not key:
        break
    try:
       record = db[key]
    except:
        print('key "%s" not found' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
    print(key)
db.close()