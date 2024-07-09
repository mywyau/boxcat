from boxcat.Either import Left, Right, Either


def test_flat_map_multiple_eithers():
    def validate_not_negative(x: int) -> Either[str, int]:
        return Right(x + 1) if x >= 0 else Left("Negative value in step 1")

    def validate_doubled_less_than_ten(x: int) -> Either[str, int]:
        return Right(x * 2) if x <= 10 else Left("Value too large in step 2")

    def validate_minus_three_and_even(x: int) -> Either[str, int]:
        return Right(x - 3) if x % 2 == 0 else Left("Value not even in step 3")

    def validate_divide_by_two_and_not_by_zero(x: int) -> Either[str, int]:
        return Right(x // 2) if x != 0 else Left("Division by zero in step 4")

    def add_five(x: int) -> Either[str, int]:
        return Right(x + 5)

    def square_the_value(x: int) -> Either[str, int]:
        return Right(x * x)

    def subtract_seven(x: int) -> Either[str, int]:
        return Right(x - 7)

    def process(x: int) -> Either[str, int]:
        return (
            validate_not_negative(x)
            .flat_map(validate_doubled_less_than_ten)
            .flat_map(validate_minus_three_and_even)
            .flat_map(validate_divide_by_two_and_not_by_zero)
            .flat_map(add_five)
            .flat_map(square_the_value)
            .flat_map(subtract_seven)
        )

    result = process(2)

    assert result.value == 29  # after all the calcs the value should be 29 starting from x = 2


def test_pattern_matching_eithers():
    def validate_not_negative(x: int) -> Either[str, int]:
        return Right(x + 1) if x >= 0 else Left("Negative value in step 1")

    def validate_doubled_less_than_ten(x: int) -> Either[str, int]:
        return Right(x * 2) if x <= 10 else Left("Value too large in step 2")

    def validate_minus_three_and_even(x: int) -> Either[str, int]:
        return Right(x - 3) if x % 2 == 0 else Left("Value not even in step 3")

    def validate_divide_by_two_and_not_by_zero(x: int) -> Either[str, int]:
        return Right(x // 2) if x != 0 else Left("Division by zero in step 4")

    def add_five(x: int) -> Either[str, int]:
        return Right(x + 5)

    def square_the_value(x: int) -> Either[str, int]:
        return Right(x * x)

    def subtract_seven(x: int) -> Either[str, int]:
        return Right(x - 7)

    def process(x: int) -> Either[str, int]:
        return (
            validate_not_negative(x)
            .flat_map(validate_doubled_less_than_ten)
            .flat_map(validate_minus_three_and_even)
            .flat_map(validate_divide_by_two_and_not_by_zero)
            .flat_map(add_five)
            .flat_map(square_the_value)
            .flat_map(subtract_seven)
        )

    result: Either[str, int] = process(2)

    def handle_either(either: Either[str, int]):
        match result:
            case Right(value):
                return value
            case Left(error_message):
                return error_message

    assert handle_either(result) == 29  # after all the calcs the value should be 29 starting from x = 2
