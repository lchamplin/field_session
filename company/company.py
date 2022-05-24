from sqlalchemy import Column, ForeignKey, Integer, Table, String
from sqlalchemy.orm import declarative_base, relationship

from typing import List

from event.event import Event
from people.person import Person
from people.client import Client
from people.programmer import Programmer
from project.project import Project

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    # ceo = Column(String(250))
    programmers = relationship("Programmer")
    # clients = relationship("Client", backref="company")
    # projects = relationship("Project", backref="company")
    # events = relationship("Event", backref="company")
    description = Column(String(250))




#     class Parent(Base):
#     __tablename__ = "parent"
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child")


# class Child(Base):
#     __tablename__ = "child"
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey("parent.id"))

