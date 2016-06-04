from gameStart import setup
from Turn import takeTurn

playerList = setup()

gameOver = False

while not gameOver:
    gameOver = takeTurn(playerList)
    gameOver = True
