from datetime import datetime
from typing import List

from shapely.geometry import Point

from event.event import Event
from people.programmer import Programmer
from project.project import Project


class OnSiteSupport(Event):

    def __init__(self,
                 location: Point,
                 start_time: datetime,
                 end_time: datetime,
                 programmers: List[Programmer],
                 project: Project,
                 fixed_problem: bool) -> None:
        super().__init__(location=location, start_time=start_time, end_time=end_time)
        self.programmers: List[Programmer] = programmers
        self.project: Project = project
        self.fixed_problem: bool = fixed_problem
