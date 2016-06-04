from Player.Player import Player

def setup():
    playerList = getPlayers()
    chooseCivs(playerList)
    tradeDecks(playerList)
    return playerList

def getPlayers(): #Gets player number and creates player objects
    numPlayers = input('How many players?')

    playerList = []
    for player in range(numPlayers):
        playerList.append(Player())
        #TODO Get player names

    return playerList

def chooseCivs(playerList): #Gets civs and starting locations
    civList = [1, 2] #Update based on player counts. For simplicity the starting locations of the civs should be the same as their numbers

    for idx, player in enumerate(playerList):
        player.civ = civList[idx]
        player.units[0] = player.civ

def tradeDecks(playerList): #Sets up trade decks
    pass #TODO base off player counts