"""Фабрика для создания объектов Vehicle из словаря."""

from exceptions import InvalidVehicleDataError
from models.bus import Bus
from models.car import Car
from models.engine import Engine
from models.motorcycle import Motorcycle
from models.owner import Owner
from models.truck import Truck
from models.vehicle import Vehicle


class VehicleFactory:
    """Создаёт нужный подкласс Vehicle по полю 'type'."""

    _registry: dict[str, type[Vehicle]] = {
        "Car": Car,
        "Truck": Truck,
        "Bus": Bus,
        "Motorcycle": Motorcycle,
    }

    @classmethod
    def from_dict(cls, data: dict) -> Vehicle:
        """Создать объект Vehicle из словаря."""
        vehicle_type = data.get("type")
        if vehicle_type not in cls._registry:
            raise InvalidVehicleDataError(f"Неизвестный тип ТС: {vehicle_type}")

        engine = Engine.from_dict(data["engine"])
        owner = Owner.from_dict(data["owner"]) if data.get("owner") else None

        common = {
            "brand": data["brand"],
            "model": data["model"],
            "year": int(data["year"]),
            "price": float(data["price"]),
            "plate": data["plate"],
            "engine": engine,
            "owner": owner,
        }

        if vehicle_type == "Car":
            return Car(
                **common,
                doors=int(data["doors"]),
                body_type=data["body_type"],
            )
        if vehicle_type == "Truck":
            return Truck(**common, capacity_tons=float(data["capacity_tons"]))
        if vehicle_type == "Bus":
            return Bus(**common, seats=int(data["seats"]))
        if vehicle_type == "Motorcycle":
            return Motorcycle(**common, moto_type=data["moto_type"])

        raise InvalidVehicleDataError(f"Неизвестный тип ТС: {vehicle_type}")
