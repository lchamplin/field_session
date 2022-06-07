# Project:      neo4j demo
# Date:         5/25/2022
# Team:         aMALGomation
# Client:       ICR
# Contributors: Graham Stookey
# Description:  This program demonstrated a use case of 
#               Neo4j, utilizing the Python Driver, using a mock dataset

from neo4j import GraphDatabase

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

connectionString_uri = "neo4j://localhost:7687"     # unencrypted local host
username = "neo4j"                              # default
password = "neo"                                # default


driver = GraphDatabase.driver("neo4j://localhost:7687",
    auth=("neo4j", "neo"))


# class Neo4jDemo:
    
#     def __init__(self, uri, user, password):
#         self.driver = GraphDatabase.driver(uri, auth=(user, password))

#     def close(self):
#         self.driver.closer()

    