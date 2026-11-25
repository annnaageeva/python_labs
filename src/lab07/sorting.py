def bubble_sort(nums: list[int]) -> list[int]:
    """
    Сортирует список методом пузырька.

    Возвращает новый отсортированный список.
    Исходный список не изменяется.

    Используется досрочное завершение,
    если за проход не было обменов.
    """
    result = nums[:]
    n = len(result)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result


def insertion_sort(nums: list[int]) -> list[int]:
    """
    Сортирует список методом вставок.

    Возвращает новый отсортированный список.
    Исходный список не изменяется.
    """
    result = list(nums)

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result


def selection_sort(nums: list[int]) -> list[int]:
    """
    Сортирует список методом выбора.

    Возвращает новый отсортированный список.
    Исходный список не изменяется.
    """
    result = list(nums)

    n = len(result)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]

    return result

