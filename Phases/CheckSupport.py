from Board import board

def checkSupport(playerList):
    surplusPopulation(playerList)

    citySupport(playerList)

def surplusPopulation(playerList): #Goes through each player and each space by player killing units until they are at the limit
    for player in playerList:
        for area, unitLimit in enumerate(board.areas):
            while player.numUnits(area) > unitLimit: # TODO check for cities!
                player.killUnit(area)


def citySupport(playerList):
    for player in playerList:
        numCities = player.numCities()
        numUnits = player.census()

        while numCities * 2 > numUnits:# TODO add possibility of inability to reduce city (lack of units in stock)
            reducedCitySpace = input("Which city would you like to reduce? (Enter its space)") #TODO improve choice of city
            player.reduceCity(reducedCitySpace)

            numUnits = player.census()
            numCities -= player.numCities()
            #TODO Reduce cities beginning with the recently built ones