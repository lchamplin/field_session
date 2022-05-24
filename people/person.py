from sqlalchemy import Column, ForeignKey, Integer, Table, String
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class Person():
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))

