"""Скрипт подсчёта частот слов в текстовом файле."""

import argparse
import sys
from collections import Counter
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(SRC_DIR))

# Добавляем корень проекта в путь импорта, чтобы работали оба способа запуска:
# python src/lab04/text_report.py и python -m src.lab04.text_report

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from lab04.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize


def frequencies_from_text(text: str) -> Counter[str]:
    """Нормализовать текст, разбить на токены и посчитать частоты."""
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Отсортировать слова по частоте по убыванию, затем по алфавиту."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main() -> None:
    """Прочитать входной файл, сохранить CSV и вывести краткую статистику."""
    parser = argparse.ArgumentParser(
        description="Подсчёт частот слов в текстовом файле."
    )
    parser.add_argument(
        "--in", dest="input_path", default="data/input.txt",
        help="путь к входному текстовому файлу (по умолчанию data/input.txt)",
    )
    parser.add_argument(
        "--out", dest="output_path", default="data/report.csv",
        help="путь к CSV-отчёту (по умолчанию data/report.csv)",
    )
    parser.add_argument(
        "--encoding", default="utf-8",
        help="кодировка входного файла (по умолчанию utf-8; например cp1251)",
    )
    args = parser.parse_args()

    try:
        text = read_text(args.input_path, encoding=args.encoding)
    except (FileNotFoundError, UnicodeDecodeError) as error:
        parser.error(str(error))

    freq = frequencies_from_text(text)
    sorted_counts = sorted_word_counts(freq)

    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(sorted_counts, output_path, header=("word", "count"))

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in sorted_counts[:5]:
        print(f"  {word}: {count}")

if __name__ == "__main__":
    main()
