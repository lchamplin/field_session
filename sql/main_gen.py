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
        # engine = create_engine('postgresql://postgres:mypassword@fsdatabase.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)
        # engine = create_engine('postgresql://postgres:mypassword@fsdatabase1.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)
        engine = create_engine('postgresql://postgres:mypassword@fsdatabase2.ch2bjjecacbc.us-west-2.rds.amazonaws.com:8080/postgres')#, echo=True)

        
        # uncomment and run code below if it forgets the geometry library
        # with engine.connect() as conn:
        #         conn.execute(text("""CREATE EXTENSION postgis;"""))

        # Session = sessionmaker(engine)  
        # session = Session()

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        for i in range(0, 10):
                generator = Generator(engine, N_companies=6750, N_betatests=3250, N_demos=3250, N_onsitesupports=3250,
                N_clients=12500, N_programmers=20000, N_salesperson=6250, N_users=28000, N_projects=10000, iteration=i)
                generator.genAll()
                print(i)


        return 0



# main()