import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n


def cat_file(input_path: str, number_lines: bool = False) -> None:
    """Вывести содержимое файла в терминал."""
    path = Path(input_path)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    for index, line in enumerate(lines, start=1):
        if number_lines:
            print(f"{index}: {line}")
        else:
            print(line)


def show_stats(input_path: str, top: int = 5) -> None:
    """Посчитать частоты слов в текстовом файле."""

    path = Path(input_path)
    text = path.read_text(encoding="utf-8")
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    popular_words = top_n(frequencies, top)

    # Выводим общую статистику.
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print(f"Топ-{top}:")

    for word, count in popular_words:
        print(f"{word}:{count}")


def main() -> None:
    """Создать команды cat и stats."""

    parser = argparse.ArgumentParser(description="CLI_утилиты лабораторной №6")

    # Создаём список подкоманд.
    subparsers = parser.add_subparsers(dest="command", required=True)

    # подкоманда cat.
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats.
    stats_parser = subparsers.add_parser("stats", help="Посчитать частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5, help="Количество слов в топе (по умолчанию 5)")

    # Получаем аргументы, введённые пользователем.
    args = parser.parse_args()

    try:
        if args.command == "cat":
            cat_file(args.input, args.n)

        elif args.command == "stats":
            if args.top < 0:
                parser.error("--top не может быть отрицательным")

            show_stats(args.input, args.top)

    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")


if __name__ == "__main__":
    main()
