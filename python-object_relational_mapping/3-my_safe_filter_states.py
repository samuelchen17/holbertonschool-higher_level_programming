#!/usr/bin/python3
"""
select all in states where name matches arg
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

    state_name = sys.argv[4]

    query = """
        "SELECT id, name "
        "FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY id ASC"
    """
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
