from sqlalchemy import Column, ForeignKey, Integer, Table, String, Boolean, DateTime, create_engine
from geoalchemy2 import Geometry
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# ASSOCIATION TABLES ###########################################################
project_programmer_association_table = Table("project_programmer_association",Base.metadata,
    Column("project_id", ForeignKey("project.id"), primary_key=True),
    Column("programmer_id", ForeignKey("programmer.id"), primary_key=True),
)
project_user_association_table = Table("project_user_association",Base.metadata,
    Column("project_id", ForeignKey("project.id"), primary_key=True),
    Column("user_id", ForeignKey("user_p.id"), primary_key=True),
)
client_company_association_table = Table("client_company_association",Base.metadata,
    Column("client_id", ForeignKey("client.id"), primary_key=True),
    Column("company_id", ForeignKey("company.id"), primary_key=True),
)
betatest_user_association_table = Table("betatest_user_association",Base.metadata,
    Column("betatest_id", ForeignKey("betatest.id"), primary_key=True),
    Column("user_id", ForeignKey("user_p.id"), primary_key=True),
)
demo_salesperson_association_table = Table("demo_salesperson_association",Base.metadata,
    Column("demo_id", ForeignKey("demo.id"), primary_key=True),
    Column("salesperson_id", ForeignKey("salesperson.id"), primary_key=True),
)
demo_client_association_table = Table("demo_client_association",Base.metadata,
    Column("demo_id", ForeignKey("demo.id"), primary_key=True),
    Column("client_id", ForeignKey("client.id"), primary_key=True),
)
onsitesupport_programmer_association_table = Table("onsitesupport_programmer_association",Base.metadata,
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
    projects = relationship("Project", secondary=project_programmer_association_table, back_populates="programmers", cascade="all, delete")
    onsitesupports = relationship("OnSiteSupport", secondary=onsitesupport_programmer_association_table, back_populates="programmers", cascade="all, delete")

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
    companies = relationship("Company", secondary=client_company_association_table, back_populates="clients", cascade="all, delete")
    demos = relationship("Demo", secondary=demo_client_association_table, back_populates="clients", cascade="all, delete")

class Salesperson(Base):
    __tablename__ = "salesperson"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    trustworthy = Column(Boolean)
    demos = relationship("Demo", secondary=demo_salesperson_association_table, back_populates="salespeople", cascade="all, delete")

class User_p(Base):
    __tablename__ = "user_p"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    projects = relationship("Project", secondary=project_user_association_table, back_populates="users", cascade="all, delete")
    betatests = relationship("BetaTest", secondary=betatest_user_association_table, back_populates="users", cascade="all, delete")

# PEOPLE ###########################################################


# EVENTS ###########################################################

class BetaTest(Base):
    __tablename__ = "betatest"
    id = Column(Integer, primary_key=True)
    location = Column(Geometry(geometry_type='POINT'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    users = relationship("User_p", secondary=betatest_user_association_table, back_populates="betatests", cascade="all, delete")
    project_id = Column(Integer, ForeignKey("project.id"))
    company_id = Column(Integer, ForeignKey("company.id"))


class Demo(Base):
    __tablename__ = "demo"
    id = Column(Integer, primary_key=True)
    location = Column(Geometry(geometry_type='POINT'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    salespeople = relationship("Salesperson", secondary=demo_salesperson_association_table, back_populates="demos", cascade="all, delete")
    clients = relationship("Client", secondary=demo_client_association_table, back_populates="demos", cascade="all, delete")
    company_id = Column(Integer, ForeignKey("company.id"))
    project_id = Column(Integer, ForeignKey("project.id"))

class OnSiteSupport(Base):
    __tablename__ = "onsitesupport"
    id = Column(Integer, primary_key=True)
    location = Column(Geometry(geometry_type='POINT'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    fixed_problem = Column(Boolean)
    project_id = Column(Integer, ForeignKey("project.id"))
    company_id = Column(Integer, ForeignKey("company.id"))
    programmers = relationship("Programmer", secondary=onsitesupport_programmer_association_table, back_populates="onsitesupports", cascade="all, delete")

# EVENTS ###########################################################



# OTHER ###########################################################

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ceo = Column(Integer, ForeignKey("person.id"))
    programmers = relationship("Programmer")
    clients = relationship("Client", secondary=client_company_association_table, back_populates="companies", cascade="all, delete")
    projects = relationship("Project", cascade="all, delete")
    betatests = relationship("BetaTest", cascade="all, delete")
    demos = relationship("Demo", cascade="all, delete")
    onsitesupports = relationship("OnSiteSupport", cascade="all, delete")
    description = Column(String)


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    programmers = relationship("Programmer", secondary=project_programmer_association_table, back_populates="projects", cascade="all, delete")
    users = relationship("User_p", secondary=project_user_association_table, back_populates="projects", cascade="all, delete")
    language = Column(String) # Java, Python, Go, Rust
    in_production = Column(Boolean)
    description = Column(String)
    company_id = Column(Integer, ForeignKey("company.id"))
    betatests = relationship("BetaTest", cascade="all, delete")
    demos = relationship("Demo", cascade="all, delete")
    onesitesupports = relationship("OnSiteSupport", cascade="all, delete")

# OTHER ###########################################################


