
"""Собственные исключения предметной области транспортных средств."""


class VehicleError(Exception):
    """Базовое исключение для всех ошибок предметной области."""
    pass


class VehicleNotFoundError(VehicleError):
    """Транспортное средство не найдено в автопарке."""
    pass


class InvalidVehicleDataError(VehicleError):
    """Некорректные данные транспортного средства."""
    pass


class RepositoryError(VehicleError):
    """Ошибка при работе с файлами (JSON/XML)."""
    pass
