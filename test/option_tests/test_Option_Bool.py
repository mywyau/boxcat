# tests/test_Option.py

import pytest

from boxcat.Option import Option


def test_option_some():
    some = Option(True)
    assert some.is_some()


def test_option_is_none():
    some = Option(None)
    assert some.is_none()


def test_option_map():
    some = Option(True)
    option_True = some.map(lambda t: "True" if t else "False")
    assert option_True.get_or_else("") == "True"


def test_option_flat_map():
    some = Option(True)
    option_true_and_false = some.flat_map(lambda x: Option(False))
    assert option_true_and_false.unsafe_get() is False


def test_option_fold_with_Value():
    some = Option(True)
    assert some.fold(lambda: "", lambda t: "True" if t else "False") == "True"


def test_option_fold_None():
    some = Option(None)
    assert some.fold(
        lambda: "Option = None, Got initial value instead",
        lambda t: "True" if t else "False"
    ) == "Option = None, Got initial value instead"


def test_option_get_or_else():
    some = Option(5)
    assert some.get_or_else(0) == 5


def test_option_none():
    none = Option(None)
    assert not none.is_some()
    assert none.is_none()
    assert none.map(lambda x: x * 2).get_or_else(0) == 0
    assert none.flat_map(lambda x: Option(x * 2)).get_or_else(0) == 0
    assert none.fold(lambda: 0, lambda x: x) == 0
    assert none.get_or_else(5) == 5


if __name__ == "__main__":
    pytest.main()
