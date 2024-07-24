from src.dice import Die, DieWithSixFaces, DieWith20Faces
import pytest


@pytest.fixture
def positive_test_data():
    return [1, 2, 100]


@pytest.fixture
def negative_test_data_with_wrong_values():
    return [0, -1, -100]


@pytest.fixture
def negative_test_data_with_wrong_types():
    return ['a', 1.5, None]


def test_die_constructor_positive(positive_test_data):
    for test_value in positive_test_data:
        dice = Die(test_value)
        assert dice.nbfaces == test_value


def test_die_constructor_negative_with_wrong_values(negative_test_data_with_wrong_values):
    for test_value in negative_test_data_with_wrong_values:
        with pytest.raises(ValueError, match="Number of faces must be grater than 0"):
            Die(test_value)


def test_die_constructor_negative_with_wrong_types(negative_test_data_with_wrong_types):
    for test_value in negative_test_data_with_wrong_types:
        with pytest.raises(TypeError):
            Die(test_value)


def test_die_with_six_faces_constructor_positive():
    dice = DieWithSixFaces()
    assert dice.nbfaces == 6


def test_die_with_20_faces_constructor_positive():
    dice = DieWith20Faces()
    assert dice.nbfaces == 20


def test_throw_die(positive_test_data):
    for test_value in positive_test_data:
        dice = Die(test_value)
        assert 0 < dice.throw_die() <= test_value
