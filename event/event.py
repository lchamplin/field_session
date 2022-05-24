from datetime import datetime

from shapely.geometry import Point


class Event:

    def __init__(self,
                 location: Point,
                 start_time: datetime,
                 end_time: datetime) -> None:
        self.location: Point = location
        self.start_time = start_time
        self.end_time = end_time
