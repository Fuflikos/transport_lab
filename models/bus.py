"""Автобус."""

from models.engine import Engine
from models.owner import Owner
from models.vehicle import Vehicle


class Bus(Vehicle):
    """Автобус: число пассажирских мест."""

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        price: float,
        plate: str,
        engine: Engine,
        seats: int,
        owner: Owner | None = None,
    ) -> None:
        super().__init__(brand, model, year, price, plate, engine, owner)
        self.seats: int = seats

    def get_info(self) -> str:
        return (
            f"Автобус: {self.brand} {self.model} ({self.year}), "
            f"{self.seats} мест, двигатель {self.engine}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["seats"] = self.seats
        return data
