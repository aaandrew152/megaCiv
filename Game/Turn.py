from Phases.Update import update
from Phases.Movement import movement
from Phases.Trade import trade
from Phases.Calamities import calamities
from Phases.SpecialAbilities import specialAbilities
from Phases.Technology import technology
from Phases.Ast import ast, checkGameEnd

def takeTurn(playerList): #Go through the phases in a turn
    gameEnd = checkGameEnd(playerList)

    update(playerList)

    movement(playerList)

    trade(playerList)

    calamities(playerList)

    specialAbilities(playerList)

    technology(playerList)

    ast(playerList)

    return gameEnd
