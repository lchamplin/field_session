from datetime import datetime
from typing import List

from shapely.geometry import Point

from event.event import Event
from people.salesperson import Salesperson
from people.client import Client
from project.project import Project


class Demo(Event):

    def __init__(self,
                 location: Point,
                 start_time: datetime,
                 end_time: datetime,
                 salespeople: List[Salesperson],
                 clients: List[Client],
                 sold_product: bool,
                 project: Project) -> None:
        super().__init__(location=location, start_time=start_time, end_time=end_time)
        self.salespeople: List[Salesperson] = salespeople
        self.clients: List[Client] = clients
        self.sold_product: bool = sold_product
        self.project: Project = project
