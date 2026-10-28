"""Преобразование CSV в файл Excel XLSX."""

import csv
from pathlib import Path

from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Преобразовать CSV в XLSX.

    Первая строка CSV используется как заголовок таблицы.
    Название листа Excel — Sheet1.
    Ширина каждого столбца определяется длиной самого длинного значения,
    но составляет не менее 8 символов.

    ValueError возникает, если расширение неверное или CSV пустой.
    FileNotFoundError возникает, если входной файл не найден.
    """
    input_path = Path(csv_path)
    output_path = Path(xlsx_path)

    if input_path.suffix.lower() != ".csv":
        raise ValueError("Входной файл должен иметь расширение .csv")

    if output_path.suffix.lower() != ".xlsx":
        raise ValueError("Выходной файл должен иметь расширение .xlsx")

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows or not rows[0] or all(value.strip() == "" for value in rows[0]):
        raise ValueError("CSV пустой или не содержит заголовок")

    # Создаём новую книгу Excel.
    workbook = Workbook()

    # Получаем первый лист.
    sheet = workbook.active

    # Переносим строки CSV в таблицу Excel.
    for row in rows:
        sheet.append(row)

    # Настраиваем ширину каждого столбца.
    for column in sheet.columns:
        max_length = 0

        # Берём букву столбца, например A или B.
        column_letter = column[0].column_letter

        for cell in column:
            value = cell.value

            if value is not None:
                value_length = len(str(value))

                if value_length > max_length:
                    max_length = value_length

        # Ширина не должна быть меньше 8 символов.
        sheet.column_dimensions[column_letter].width = max(8, max_length + 2)

    # Создаём папку, если её ещё нет.
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Сохраняем книгу Excel.
    workbook.save(output_path)

# csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
# print("CSV преобразован в XLSX")