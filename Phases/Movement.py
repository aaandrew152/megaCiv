from Phases.CheckSupport import checkSupport
from Board import board

def movement(playerList): #Move player by player, resolve combat, cities, support limits
    move(playerList)

    combat(playerList)

    checkSupport(playerList)

def move(playerList):
    censusList = []
    for player in playerList:
        censusList.append(player.census())

    for playerMove in range(len(playerList)):
        currentPlayer = censusList.index(playerMove)
        playerList[currentPlayer].move(board)

def combat(playerList):
    for area, popCap in enumerate(board.areas):
        count = 0
        cityPresent = False
        for idx, player in enumerate(playerList):
            units = player.numUnits(area)
            present = []
            if units > 0:
                count += units
                present.append((idx, units))

            if player.cityPresent(area):
                cityPresent = True

        if count > popCap and not cityPresent:
            pass #TODO unit combat, check for multiple players
        if count > 0 and cityPresent:
            pass #
    #City
