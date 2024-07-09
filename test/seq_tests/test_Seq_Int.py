from typing import Any

import pytest

from boxcat.Seq import Seq


def test_fill():
    empty_list = []
    empty_Seq = Seq(empty_list)
    result = empty_Seq.fill(5)("mikey")
    assert result.to_list() == ["mikey", "mikey", "mikey", "mikey", "mikey"]


def test_fill_currying_capabilities():
    empty_list: list[Any] = []
    empty_Seq_1: Seq[Any] = Seq(empty_list)

    fill_three_times_Seq_1 = empty_Seq_1.fill(3)
    result_1 = fill_three_times_Seq_1(1)
    assert result_1.to_list() == [1, 1, 1]

    result_2 = fill_three_times_Seq_1(True, False)
    assert result_2.to_list() == [1, 1, 1, True, False, True, False, True, False]

    result_3 = fill_three_times_Seq_1("Mikey")
    assert result_3.to_list() == [1, 1, 1, True, False, True, False, True, False, 'Mikey', 'Mikey', 'Mikey']

    empty_list_2: list[Any] = []
    empty_Seq_2: Seq[Any] = Seq(empty_list_2)
    result_4 = empty_Seq_2.fill(2)(1, "Mikey", True)
    assert result_4.to_list() == [1, 'Mikey', True, 1, 'Mikey', True]


def test_map():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    seq = Seq(numbers)

    assert seq.map(lambda x: x + 1).to_list() == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def test_flat_map():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    seq = Seq(numbers)

    assert seq.flat_map(lambda x: [x + 1]).to_list() == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def test_fold_left():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    seq = Seq(numbers)

    assert seq.fold_left(0)(lambda x, y: x + y) == 55


def test_filter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    seq = Seq(numbers)

    assert seq.filter(lambda x: x % 2 == 0).to_list() == [2, 4, 6, 8, 10]


# If you want to run tests from the command line using pytest
if __name__ == "__main__":
    pytest.main()
