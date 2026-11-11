"""Преобразование JSON в CSV и CSV в JSON."""

import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразовать список словарей из JSON в CSV.

    Порядок столбцов определяется порядком ключей в JSON.
    Если у объекта отсутствует какое-то поле, записывается пустая строка.

    ValueError возникает, если расширение неверное, JSON пустой
    или его структура не соответствует списку словарей.
    FileNotFoundError возникает, если входной файл не найден.
    """
    input_path = Path(json_path)
    output_path = Path(csv_path)

    if input_path.suffix.lower() != ".json":
        raise ValueError("Входной файл должен иметь расширение .json")

    if output_path.suffix.lower() != ".csv":
        raise ValueError("Выходной файл должен иметь расширение .csv")

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON должен содержать список словарей")

    # Собираем все ключи, сохраняя порядок их появления.
    fieldnames = []

    for item in data:
        for key in item:
            if not isinstance(key, str):
                raise ValueError("Ключи объектов JSON должны быть строками")

            if key not in fieldnames:
                fieldnames.append(key)

    # Создаём родительскую папку, если её ещё нет.
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразовать CSV в JSON — список словарей.

    Первая строка CSV должна содержать названия столбцов.
    Значения полей сохраняются как строки.
    JSON записывается в кодировке UTF-8 с отступами.

    ValueError возникает, если расширение неверное,
    CSV пустой или заголовок некорректен.
    FileNotFoundError возникает, если входной файл не найден.
    """
    input_path = Path(csv_path)
    output_path = Path(json_path)

    if input_path.suffix.lower() != ".csv":
        raise ValueError("Входной файл должен иметь расширение .csv")

    if output_path.suffix.lower() != ".json":
        raise ValueError("Выходной файл должен иметь расширение .json")

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Проверяем наличие заголовка.
        if reader.fieldnames is None or not reader.fieldnames:
            raise ValueError("CSV пустой или не содержит заголовок")

        # Пустые имена столбцов не допускаются.
        if any(
            name is None or name.strip() == ""
            for name in reader.fieldnames
        ):
            raise ValueError("Названия столбцов не должны быть пустыми")

        # Повторяющиеся названия столбцов могут привести
        # к потере данных при создании словарей.
        if len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError("Названия столбцов должны быть уникальными")

        data = list(reader)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# json_to_csv("data/samples/people.json","data/out/people_from_json.csv")
# print("JSON преобразован в CSV")

# csv_to_json("data/samples/people.csv","data/out/people_from_csv.json")
# print("CSV преобразован в JSON")
