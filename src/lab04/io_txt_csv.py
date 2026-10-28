
import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл целиком и вернуть его содержимое одной строкой.

    Если файл сохранён в другой кодировке, передайте её в аргументе
    encoding, например encoding="cp1251".
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: list[tuple | list], path: str | Path,
    header: tuple[str, ...] | None = None,) -> None:
    """Создать или перезаписать CSV-файл.

    Если передан header, он записывается первой строкой.
    Все строки данных должны иметь одну длину."""
    p = Path(path)
    rows = list(rows)

    if rows:
        first_len = len(rows[0])
        for row_number, row in enumerate(rows, start=1):
            if len(row) != first_len:
                raise ValueError(
                    f"У строки {row_number} длина {len(row)},"
                    f"а должна быть, как у первой строки {first_len}")
                

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)


def ensure_parent_dir(path: str | Path) -> None:
    """Создать папку для файла, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)







    