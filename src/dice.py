from random import randint


class Die:
    nbfaces: int

    def __init__(self, nbfaces: int):
        if type(nbfaces) is not int:
            raise TypeError
        if nbfaces <= 0:
            raise ValueError("Number of faces must be grater than 0")
        self.nbfaces = nbfaces

    def throw_die(self) -> int:
        return randint(1, self.nbfaces)


class DieWithSixFaces(Die):

    def __init__(self):
        Die.__init__(self, 6)


class DieWith20Faces(Die):

    def __init__(self):
        Die.__init__(self, 20)
