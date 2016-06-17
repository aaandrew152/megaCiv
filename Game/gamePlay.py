from Game.Turn import takeTurn
from Game.gameStart import setup

playerList = setup()

gameOver = False

while not gameOver:
    gameOver = takeTurn(playerList)
    gameOver = True
