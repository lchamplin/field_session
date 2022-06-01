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
        engine = create_engine('postgresql://postgres:mypassword@fsdatabase.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)
        # engine = create_engine('postgresql://postgres:mypassword@fsdatabase1.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)

        
        # uncomment and run code below if it forgets the geometry library
        # with engine.connect() as conn:
        #         conn.execute(text("""CREATE EXTENSION postgis;"""))

        # Session = sessionmaker(engine)  
        # session = Session()

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        generator = Generator(engine, N_companies=675, N_betatests=325, N_demos=325, N_onsitesupports=325,
         N_clients=1250, N_programmers=2000, N_salesperson=625, N_users=2800, N_projects=1000)
        generator.genAll()

        
        # g = Programmer(first_name="Graham", last_name="Stookey", years_of_experience=1)
        # p = Project(language="Java", programmers=[g], in_production=True)
        # l = Programmer(first_name="Lauren", last_name="Champlin", projects = [p], years_of_experience=4)
        # a = Programmer(first_name="Ash", last_name="B", years_of_experience=3)
        # m = Programmer(first_name="Manisha", last_name="J", years_of_experience=1)
        # c = Company(name="ICR", programmers=[l, g], projects = [p], description="best company ever")
        
        # session.add(l)
        # session.add(g)
        # session.add(a)
        # session.add(c)
        # session.commit() 
        # print(session.query(Programmer)[3])     



        return 0



main()