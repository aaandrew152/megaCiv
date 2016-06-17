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
        unitSpace = [unit for unit in self.units if unit == space]
        return len(unitSpace)

    def stockIndexes(self): #Returns indexes of units in stock
        return [idx for idx, unit in enumerate(self.units) if unit == 0]

    def gainGold(self, number): #Returns number of revolts
        stockIdxs = self.stockIndexes()

        if len(stockIdxs) < number:
            for idx in stockIdxs:
                self.units[idx] = -1

            return number - len(stockIdxs)
        else:
            for stock in range(number):
                self.units[stockIdxs[stock]] = -1

            return 0

    def addUnits(self, space, number):
        stockIdxs = self.stockIndexes()
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








