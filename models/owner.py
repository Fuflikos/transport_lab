"""Класс владельца транспортного средства."""

from exceptions import InvalidVehicleDataError


class Owner:
    """Владелец: ФИО и телефон."""

    def __init__(self, full_name: str, phone: str) -> None:
        if not full_name:
            raise InvalidVehicleDataError("ФИО владельца обязательно")
        if not phone:
            raise InvalidVehicleDataError("Телефон владельца обязателен")

        self.full_name: str = full_name
        self.phone: str = phone

    def to_dict(self) -> dict:
        return {"full_name": self.full_name, "phone": self.phone}

    @classmethod
    def from_dict(cls, data: dict) -> "Owner":
        return cls(full_name=data["full_name"], phone=data["phone"])

    def __str__(self) -> str:
        return f"{self.full_name} ({self.phone})"

    def __repr__(self) -> str:
        return f"Owner({self.full_name!r}, {self.phone!r})"
