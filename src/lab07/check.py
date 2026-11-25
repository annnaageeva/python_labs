import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100) -> int:
    """
    Проверяет алгоритм сортировки на случайных списках.

    Сравнивает результат с результатом sorted().
    Также проверяет, что исходный список не изменился.

    Возвращает количество выполненных проверок.
    """
    checks = 0

    for _ in range(trials):
        length = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(length)]
        copy = nums[:]
        result = fn(nums)
        assert result == sorted(nums), (f"Ошибка сортировки: {fn.__name__}, " f"список {nums}, результат {result}")
        checks += 1
        assert nums == copy, (f"Функция {fn.__name__} изменила исходный список")
        checks += 1

    return checks


def check_search() -> int:
    """
    Проверяет линейный и бинарный поиск.

    Сравнивает результаты с поведением list.index().
    Проверяет также случаи, когда элемент отсутствует.
    """
    checks = 0

    test_lists = [
        [],
        [1],
        [1, 2, 3],
        [1, 1, 2, 3],
        [-5, -2, 0, 4, 8],
    ]

    for nums in test_lists:
        for x in range(-7, 11):
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1

            actual = linear_search(nums, x)

            assert actual == expected, (f"Ошибка linear_search: список {nums}, элемент {x}")
            checks += 1

            sorted_nums = sorted(nums)
            binary_result = binary_search(sorted_nums, x)

            if x in sorted_nums:
                assert binary_result != -1
                assert sorted_nums[binary_result] == x
            else:
                assert binary_result == -1

            checks += 1

    return checks


def check_two_sum(trials: int = 100) -> int:
    """
    Сравнивает два алгоритма решения задачи Two Sum.

    Проверяет, что оба алгоритма либо находят пару,
    либо возвращают None.

    Если пара найдена, проверяет сумму элементов.
    """
    checks = 0

    for _ in range(trials):
        length = random.randint(0, 30)
        nums = [random.randint(-20, 20) for _ in range(length)]
        target = random.randint(-30, 30)

        brute_result = two_sum_brute(nums, target)
        fast_result = two_sum_fast(nums, target)

        assert (brute_result is None) == (fast_result is None), (f"Алгоритмы дали разные результаты: {nums}, target={target}")
        checks += 1

        for result in (brute_result, fast_result):
            if result is not None:
                i, j = result

                assert i != j
                assert 0 <= i < len(nums)
                assert 0 <= j < len(nums)
                assert nums[i] + nums[j] == target

                checks += 1

    return checks


def main() -> None:
    """
    Запускает все проверки лабораторной работы.
    """
    random.seed(42)

    checks = 0

    checks += check_sorting(bubble_sort)
    checks += check_sorting(insertion_sort)
    checks += check_sorting(selection_sort)

    checks += check_search()
    checks += check_two_sum()

    print(f"OK: {checks} проверок")


if __name__ == "__main__":
    main()