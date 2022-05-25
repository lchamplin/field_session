#!/usr/bin/env python

from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from objects import *
import psycopg2


from shapely.geometry import Point
from datetime import datetime



def main():
        engine = create_engine('postgresql://postgres:mypassword@fsdatabase.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres', echo=True)
        # with engine.connect() as conn:
        #         conn.execute(text("""CREATE EXTENSION postgis;"""))

        Session = sessionmaker(engine)  
        session = Session()
        Base.metadata.create_all(engine)
        
        l = Programmer(first_name="Lauren", last_name="Champlin", years_of_experience=4)
        g = Programmer(first_name="Graham", last_name="Stookey", years_of_experience=1)
        a = Programmer(first_name="Ash", last_name="B", years_of_experience=3)
        
        session.add(l)
        session.add(g)
        session.add(a)
        session.commit()

        programmers = session.query(Programmer)  
        for p in programmers:  
                print(p.first_name)
     
        return 0



main()