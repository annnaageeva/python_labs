
import random
import timeit
from pathlib import Path
from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (linear_search, binary_search, two_sum_brute, two_sum_fast)
from src.lab07.sorting import (bubble_sort, insertion_sort, selection_sort)


def measure(fn, *args) -> float:
    return timeit.timeit(lambda: fn(*args), number=1)


def format_seconds(seconds) -> str:
    """
    Форматирует время выполнения до 6 знаков после запятой.
    """
    if seconds is None:
        return "> 60"

    return f"{seconds:.6f}"


def print_table(headers: list[str], rows: list[list]) -> None:
    """
    Выводит данные в виде таблицы в терминале.
    """
    widths = []

    for i in range(len(headers)):
        column = [str(row[i]) for row in rows]
        width = max(len(headers[i]), max((len(value) for value in column), default=0))
        widths.append(width)

    header_line = " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))
    separator = "-+-".join("-" * width for width in widths)

    print(header_line)
    print(separator)

    for row in rows:
        print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))))


def main() -> None:
    """
    Запускает измерения алгоритмов сортировки и поиска,
    выводит результаты в таблицах и сохраняет их в CSV.
    """

    random.seed(42)
    rows_csv = []

    print("\nСРАВНЕНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
    print("=" * 75)

    sorting_functions = [("sorted", sorted), ("bubble", bubble_sort), ("selection", selection_sort), ("insertion", insertion_sort)]
    sorting_rows = []

    for n in [1000, 10000, 100000]:
        nums = [random.randint(-100000, 100000) for _ in range(n)]
        row = [n]
        for name, fn in sorting_functions:
            if n == 100000 and name != "sorted":
                seconds = None
                display_time = "> 60"
            else:
                seconds = measure(fn, nums)
                display_time = f"{seconds:.6f} с"
            row.append(display_time)
            rows_csv.append(["sort", n, name, format_seconds(seconds)])
        sorting_rows.append(row)

    print_table(["n", "sorted", "bubble", "selection", "insertion"], sorting_rows)

    print("\nСРАВНЕНИЕ АЛГОРИТМОВ ПОИСКА")
    print("=" * 75)

    nums = [random.randint(0, 100000) for _ in range(100000)]
    queries = [random.choice(nums) for _ in range(10000)]

    linear_time = timeit.timeit(lambda: [linear_search(nums, x) for x in queries], number=1)
    sort_time = measure(sorted, nums)

    sorted_nums = sorted(nums)
    binary_time = timeit.timeit(lambda: [binary_search(sorted_nums, x) for x in queries], number=1)

    search_rows = [["linear", format_seconds(linear_time)], ["sort_before_binary", format_seconds(sort_time)], ["binary", format_seconds(binary_time)]]

    print_table(["impl", "seconds"], search_rows)

    rows_csv.extend([["search", 100000, "linear", format_seconds(linear_time)],
                     ["search", 100000, "sort_before_binary", format_seconds(sort_time)],
                     ["search", 100000, "binary", format_seconds(binary_time)]])

    print("\nСРАВНЕНИЕ АЛГОРИТМОВ TWO SUM")
    print("=" * 75)
    two_sum_rows = []
    for n in [1000, 10000]:
        nums = [random.randint(-10000, 10000) for _ in range(n - 2)]
        nums.extend([500000, 500000])
        target = 1000000

        brute_time = measure(two_sum_brute, nums, target)
        fast_time = measure(two_sum_fast, nums, target)

        two_sum_rows.append([n, format_seconds(brute_time), format_seconds(fast_time)])

        rows_csv.append(["two_sum", n, "brute", format_seconds(brute_time)])
        rows_csv.append(["two_sum", n, "fast", format_seconds(fast_time)])

    print_table(["n", "brute", "fast"], two_sum_rows)

    output_path = Path("data/lab07/bench.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    header = ["task", "n", "impl", "seconds"]

    write_csv(rows_csv, output_path, header=header)
    print("\nРезультаты сохранены в:", output_path)


if __name__ == "__main__":
    main()
