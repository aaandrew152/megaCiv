advanceRequirements = \
    [(0, 0, 0)] * 3 + [(3, 0, 0)] * 3 #Don't remember rest will need to find
#Format is (cities, total tech, early tech)

def ast(playerList):
    pass # TODO fill in

def checkGameEnd(playerList): #True if end is next turn
    for player in playerList:
        if player.ast == 18: #Check number
            return True
    return False