from people.person import Person


class Programmer(Person):

    def __init__(self, first_name: str, last_name: str, years_of_experience: int) -> None:
        super().__init__(first_name=first_name, last_name=last_name)
        self.years_of_experience: int = years_of_experience
