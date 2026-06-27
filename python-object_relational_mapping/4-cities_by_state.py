#!/usr/bin/python3
"""
list all cities in db
"""

import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    cur = conn.cursor()

    query = """
        SELECT id, name 
        FROM states 
        WHERE BINARY name = %s 
        ORDER BY id ASC
    """
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
