from src.dice import DieWithSixFaces, DieWith20Faces
from typing import List, Dict


def throw_all_dice_from_list(dice_list: List[DieWithSixFaces | DieWith20Faces]) -> Dict[type, List[int]]:
    """
        Simulates rolling all dice in the provided list and returns the results categorized by die type.

        This function accepts a list of dice, where each die is either a DieWithSixFaces or DieWith20Faces object.
        It throws each die, collects the results, and returns them in a dictionary, where keys are die types and values
        are lists of results. If the input list is empty or contains dice of incorrect types, appropriate exceptions are raised.

        Parameters:
        dice_list (List[DieWithSixFaces | DieWith20Faces]): A list of dice objects to be rolled.

        Returns:
        Dict[Type[DieWithSixFaces | DieWith20Faces], List[int]]: A dictionary with die types as keys and lists of roll results as values.
    """
    if len(dice_list) == 0:
        raise ValueError("Got empty list of dice")

    results_list = {DieWithSixFaces: [], DieWith20Faces: []}
    for die in dice_list:
        die_type = type(die)
        if die_type is not DieWithSixFaces and die_type is not DieWith20Faces:
            raise TypeError("The type of any die must be either DieWithSixFaces, or DieWith20Faces")
        results_list[die_type].append(die.throw_die())

    print(f'Results of rolls with dice with 6 faces: {', '.join(map(str, results_list[DieWithSixFaces]))}')
    print(f'Results of rolls with dice with 20 faces: {', '.join(map(str, results_list[DieWith20Faces]))}')
    return results_list


def check_for_win(results_list: Dict[type, List[int]]) -> bool:
    """
       Determines whether the player has won based on the results of dice rolls.

       This function checks if the player has won based on two conditions:
       1. At least one pair of the same number was rolled on the 6-sided dice.
       2. A 20 was rolled at least once on the 20-sided dice.

       Parameters:
       results_list (Dict[type, List[int]]): A dictionary where keys are die types (DieWithSixFaces or DieWith20Faces)
                                             and values are lists of roll results for those dice.

       Returns:
       bool: True if both winning conditions are met, False otherwise.
    """
    condition_1 = False
    condition_2 = 20 in results_list[DieWith20Faces]
    while len(results_list[DieWithSixFaces]) > 0 and not condition_1:
        checked_result = results_list[DieWithSixFaces].pop(0)
        condition_1 = checked_result in results_list[DieWithSixFaces]
    return condition_1 and condition_2


def main() -> None:
    """
        Main function to simulate rolling a list of dice and check for a win.

        This function initializes a list of dice, consisting of five 6-sided dice and five 20-sided dice.
        It then calls `throw_all_dice_from_list` to simulate rolling all the dice. After obtaining the results,
        it uses `check_for_win` to determine if the user has won

        Based on the results, it prints whether the user has won or lost.
    """
    dice_list = [DieWithSixFaces()] * 5 + [DieWith20Faces()] * 5

    results = throw_all_dice_from_list(dice_list)
    if check_for_win(results):
        print("User has won")
    else:
        print("User has lost")


if __name__ == "__main__":
    main()
