class Player(object):
    def __init__(self):
        self.civ = 0 # Get civ later
        self.units = [0]*55 #If a unit has a positive value it refers to a map location, if negative 1 it is gold, if 0 in stock
        self.tradeHand = []
        self.cities = [0]*9 #Again positive values denote locations of cities

    def numCities(self):
        cityList = [city for city in self.cities if city > 0]
        return len(cityList)


