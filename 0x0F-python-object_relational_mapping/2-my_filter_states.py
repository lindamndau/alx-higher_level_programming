#!/usr/bin/python3

import sys
import MySQLdb

db = MySQLdb.connect(username = sys.argv[1], passwd = sys.argv[2], database = sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM states WHERE BINARY name ='{}'",format(sys.argv[4],))
[print(state) for state in c.fetchall()
