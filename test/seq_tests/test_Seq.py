from functools import reduce
from typing import List

import pytest

from boxcat.Seq import Seq


# Test cases for the seq class
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


# If you want to run tests from the command line using pytest
if __name__ == "__main__":
    pytest.main()
