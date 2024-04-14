#!/usr/bin/python3
# Lists all states from hbtn_0e_0_usa database

import sys
import  MySQLdb

if__name__ == "__main__":
my_database = MySQLdb.connect(user =sys.argv[1], passwd=sys.argv[2], my_database=sys.argv[3])
    c = my_database.cursor()
    c.execute("SELECT * FROM 'states'")
    [print(state) for state in c.fetchall()]
