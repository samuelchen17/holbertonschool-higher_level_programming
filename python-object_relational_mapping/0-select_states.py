#!/usr/bin/python3
"""
List all states in db
"""

import MySQLdb
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=uid,
        password=pw,
        database=db_name,
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
