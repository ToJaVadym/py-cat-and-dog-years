from app.main import get_human_age


def test_14_cat_or_dog_years_should_convert_into_0_human_age():
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_1_when_cat_and_dog_age_is_greater_than_15_and_lower_than_24():
    assert get_human_age(16, 20) == [1, 1]


def test_should_return_2_when_cat_age_is_greater_than_24_and_lower_than_28():
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_3_when_cat_age_is_greater_or_equal_to_28():
    assert get_human_age(28, 25) == [3, 2]


def test_should_return_2_when_dog_age_is_greater_than_24_and_lower_than_29():
    assert get_human_age(27, 25) == [2, 2]


def test_should_return_3_when_dog_age_is_greater_or_equal_to_29():
    assert get_human_age(30, 29) == [3, 3]
