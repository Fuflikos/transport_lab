"""Легковой автомобиль."""

from models.engine import Engine
from models.owner import Owner
from models.vehicle import Vehicle


class Car(Vehicle):
    """Легковой автомобиль: число дверей и тип кузова."""

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        price: float,
        plate: str,
        engine: Engine,
        doors: int,
        body_type: str,
        owner: Owner | None = None,
    ) -> None:
        super().__init__(brand, model, year, price, plate, engine, owner)
        self.doors: int = doors
        self.body_type: str = body_type

    def get_info(self) -> str:
        return (
            f"Легковой: {self.brand} {self.model} ({self.year}), "
            f"{self.doors} дверей, кузов {self.body_type}, "
            f"двигатель {self.engine}"
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"doors": self.doors, "body_type": self.body_type})
        return data
