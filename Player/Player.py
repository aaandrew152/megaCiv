from Board import board

class Player(object):
    def __init__(self):
        self.civ = 0 # Get civ later
        self.units = [0]*55 #If a unit has a positive value it refers to a map location, if negative 1 it is gold, if 0 in stock
        self.tradeHand = []
        self.cities = [0]*9 #Again positive values denote locations of cities
        self.ast = 0 #Starts at position 0

    def numCities(self):
        cityList = [city for city in self.cities if city > 0]
        return len(cityList)

    def numUnits(self, space):
        unitsOnSpace = [unit for unit in self.units if unit == space]
        return len(unitsOnSpace)

    def areaIndexes(self, area=0): #Returns indexes of units in given space, defaults to stock
        return [idx for idx, unit in enumerate(self.units) if unit == area]

    def census(self): #Returns population
        unitsOnBoard = [unit for unit in self.units if unit > 0]
        return len(unitsOnBoard)

    def gainGold(self, number): #Returns number of revolts
        stockIdxs = self.areaIndexes()

        if len(stockIdxs) < number:
            for idx in stockIdxs:
                self.units[idx] = -1

            return number - len(stockIdxs)
        else:
            for stock in range(number):
                self.units[stockIdxs[stock]] = -1

            return 0

    def addUnits(self, space, number):
        stockIdxs = self.areaIndexes()
        if len(stockIdxs) >= number:
            for idx in range(number):
                self.units[stockIdxs[idx]] = space
            return True
        else:
            for stIdx in stockIdxs:
                self.units[stIdx] = space
            return False

    def repopulate(self, space):
        units = self.numUnits(space)

        if units == 1:
            return self.addUnits(space, 1)
        elif units >= 2:
            return self.addUnits(space, 2)

    def move(self, board):
        pass #TODO, don't forget ships

    def killUnit(self, space): #Puts one unit on given space back into stock
        areaIdxes = self.areaIndexes(space)
        self.units[areaIdxes[0]] = 0

    def buildCity(self, space):
        unbuiltCities = [idx for idx, city in enumerate(self.cities) if city == 0] #TODO Check if index returns multiple values
        self.cities[unbuiltCities[0]] = space

    def destroyCity(self, space):
        city = self.cities.index(space)
        self.cities[city] = 0

    def reduceCity(self, space):
        self.destroyCity(space)
        unitCap = board.areas[space]
        self.addUnits(space, unitCap)





