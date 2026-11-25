def linear_search(nums, x) -> int:
    """
    Выполняет линейный поиск элемента x в списке nums.
    Возвращает индекс первого найденного элемента.
    Если элемент не найден, возвращает -1.
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i

    return -1


def binary_search(sorted_nums, x) -> int:
    """
    Выполняет бинарный поиск элемента x
    в отсортированном по возрастанию списке.
    Возвращает индекс найденного элемента.
    Если элемент не найден, возвращает -1.

    Важно: список должен быть отсортирован заранее.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2 
        guess = sorted_nums[mid]
        if guess == x:
            return mid 
        elif guess > x:
            hi = mid - 1
        else: 
            lo = mid + 1
    return -1 


def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """
    Находит индексы двух элементов, сумма которых равна target.
    Использует полный перебор пар элементов.
    Возвращает кортеж из двух индексов.
    Если подходящей пары нет, возвращает None.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None


def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Находит индексы двух элементов, сумма которых равна target.
    Использует словарь для ускорения поиска.
    Возвращает кортеж из двух индексов.
    Если подходящей пары нет, возвращает None.
    """
    seen = {}

    for i in range(len(nums)):
        current = nums[i]
        needed = target - current

        if needed in seen:
            return (seen[needed], i)

        seen[current] = i

    return None

