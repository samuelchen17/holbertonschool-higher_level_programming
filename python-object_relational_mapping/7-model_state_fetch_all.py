#!/usr/bin/python3
"""
Module to fetch all states
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

if __name__ == "__main__":

    url = URL.create(
        "mysql+mysqldb",
        username=sys.argv[1],
        password=sys.argv[2],
        host="localhost",
        port=3306,
        database=sys.argv[3],
    )

    engine = create_engine(
        url,
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        print(f"{state.id}: {state.name}")
