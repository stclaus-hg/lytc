__author__ = 'stclaus'

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def load_dbase(db_filename=dbfilename):
    import sys
    db_file = open(db_filename, 'r')
    sys.stdin = db_file
    key = input()
    db = {}
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = value
            field = input()
        db[key] = rec
        key = input()
    db_file.close()
    return db


def store_dbase(db):
    db_file = open(dbfilename, 'w')

    for key in db:
        print(key, file=db_file)
        for name, value in db[key].items():
            print(name+RECSEP+repr(value), file=db_file)
        print(ENDREC, file=db_file)
    print(ENDDB, file=db_file)
    db_file.close()


if  __name__ == '__main__':
    from initdata import db
    store_dbase(db)
    print(load_dbase())