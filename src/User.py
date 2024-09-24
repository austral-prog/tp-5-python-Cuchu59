class User:
    def init(self, dni: int, name: str, number_of_checkouts: int = 0, number_of_checkins: int = 0) -> None:
        self.dni: int = dni
        self.name: str = name
        self.number_of_checkouts: int = number_of_checkouts
        self.number_of_checkins: int = number_of_checkins

    # Getters
    def get_dni(self) -> int:
        return self.dni

    def get_name(self) -> str:
        return self.name

    def get_number_of_checkouts(self) -> int:
        return self.number_of_checkouts

    def get_number_of_checkins(self) -> int:
        return self.number_of_checkins

    # Setters
    def increment_checkouts(self) -> None:
        self.number_of_checkouts += 1

    def increment_checkins(self) -> None:
        self.number_of_checkins += 1
