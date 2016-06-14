def update(playerList): # Taxation and repopulation
    taxation(playerList)

    populate(playerList)

def taxation(playerList):
    for player in playerList:
        numRevolts = player.gainGold(player.numCities())

        if numRevolts:
            pass #TODO add in tax revolts

def populate(playerList):
    for player in playerList:
        for space in boardSpaces:
            pass #TODO determine how board works