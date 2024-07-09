import pytest

from boxcat.Seq import Seq


# Test cases for the seq class
def test_map():
    bools: list[bool] = [True, False, True, False, True, False]

    seq = Seq(bools)
    result = seq.map(lambda boolean: "I hit the truth" if boolean else "I succumb to the false gods")

    assert (result.to_list() ==
            [
                "I hit the truth",
                "I succumb to the false gods",
                "I hit the truth",
                "I succumb to the false gods",
                "I hit the truth",
                "I succumb to the false gods",
            ]
            )


def test_flat_map():
    bools: list[bool] = [True, False, True, False, True, False]
    seq = Seq(bools)
    result = seq.flat_map(lambda x: [False])
    assert result.to_list() == [False, False, False, False, False, False]


def test_fold_left():
    # combine all the boolean values together
    # eventually evaluates to just True when combined
    bools: list[bool] = [True, False, True, False, True, False, True]
    seq: Seq[bool] = Seq(bools)
    result = seq.fold_left(0)(lambda acc, boolean: 10 if boolean else 0)  # True so result == 10
    assert result == 10


# If you want to run tests from the command line using pytest
if __name__ == "__main__":
    pytest.main()
