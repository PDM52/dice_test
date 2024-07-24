from src.game import throw_all_dice_from_list, check_for_win
from src.dice import Die, DieWithSixFaces, DieWith20Faces
import pytest


@pytest.fixture
def positive_test_data():
    return [[DieWithSixFaces()] * 5 + [DieWith20Faces()] * 5,
            [DieWithSixFaces()],
            [DieWith20Faces()] * 3]


@pytest.fixture
def negative_test_data():
    return ['a', 9.0, None]


def test_throw_all_dice_from_list_positive(positive_test_data):
    for dice_list in positive_test_data:
        number_of_dice_with_6_faces = 0
        number_of_dice_with_20_faces = 0
        for dice in dice_list:
            if type(dice) is DieWithSixFaces:
                number_of_dice_with_6_faces += 1
            elif type(dice) is DieWith20Faces:
                number_of_dice_with_20_faces += 1

        roll_results = throw_all_dice_from_list(dice_list)
        assert type(roll_results) is dict
        assert len(roll_results[DieWithSixFaces]) == number_of_dice_with_6_faces
        assert len(roll_results[DieWith20Faces]) == number_of_dice_with_20_faces
        for key in roll_results:
            assert key is DieWithSixFaces or key is DieWith20Faces
            for roll_result in roll_results[key]:
                assert type(roll_result) is int
                if key == DieWithSixFaces:
                    assert 0 < roll_result <= 6
                if key == DieWith20Faces:
                    assert 0 < roll_result <= 20


def test_throw_all_dice_from_list_negative_with_empty_array():
    with pytest.raises(ValueError, match="Got empty list of dice"):
        throw_all_dice_from_list([])


def test_throw_all_dice_from_list_negative_with_wrong_dice_type():
    with pytest.raises(TypeError, match="The type of any die must be either DieWithSixFaces, or DieWith20Faces"):
        throw_all_dice_from_list([DieWith20Faces(), Die])


def test_throw_all_dice_from_list_negative_with_wrong_array_type(negative_test_data):
    for test_value in negative_test_data:
        with pytest.raises(TypeError):
            throw_all_dice_from_list(test_value)


def test_check_for_win_positive_with_both_conditions_met():
    roll_results = {
        DieWithSixFaces: [6, 2, 2, 4, 1],
        DieWith20Faces: [1, 7, 2, 20, 2]
    }
    assert check_for_win(roll_results) is True


def test_check_for_win_positive_with_first_condition_met():
    roll_results = {
        DieWithSixFaces: [6, 2, 2, 4, 1],
        DieWith20Faces: [6, 19, 8, 16, 10]
    }
    assert check_for_win(roll_results) is False


def test_check_for_win_positive_with_second_condition_met():
    roll_results = {
        DieWithSixFaces: [1, 2, 3, 4, 5],
        DieWith20Faces: [1, 7, 2, 20, 2]
    }
    assert check_for_win(roll_results) is False


def test_check_for_win_positive_with_no_conditions_met():
    roll_results = {
        DieWithSixFaces: [1, 2, 3, 4, 5],
        DieWith20Faces: [6, 19, 8, 16, 10]
    }
    assert check_for_win(roll_results) is False


def test_check_for_win_negative(negative_test_data):
    for test_value in negative_test_data:
        with pytest.raises(TypeError):
            check_for_win(test_value)
