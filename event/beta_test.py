from datetime import datetime
from typing import List

from shapely.geometry import Point

from event.event import Event
from people.user import User
from people.client import Client
from project.project import Project


class BetaTest(Event):

    def __init__(self,
                 location: Point,
                 start_time: datetime,
                 end_time: datetime,
                 users: List[User],
                 clients: List[Client],
                 project: Project) -> None:
        super().__init__(location=location, start_time=start_time, end_time=end_time)
        self.users: List[User] = users
        self.clients: List[Client] = clients
        self.project: Project = project