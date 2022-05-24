from sqlalchemy import Column, ForeignKey, Integer, Table, String
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class Programmer(Base):
    __tablename__ = "programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    years_of_experience = Column(Integer)
    company_id = Column(Integer, ForeignKey("company.id"))

