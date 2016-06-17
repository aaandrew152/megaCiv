from Board import board

def update(playerList): # Taxation and repopulation
    taxation(playerList)
    populate(playerList)

def taxation(playerList):
    for player in playerList:
        goldGain = 2 * player.numCities()
        numRevolts = player.gainGold(goldGain)

        if numRevolts:
            pass #TODO add in tax revolts

def populate(playerList):
    for player in playerList:
        for space in board.areas:
            stockEmpty = player.repopulate(space)
    #TODO see if speed improvement necessary
    #TODO allow choice of where units repopulate