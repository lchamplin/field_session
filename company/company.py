from typing import List

from event.event import Event
from people.person import Person
from people.client import Client
from people.programmer import Programmer
from project.project import Project


class Company():

    def __init__(self,
                 name: str,
                 ceo: Person,
                 programmers: List[Programmer],
                 clients: List[Client],
                 projects: List[Project],
                 events: List[Event],
                 description: str) -> None:
        self.name = name
        self.ceo = ceo
        self.programmers = programmers
        self.clients = clients
        self.projects = projects
        self.events = events
        self.description = description
