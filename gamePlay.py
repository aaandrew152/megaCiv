from gameStart import setup
from Turn import takeTurn

playerList = setup()

gameNotOver = False

while gameNotOver:
    gameNotOver = takeTurn(playerList)
    print(playerList[0].civ)