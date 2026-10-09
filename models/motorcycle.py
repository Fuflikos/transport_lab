"""Мотоцикл."""

from models.engine import Engine
from models.owner import Owner
from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    """Мотоцикл: тип (спорт, круизер и т.п.)."""

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        price: float,
        plate: str,
        engine: Engine,
        moto_type: str,
        owner: Owner | None = None,
    ) -> None:
        super().__init__(brand, model, year, price, plate, engine, owner)
        self.moto_type: str = moto_type

    def get_info(self) -> str:
        return (
            f"Мотоцикл: {self.brand} {self.model} ({self.year}), "
            f"тип {self.moto_type}, двигатель {self.engine}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["moto_type"] = self.moto_type
        return data
