from walrus import *

database = Database(host='localhost', port=6379, db=0)
ac = database.autocomplete()
