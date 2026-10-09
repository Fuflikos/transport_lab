"""Базовый абстрактный класс транспортного средства."""

from abc import ABC, abstractmethod

from exceptions import InvalidVehicleDataError
from models.engine import Engine
from models.owner import Owner


class Vehicle(ABC):
    """Абстрактное транспортное средство."""

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        price: float,
        plate: str,
        engine: Engine,
        owner: Owner | None = None,
    ) -> None:
        if not brand or not model:
            raise InvalidVehicleDataError("Марка и модель обязательны")
        if not (1900 <= year <= 2100):
            raise InvalidVehicleDataError(f"Некорректный год выпуска: {year}")
        if price < 0:
            raise InvalidVehicleDataError("Цена не может быть отрицательной")
        if not plate:
            raise InvalidVehicleDataError("Госномер обязателен")

        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.price: float = price
        self.plate: str = plate
        self.engine: Engine = engine
        self.owner: Owner | None = owner

    @abstractmethod
    def get_info(self) -> str:
        """Краткая информация о ТС. Реализуется в наследниках."""
        ...

    def to_dict(self) -> dict:
        """Сериализация в словарь."""
        return {
            "type": self.__class__.__name__,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "plate": self.plate,
            "engine": self.engine.to_dict(),
            "owner": self.owner.to_dict() if self.owner else None,
        }

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year}), {self.plate}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.brand!r}, {self.model!r}, {self.plate!r})"
