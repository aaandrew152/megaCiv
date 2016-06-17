class Board(object):
    def __init__(self):
        self.spaces = [0] * 16

    def number(self, space, playerList):
        num = 0
        for player in playerList:
            num += player.numUnits(space)
        return num

