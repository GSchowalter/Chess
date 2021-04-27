import space

class Board:

    def __init__(self):
        self.space = dict()
        self.color = dict()

        space_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

        for i in range(71, 7, -1):
            self.space[space_letters[i % 8] + str(i//8)] = space.Space("w") if i % 2 == 0 else space.Space('b')
        


        