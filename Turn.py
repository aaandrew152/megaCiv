from Phases.Update import update
from Phases.Movement import movement
from Phases.Trade import trade
from Phases.Calamities import calamities
from Phases.SpecialAbilities import specialAbilities
from Phases.Technology import technology
from Phases.Ast import ast

def takeTurn(): #Go through the phases in a turn
    update()

    movement()

    trade()

    calamities()

    specialAbilities()

    technology()

    ast()

