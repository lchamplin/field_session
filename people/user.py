from people.person import Person


class User(Person):

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        super().__init__(first_name=first_name, last_name=last_name)
        self.age: int = age
