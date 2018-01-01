from walrus import *

db = Database(host='localhost', port=6379, db=0)
ac = db.autocomplete()
