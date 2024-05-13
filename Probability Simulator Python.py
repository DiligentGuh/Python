import random

mana = 0
currentTurn = 1
cardsDrawn = 0
lifeCount = 20
numcreature = 0

class Card:

    def __init__(self, name, type, manavalue, power): #decide on effect/etb triggers
        self.name = name
        self.type = type
        self.manavalue = manavalue
        self.power = power
    def __str__(self):
        return ", ".join((self.name, self.type, self.manavalue, self.power))

#60 card mono red burn deck 
mountain = Card('mountain', 'land', '0', '')
playWithFire = Card('play with fire', 'sorcery', '1', '')
lightUpTheStage = Card('light up the stage', 'sorcery', '3', '')
lightningBolt = Card('lightning bolt', 'sorcery', '1', '')
wizardsLightning = Card('wizards lightning', 'sorcery', '3', '')
skewerTheCritics = Card('skewer the critics', 'sorcery', '3', '')
lavaSpike = Card('lava spike', 'sorcery', '1', '')
monasterySwiftSpear = Card('monastery swiftspear', 'creature', '1', '1')
ghituLavaRunner = Card('ghitu lavarunner', 'creature', '1', '1')
viashinoPryomancer = Card('viashino pyromancer', 'creature', '3', '2')

#lists 
deck = [] 
hand = []
board = []

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
    deck.append(monasterySwiftSpear)

for i in range(4):
    deck.append(ghituLavaRunner)

for i in range(4):
    deck.append(viashinoPryomancer)

random.shuffle(deck) #shuffle deck

#adding mana function
def manaFunction():
    global mana
    mana += 1

#draw function
def draw():
    hand.append(deck.pop(0))

#draw staring hand
def start():
    for i in range(7):
        hand.append(deck.pop(0))

#upkeep phase
def upkeep():
    draw()
    global currentTurn
    currentTurn += 1

#play land
def land():
    for card in hand:
        if card.type == "land":
            board.append(card)
            hand.remove(card)
            break

#checking for land -> add mana
def check():
    for card in board:
        if card.type == "land":
            manaFunction()

#play creature function

#play spell function

#combat phase
# def combat():
#     for card in board:
#         if card.type == "creature":

#end phase

# for card in deck:
#     print(card)

# print("----------------------")

print("Hand:")

for card in hand:
    print(card)

print("----------------------")

print("Board:")

for card in board:
    print(card)

# print("----------------------")

print(f"mana: {mana}")