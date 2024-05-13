import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import copy

def rungame():
    mana = 0
    currentTurn = 0
    lifeCount = 20
    cardsDrawn = 0
    numLands = 0
    manaAccumulated = 0
    prowess = 0

    #functions for each sorcery card
    def playwithfire():
        nonlocal lifeCount
        lifeCount -= 2

    def lightupthestage():
        for i in range(2):
            draw()

    def lightningbolt():
        nonlocal lifeCount
        lifeCount -= 3

    def wizardslightning():
        nonlocal lifeCount
        lifeCount -= 3

    def skewerthecritics():
        nonlocal lifeCount
        lifeCount -= 3

    def lavaspike():
        nonlocal lifeCount
        lifeCount -= 3

    mydict = {
        "Summoning Sickness" : True,
    }

    class Card:

        def __init__(self, name, type, subtype, manavalue, power, effect, dict, keyword): 
            self.name = name
            self.type = type
            self.subtype = subtype
            self.manavalue = manavalue
            self.power = power
            self.effect = effect
            self.dict = dict
            self.keyword = keyword
        def __str__(self):
            return ", ".join((self.name, self.type, str(self.subtype), str(self.manavalue), str(self.power), str(self.dict), str(self.keyword)))

    #60 card mono red burn deck 
    mountain = Card('mountain', 'land', None, 0, None, None, None, None)
    playWithFire = Card('play with fire', 'sorcery', None, 1, 0, playwithfire, None, None) 
    lightUpTheStage = Card('light up the stage', 'sorcery', None, 3, 0, lightupthestage, None, None)
    lightningBolt = Card('lightning bolt', 'sorcery', None, 1, 0, lightningbolt, None, None)
    wizardsLightning = Card('wizards lightning', 'sorcery', None, 3, 0, wizardslightning, None, None)
    skewerTheCritics = Card('skewer the critics', 'sorcery', None, 3, 0, skewerthecritics, None, None)
    lavaSpike = Card('lava spike', 'sorcery', None, 1, 0, lavaspike, None, None)
    monasterySwiftSpear = Card('monastery swiftspear', 'creature', None, 1, 1, None, mydict, "Prowess")
    ghituLavaRunner = Card('ghitu lavarunner', 'creature', 'wizard', 1, 1, None, mydict, None)
    viashinoPyromancer = Card('viashino pyromancer', 'creature', 'wizard', 3, 2, None, mydict, None)

    spells = [lavaSpike, lightningBolt, wizardsLightning, playWithFire, lightUpTheStage, skewerTheCritics]
    creatures = [ghituLavaRunner, monasterySwiftSpear, viashinoPyromancer]

    def generatedeck(spells, creatures, mountain, spellratio = 2/4, creatureratio = 1/4, decksize = 60):
        numspell = math.floor(decksize * spellratio)
        numcreatures = math.floor(decksize * creatureratio)
        numlands = decksize - (numspell + numcreatures)

        spells_2 = []
        for card in spells:
            spells_2.append(card, card, card, card)
        
        creatures_2 = []
        for card in creatures:
            creatures_2.append(card, card, card, card)

        for i in range(numspell):
            deck.append(spells_2[i])

        for i in range(numcreatures):
            deck.append(creatures_2[i])

        for i in range(numlands):
            deck.append(mountain)



    #lists 
    deck = [] 
    hand = []
    board = []
    recordsorcery = []
    recordcreature = []
    winningTurn = []

    #add cards to deck
    for i in range(24):
        deck.append(mountain)

    for i in range(4):
        deck.append(playWithFire)

    for i in range(4):
        deck.append(lightUpTheStage)

    for i in range(4):
        deck.append(lightningBolt)

    for i in range(4):
        deck.append(wizardsLightning)

    for i in range(4):
        deck.append(skewerTheCritics)

    for i in range(4):
        deck.append(lavaSpike)

    for i in range(4):
        deck.append(copy.deepcopy(monasterySwiftSpear))

    for i in range(4):
        deck.append(copy.deepcopy(ghituLavaRunner))

    for i in range(4):
        deck.append(copy.deepcopy(viashinoPyromancer))

    random.shuffle(deck) #shuffle deck

    #adding mana function
    def manaFunction():
        nonlocal mana
        mana += 1
        nonlocal manaAccumulated
        manaAccumulated += 1

    #draw function
    def draw():
        hand.append(deck.pop(0))

    #draw starting hand
    def start():
        for i in range(7):
            hand.append(deck.pop(0))
            nonlocal cardsDrawn
            cardsDrawn += 1
        nonlocal lifeCount
        lifeCount = 20

    #upkeep phase
    def upkeep():
        nonlocal prowess
        prowess = 0
        draw()
        nonlocal currentTurn
        currentTurn += 1
        nonlocal cardsDrawn
        cardsDrawn += 1
        for card in board:
            if(card.type == "creature"):
                mydict["Summoning Sickness"] = False

    #play land
    def land():
        for card in hand:
            if card.type == "land":
                nonlocal numLands
                numLands += 1
                board.append(card)
                hand.remove(card)
                break

    #checking for land -> add mana
    def check():
        for card in board:
            if card.type == "land":
                manaFunction()
                
    #play creature function
    def playcreature():
        nonlocal mana
        for i in range(mana, 0, -1):
            for card in hand:
                if card.type == "creature" and mana - card.manavalue >= 0:
                    mana -= card.manavalue
                    board.append(card)
                    recordcreature.append(card)
                    hand.remove(card)
                if card.name == "viashino pyromancer": 
                    nonlocal lifeCount
                    lifeCount -= 2

    #play spell function
    def playspell():
        nonlocal mana
        nonlocal prowess
        for card in board:
            if(card.subtype == "wizard"):
                wizardsLightning.manavalue = 1
        for i in range(mana, 0 , -1):
            for card in hand:
                if card.type == "sorcery" and mana - card.manavalue >= 0:
                    card.effect()
                    prowess += 1
                    mana -= card.manavalue
                    recordsorcery.append(card)
                    hand.remove(card)
                    # print(f"Sorcery: {card.name}")

    #combat phase
    def combat():
        for card in board:
            if(card.type == "creature"):
                if(not mydict["Summoning Sickness"]):
                    for card in board:
                        if card.keyword == "Prowess":
                            nonlocal lifeCount
                            nonlocal prowess
                            lifeCount -= card.power + prowess
                        elif card.type == "creature":
                                lifeCount -= card.power
                                
    #end phase
    def endphase():
        nonlocal mana
        mana = 0

    def printgame():
        print("--------start--------")
        start()
        print("Cards in hand:")
        for card in hand:
            print(card.name)
        while lifeCount > 0:
            print("--------upkeep--------")
            upkeep()
            print("Cards in hand:")
            for card in hand:
                print(card.name)
            for card in board:
                if(card.type == "creature"):
                    print("Creatures on board:")
                    print(f"Summoning Sick: {mydict["Summoning Sickness"]}")
            print("--------play land--------")
            land()
            print("Cards on board:")
            for card in board:
                print(card.name)
            print("--------mana--------")
            check()
            print(f"Mana: {mana}")
            print("--------play creature + sorcery--------")
            if lifeCount <= 12:
                playspell()
                playcreature()
            else:
                playcreature()
                playspell()
            print("Cards on board")
            for card in board:
                print(card.name)
            print("--------combat--------")
            combat()
            for card in board:
                if card.type == "creature":
                    print(card.name)
                    print(f"Summoning Sick: {mydict["Summoning Sickness"]}")
            print("--------end phase--------")
            endphase()
            print(f"Lifecount: {lifeCount}")
            print(f"Current Turn: {currentTurn}")

    def regulargame():
        start()
        while lifeCount > 0:
            upkeep()
            land()
            check()
            if lifeCount <= 12:
                playspell()
                playcreature()
            else:
                playcreature()
                playspell()
            combat()
            endphase()

    # printgame()
    regulargame()
    
    winningTurn.append(currentTurn)

    return (winningTurn, recordsorcery, recordcreature, numLands, cardsDrawn, manaAccumulated)

data = {
    "Winning_Turn": [],
    "Cards_Drawn": [],
    "Number_Lands": [],
    "Mana_Accumulated": [],
    "Recorded_Sorcery": [],
    "Recorded_Creature": [],
    "Number_Games": []
}

# for i in range(1000):
#     results = rungame()
#     data["Number_Lands"].append(results[3])
#     data["Winning_Turn"].append(results[0])
#     data["Number_Games"].append(i)

# def scatter():
#     size = 20
#     x = np.array(data['Number_Games'])
#     y = np.array(data['Winning_Turn'])
#     plt.scatter(x, y, s=size, alpha = 0.1, color = 'blue')

#     y = np.array(data['Number_Lands'])
#     plt.scatter(x, y, s=size, alpha = 0.1, color = 'cyan')

#     listOf_Yticks = np.arange(0, 26, 1)
#     plt.yticks(listOf_Yticks)

#     listOf_Xticks = np.arange(0, 1100, 100)
#     plt.xticks(listOf_Xticks)

#     plt.xlabel("Game Number")
#     plt.ylabel("Winning Turn")
#     plt.show()

# scatter()