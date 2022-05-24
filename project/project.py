from enum import Enum
from typing import List

from people.programmer import Programmer
from people.user import User
from people.client import Client


class Language(Enum):
    JAVA = 'Java'
    PYTHON = 'Python'
    GO = 'Go'
    RUST = 'Rust'


class Project:

    def __init__(self,
                 programmers: List[Programmer],
                 users: List[User],
                 clients: List[Client],
                 language: Language,
                 in_production: bool,
                 description: str) -> None:
        self.programmers = programmers
        self.users = users
        self.clients = clients
        self.language = language
        self.in_production = in_production
        self.description = description
