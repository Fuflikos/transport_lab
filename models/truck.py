"""Грузовой автомобиль."""

from models.engine import Engine
from models.owner import Owner
from models.vehicle import Vehicle


class Truck(Vehicle):
    """Грузовик: грузоподъёмность в тоннах."""

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        price: float,
        plate: str,
        engine: Engine,
        capacity_tons: float,
        owner: Owner | None = None,
    ) -> None:
        super().__init__(brand, model, year, price, plate, engine, owner)
        self.capacity_tons: float = capacity_tons

    def get_info(self) -> str:
        return (
            f"Грузовой: {self.brand} {self.model} ({self.year}), "
            f"грузоподъёмность {self.capacity_tons} т, двигатель {self.engine}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["capacity_tons"] = self.capacity_tons
        return data
