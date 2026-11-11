import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    """Создать команды для преобразования файлов."""

    parser = argparse.ArgumentParser( description="Конвертер файлов JSON, CSV и XLSX" )

    # Создаём подкоманды.
    subparsers = parser.add_subparsers(dest="command", required=True)

    # JSON -> CSV.
    json_parser = subparsers.add_parser("json2csv", help="Преобразовать JSON в CSV")
    json_parser.add_argument("--in", dest="input", required=True, help="Путь к JSON-файлу")
    json_parser.add_argument("--out", dest="output", required=True, help="Путь для сохранения CSV-файла")

    # CSV -> JSON.
    csv_json_parser = subparsers.add_parser("csv2json", help="Преобразовать CSV в JSON")
    csv_json_parser.add_argument("--in", dest="input", required=True, help="Путь к CSV-файлу")
    csv_json_parser.add_argument("--out", dest="output", required=True, help="Путь для сохранения JSON-файла")

    # CSV -> XLSX.
    xlsx_parser = subparsers.add_parser("csv2xlsx", help="Преобразовать CSV в XLSX")
    xlsx_parser.add_argument("--in", dest="input", required=True, help="Путь к CSV-файлу")
    xlsx_parser.add_argument("--out", dest="output", required=True, help="Путь для сохранения XLSX-файла")

    # Получаем аргументы пользователя.
    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
            print("JSON успешно преобразован в CSV!")

        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
            print("CSV успешно преобразован в JSON!")

        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print("CSV успешно преобразован в XLSX!")

    except (FileNotFoundError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
