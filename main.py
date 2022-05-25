#!/usr/bin/env python

from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from objects import *
from gen import Generator
import contextlib
from sqlalchemy import MetaData
import psycopg2


from shapely.geometry import Point
from datetime import datetime



def main():
        engine = create_engine('postgresql://postgres:mypassword@fsdatabase.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres', echo=True)
        # uncomment and run code below if it forgets the geometry library
        # with engine.connect() as conn:
        #         conn.execute(text("""CREATE EXTENSION postgis;"""))

        # Session = sessionmaker(engine)  
        # session = Session()

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        generator = Generator(engine, N_companies=10, N_betatests=1, N_demos=3, N_onsitesupports=1,
         N_clients=20, N_programmers=20, N_salesperson=10, N_users=50, N_projects=30)
        generator.genAll()

        
        # g = Programmer(first_name="Graham", last_name="Stookey", years_of_experience=1)
        # p = Project(language="Java", programmers=[g], in_production=True)
        # l = Programmer(first_name="Lauren", last_name="Champlin", projects = [p], years_of_experience=4)
        # a = Programmer(first_name="Ash", last_name="B", years_of_experience=3)
        # c = Company(name="ICR", programmers=[l, g, a], projects = [p], description="best company ever")
        
        # session.add(l)
        # session.add(g)
        # session.add(a)
        # session.add(c)
        # session.commit() 
        # print(session.query(Programmer)[3])     

        return 0



main()