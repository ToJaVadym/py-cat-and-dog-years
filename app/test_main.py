import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),

        (16, 20, [1, 1]),

        (27, 28, [2, 2]),

        (28, 29, [3, 2]),

        (32, 34, [4, 3]),
    ]
)
def test_get_human_age_conversion(cat_age: int,
                                  dog_age: int,
                                  expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
