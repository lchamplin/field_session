from people.person import Person


class Salesperson(Person):

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 trustworthy: bool) -> None:
        super().__init__(first_name=first_name, last_name=last_name)
        self.trustworthy: bool = trustworthy
