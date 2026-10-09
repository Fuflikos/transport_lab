
"""Класс двигателя транспортного средства."""

from exceptions import InvalidVehicleDataError


class Engine:
    """Двигатель: тип, объём, мощность."""

    def __init__(self, engine_type: str, volume: float, power: int) -> None:
        if not engine_type:
            raise InvalidVehicleDataError("Тип двигателя не может быть пустым")
        if volume <= 0:
            raise InvalidVehicleDataError("Объём двигателя должен быть больше 0")
        if power <= 0:
            raise InvalidVehicleDataError("Мощность двигателя должна быть больше 0")

        self.engine_type: str = engine_type
        self.volume: float = volume
        self.power: int = power

    def to_dict(self) -> dict:
        """Сериализация в словарь."""
        return {
            "engine_type": self.engine_type,
            "volume": self.volume,
            "power": self.power,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Engine":
        """Десериализация из словаря."""
        return cls(
            engine_type=data["engine_type"],
            volume=float(data["volume"]),
            power=int(data["power"]),
        )

    def __str__(self) -> str:
        return f"{self.engine_type} {self.volume}L, {self.power} л.с."

    def __repr__(self) -> str:
        return f"Engine({self.engine_type!r}, {self.volume}, {self.power})"
