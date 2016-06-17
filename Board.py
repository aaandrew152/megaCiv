from settings import spaces

class Board(object):
    def __init__(self, areas):
        self.areas = areas

    @staticmethod
    def numberInArea(area, playerList):
        num = 0
        for player in playerList:
            num += player.numUnits(area)
        return num


board = Board(spaces)

