def ast(playerList):
    advance(playerList)

def advance(playerList):
    pass # TODO fill in

def checkGameEnd(playerList): #True if end is next turn
    for player in playerList:
        if player.ast == 18: #Check number
            return True
    return False