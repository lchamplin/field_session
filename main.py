from company.company import Company
from event.event import Event
from event.demo import Demo
from event.beta_test import BetaTest
from event.on_site_support import OnSiteSupport
from people.person import Person
from people.client import Client
from people.programmer import Programmer
from people.salesperson import Salesperson
from people.user import User
from project.project import Project

from shapely.geometry import Point
from datetime import datetime



def main():
        company = Company(name="ICR", ceo="Rob", programmers=[], clients=[], projects=[], events=[], description="the best")
        print(company)
        return 0



main()