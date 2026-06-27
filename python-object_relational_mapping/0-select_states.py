#!/usr/bin/python3
"""
List all states in db
"""

import MySQLdb
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb(host="localhost", port=3306, user=uid, passwd=pw, database=db)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
