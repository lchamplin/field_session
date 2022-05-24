from sqlalchemy import Column, ForeignKey, Integer, Table, String, Boolean, DateTime
from geoalchemy2 import Geometry
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# ASSOCIATION TABLES ###########################################################
project_programmer_association_table = Table("association1",Base.metadata,
    Column("project_id", ForeignKey("project.id"), primary_key=True),
    Column("programmer_id", ForeignKey("programmer.id"), primary_key=True),
)
project_user_association_table = Table("association2",Base.metadata,
    Column("project_id", ForeignKey("project.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)
client_company_association_table = Table("association3",Base.metadata,
    Column("client_id", ForeignKey("client.id"), primary_key=True),
    Column("company_id", ForeignKey("company.id"), primary_key=True),
)
client_betatest_association_table = Table("association4",Base.metadata,
    Column("client_id", ForeignKey("client.id"), primary_key=True),
    Column("betatest_id", ForeignKey("betatest.id"), primary_key=True),
)
betatest_user_association_table = Table("association5",Base.metadata,
    Column("betatest_id", ForeignKey("betatest.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)
demo_salesperson_association_table = Table("association6",Base.metadata,
    Column("demo_id", ForeignKey("demo.id"), primary_key=True),
    Column("salesperson_id", ForeignKey("salesperson.id"), primary_key=True),
)
demo_client_association_table = Table("association7",Base.metadata,
    Column("demo_id", ForeignKey("demo.id"), primary_key=True),
    Column("client_id", ForeignKey("client.id"), primary_key=True),
)
onsitesupport_programmer_association_table = Table("association8",Base.metadata,
    Column("onsitesupport_id", ForeignKey("onsitesupport.id"), primary_key=True),
    Column("programmer_id", ForeignKey("programmer.id"), primary_key=True),
)
# ASSOCIATION TABLES ###########################################################



# PEOPLE ###########################################################

class Programmer(Base):
    __tablename__ = "programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    years_of_experience = Column(Integer)
    company_id = Column(Integer, ForeignKey("company.id"))
    projects = relationship("Project", secondary=project_programmer_association_table, back_populates="programmers")
    onsitesupports = relationship("OnSiteSupport", secondary=onsitesupport_programmer_association_table, back_populates="programmers")

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)    

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    companies = relationship("Company", secondary=client_company_association_table, back_populates="clients")
    betatests = relationship("BetaTest", secondary=client_betatest_association_table, back_populates="clients")
    demos = relationship("Demo", secondary=demo_client_association_table, back_populates="clients")


class Salesperson(Base):
    __tablename__ = "salesperson"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    trustworthy = Column(Boolean)
    demos = relationship("Demo", secondary=demo_salesperson_association_table, back_populates="salespeople")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    projects = relationship("Project", secondary=project_user_association_table, back_populates="users")
    betatests = relationship("BetaTest", secondary=betatest_user_association_table, back_populates="users")

# PEOPLE ###########################################################


# EVENTS ###########################################################

class BetaTest(Base):
    __tablename__ = "betatest"
    id = Column(Integer, primary_key=True)
    location = Column(Geometry('POINT'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    users = relationship("User", secondary=betatest_user_association_table, back_populates="betatests")
    clients = relationship("Client", secondary=client_betatest_association_table, back_populates="betatests")
    project_id = Column(Integer, ForeignKey("project.id"))
    company_id = Column(Integer, ForeignKey("company.id"))


class Demo(Base):
    __tablename__ = "demo"
    id = Column(Integer, primary_key=True)
    location = Column(Geometry('POINT'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    salespeople = relationship("Salesperson", secondary=demo_salesperson_association_table, back_populates="demos")
    clients = relationship("Client", secondary=demo_client_association_table, back_populates="demos")
    company_id = Column(Integer, ForeignKey("company.id"))
    project_id = Column(Integer, ForeignKey("project.id"))

class OnSiteSupport(Base):
    __tablename__ = "onsitesupport"
    id = Column(Integer, primary_key=True)
    location = Column(Geometry('POINT'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    fixed_problem = Column(Boolean)
    project_id = Column(Integer, ForeignKey("project.id"))
    company_id = Column(Integer, ForeignKey("company.id"))
    programmers = relationship("Programmer", secondary=onsitesupport_programmer_association_table, back_populates="onsitesupports")

# EVENTS ###########################################################



# OTHER ###########################################################

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ceo = Column(Integer, ForeignKey("person.id"))
    programmers = relationship("Programmer")
    clients = relationship("Client", secondary=client_company_association_table, back_populates="companies")
    projects = relationship("Project")
    betatests = relationship("BetaTest")
    demos = relationship("Demo")
    onsitesupports = relationship("OnSiteSupport")
    description = Column(String)


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    programmers = relationship("Programmer", secondary=project_programmer_association_table, back_populates="projects")
    users = relationship("User", secondary=project_user_association_table, back_populates="projects")
    language = Column(String) # Java, Python, Go, Rust
    in_production = Column(Boolean)
    description = Column(String)
    company_id = Column(Integer, ForeignKey("company.id"))
    betatests = relationship("BetaTest")
    demos = relationship("Demo")
    onesitesupports = relationship("OnSiteSupport")

