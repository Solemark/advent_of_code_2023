from functools import reduce


def day1(arr: list[str]) -> int:
    total: int = 0
    numbers: list[tuple[int, int]] = []
    for row in arr:
        string: list[str] = list(row)
        chars: list[str] = [char for char in string if char.isdigit()]
        numbers.append((int(chars[0]) * 10, int(chars[-1])))
    results: list[int] = [(result[0] + result[1]) for result in numbers]
    for res in results:
        total += res
    return reduce(lambda a, b: a + b, [res for res in results])
