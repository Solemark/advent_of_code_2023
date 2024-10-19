from pytest import fixture
from day1 import day1


@fixture
def data() -> tuple[list[str], int]:
    return [
        "1abc2",  # 12
        "pqr3stu8vwx",  # 38
        "a1b2c3d4e5f",  # 15
        "treb7uchet",  # 77
    ], 142


def test_day1(data: tuple[list[str], int]) -> None:
    inp, exp = data
    assert exp == day1(inp)
