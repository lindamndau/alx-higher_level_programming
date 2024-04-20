#!/usr/bin/python3

import MySQLdb

db = mysql.connect(username = sys.arg[1], passwd = sys.arg[2], database_name = sys.arg[3], state_name = sys.arg[4])
c = db.cusor()
c = c.execute('SELECT  'cities' FROM 'c'.'id', IF 's'.'name' == 's'.'id''):
    for cities in states.fetchall():
        print(cities)
