"""Точка входа: интерактивное меню управления автопарком."""

import os
from typing import Any

from exceptions import VehicleError, VehicleNotFoundError
from fleet import Fleet
from models.bus import Bus
from models.car import Car
from models.engine import Engine
from models.motorcycle import Motorcycle
from models.owner import Owner
from models.truck import Truck
from repository import VehicleRepository

DB_JSON = "data/database.json"
DB_XML = "data/database.xml"


def input_int(prompt: str) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_float(prompt: str) -> float:
    """Безопасный ввод дробного числа."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Ошибка: введите число.")


def create_vehicle_from_input() -> Any:
    """Диалог создания нового ТС."""
    print("\nВыберите тип ТС:")
    print("1. Легковой (Car)")
    print("2. Грузовой (Truck)")
    print("3. Автобус (Bus)")
    print("4. Мотоцикл (Motorcycle)")
    choice = input("Ваш выбор: ")

    brand = input("Марка: ")
    model = input("Модель: ")
    year = input_int("Год выпуска: ")
    price = input_float("Цена: ")
    plate = input("Госномер: ")

    print("--- Двигатель ---")
    engine_type = input("Тип двигателя (Бензин/Дизель/Электро): ")
    volume = input_float("Объём двигателя: ")
    power = input_int("Мощность (л.с.): ")
    engine = Engine(engine_type, volume, power)

    print("--- Владелец (оставьте пустым, если нет) ---")
    owner_name = input("ФИО владельца: ")
    owner = None
    if owner_name:
        owner_phone = input("Телефон: ")
        owner = Owner(owner_name, owner_phone)

    if choice == "1":
        doors = input_int("Количество дверей: ")
        body_type = input("Тип кузова: ")
        return Car(brand, model, year, price, plate, engine, doors, body_type, owner)
    elif choice == "2":
        capacity = input_float("Грузоподъёмность (т): ")
        return Truck(brand, model, year, price, plate, engine, capacity, owner)
    elif choice == "3":
        seats = input_int("Количество мест: ")
        return Bus(brand, model, year, price, plate, engine, seats, owner)
    elif choice == "4":
        moto_type = input("Тип мотоцикла (Спорт/Круизер): ")
        return Motorcycle(brand, model, year, price, plate, engine, moto_type, owner)
    else:
        raise ValueError("Неверный тип ТС")


def main() -> None:
    # 1. Инициализация: загрузка или создание базы
    fleet = Fleet()
    if os.path.exists(DB_JSON):
        try:
            fleet = VehicleRepository.load_json(DB_JSON)
            print(f"База данных загружена: {len(fleet)} ТС")
        except VehicleError as e:
            print(f"Не удалось загрузить базу: {e}. Начинаем с пустой.")
    else:
        print("Файл базы данных не найден. Создан пустой автопарк.")

    # 2. Главный цикл меню
    while True:
        print("\n" + "=" * 40)
        print("         МЕНЕДЖЕР АВТОПАРКА")
        print("=" * 40)
        print("1. Показать все ТС")
        print("2. Найти ТС по госномеру")
        print("3. Добавить новое ТС")
        print("4. Обновить цену ТС")
        print("5. Удалить ТС")
        print("6. Сохранить в JSON и XML")
        print("0. Выход")
        print("=" * 40)

        choice = input("Выберите пункт меню: ").strip()

        try:
            if choice == "1":
                if len(fleet) == 0:
                    print("Автопарк пуст.")
                else:
                    print(f"\nВсего ТС: {len(fleet)}")
                    for v in fleet.all():
                        print(f" - {v.get_info()}")

            elif choice == "2":
                plate = input("Введите госномер: ").strip()
                v = fleet.get_by_plate(plate)
                print(f"Найдено: {v.get_info()}")
                if v.owner:
                    print(f"Владелец: {v.owner}")

            elif choice == "3":
                new_v = create_vehicle_from_input()
                fleet.add(new_v)
                print("ТС успешно добавлено!")

            elif choice == "4":
                plate = input("Введите госномер для обновления: ").strip()
                v = fleet.get_by_plate(plate)  # выбросит исключение, если нет
                new_price = input_float("Введите новую цену: ")
                fleet.update(plate, price=new_price)
                print(f"Цена обновлена. Новая стоимость: {v.price}")

            elif choice == "5":
                plate = input("Введите госномер для удаления: ").strip()
                fleet.delete(plate)
                print("ТС успешно удалено.")

            elif choice == "6":
                VehicleRepository.save_json(fleet, DB_JSON)
                VehicleRepository.save_xml(fleet, DB_XML)
                print(f"Сохранено в {DB_JSON} и {DB_XML}")

            elif choice == "0":
                print("Сохранение перед выходом...")
                VehicleRepository.save_json(fleet, DB_JSON)
                VehicleRepository.save_xml(fleet, DB_XML)
                print("До свидания!")
                break

            else:
                print("Неверный пункт меню. Попробуйте снова.")

        except VehicleNotFoundError as e:
            print(f"ОШИБКА: {e}")
        except VehicleError as e:
            print(f"ОШИБКА ПРЕДМЕТНОЙ ОБЛАСТИ: {e}")
        except ValueError as e:
            print(f"ОШИБКА ВВОДА: {e}")
        except Exception as e:
            print(f"НЕПРЕДВИДЕННАЯ ОШИБКА: {e}")


if __name__ == "__main__":
    main()
