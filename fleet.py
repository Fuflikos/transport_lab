"""Автопарк: хранит ТС и реализует CRUD-операции."""

from exceptions import VehicleNotFoundError
from models.vehicle import Vehicle


class Fleet:
    """Контейнер транспортных средств."""

    def __init__(self) -> None:
        self._vehicles: list[Vehicle] = []


"""Создание."""


    def add(self, vehicle: Vehicle) -> None:
        """Добавить ТС в автопарк."""
        if self._find_by_plate(vehicle.plate) is not None:
            raise ValueError(f"ТС с номером {vehicle.plate} уже существует")
        self._vehicles.append(vehicle)


"""Чтение.""""


    def get_by_plate(self, plate: str) -> Vehicle:
        """Найти ТС по госномеру."""
        vehicle = self._find_by_plate(plate)
        if vehicle is None:
            raise VehicleNotFoundError(f"ТС с номером {plate} не найдено")
        return vehicle

    def _find_by_plate(self, plate: str) -> Vehicle | None:
        """Внутренний поиск без исключения."""
        for v in self._vehicles:
            if v.plate == plate:
                return v
        return None

    def all(self) -> list[Vehicle]:
        """Вернуть список всех ТС."""
        return list(self._vehicles)

    def filter_by_brand(self, brand: str) -> list[Vehicle]:
        """Отфильтровать по марке."""
        return [v for v in self._vehicles if v.brand.lower() == brand.lower()]


"""Обновить."""



    def update(self, plate: str, **kwargs: object) -> Vehicle:
        """Обновить атрибуты ТС по госномеру."""
        vehicle = self.get_by_plate(plate)
        for key, value in kwargs.items():
            if not hasattr(vehicle, key):
                raise AttributeError(f"У ТС нет атрибута {key}")
            setattr(vehicle, key, value)
        return vehicle


"""Удалить."""


    def delete(self, plate: str) -> None:
        """Удалить ТС по госномеру."""
        vehicle = self.get_by_plate(plate)
        self._vehicles.remove(vehicle)


"""Магические методы."""


    def __len__(self) -> int:
        return len(self._vehicles)

    def __iter__(self):
        return iter(self._vehicles)

    def __repr__(self) -> str:
        return f"Fleet({len(self._vehicles)} vehicles)"
