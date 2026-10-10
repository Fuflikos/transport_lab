"""Демонстрация работы с автопарком: ООП, исключения, JSON, XML."""

from exceptions import VehicleError, VehicleNotFoundError
from fleet import Fleet
from models.bus import Bus
from models.car import Car
from models.engine import Engine
from models.motorcycle import Motorcycle
from models.owner import Owner
from models.truck import Truck
from repository import VehicleRepository


def build_demo_fleet() -> Fleet:
    """Создать демонстрационный автопарк."""
    fleet = Fleet()

    fleet.add(Car(
        brand="Toyota", model="Camry", year=2020, price=2_500_000,
        plate="A123BC", engine=Engine("Бензин", 2.5, 181),
        doors=4, body_type="Седан",
        owner=Owner("Иванов И.И.", "+7-900-000-00-01"),
    ))
    fleet.add(Truck(
        brand="Volvo", model="FH", year=2018, price=5_800_000,
        plate="B456DE", engine=Engine("Дизель", 12.8, 460),
        capacity_tons=20.0,
    ))
    fleet.add(Bus(
        brand="Mercedes", model="Sprinter", year=2021, price=3_200_000,
        plate="C789FG", engine=Engine("Дизель", 2.1, 143),
        seats=20,
    ))
    fleet.add(Motorcycle(
        brand="Yamaha", model="MT-07", year=2022, price=850_000,
        plate="D012HI", engine=Engine("Бензин", 0.689, 73),
        moto_type="Спорт",
    ))

    return fleet


def main() -> None:
    try:
        fleet = build_demo_fleet()
        print(f"Создан автопарк: {fleet}")
        print("-" * 60)
        for v in fleet.all():
            print(v.get_info())

        # Обновление
        print("\n UPDATE: смена владельца Toyota Camry")
        fleet.update("A123BC", owner=Owner("Петров П.П.", "+7-900-000-00-02"))
        print(fleet.get_by_plate("A123BC").owner)

        # Чтение
        print("\n READ: поиск по марке Volvo")
        for v in fleet.filter_by_brand("Volvo"):
            print(v.get_info())

        # Исключение 
        print("\n Обработка ошибки")
        try:
            fleet.get_by_plate("ZZ999ZZ")
        except VehicleNotFoundError as e:
            print(f"Поймано исключение: {e}")

        # JSON
        VehicleRepository.save_json(fleet, "data/fleet.json")
        fleet_from_json = VehicleRepository.load_json("data/fleet.json")
        print(f"\nЗагружено из JSON: {fleet_from_json}")

        # XML
        VehicleRepository.save_xml(fleet, "data/fleet.xml")
        fleet_from_xml = VehicleRepository.load_xml("data/fleet.xml")
        print(f"Загружено из XML: {fleet_from_xml}")

        # DELETE
        fleet.delete("D012HI")
        print(f"\nПосле удаления: {fleet}")

    except VehicleError as e:
        print(f"Ошибка предметной области: {e}")
    except Exception as e:  # noqa: BLE001
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
