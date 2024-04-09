class Potion: 
    def __init__(self):
        self.name = 
        self.value =

class Monster: 
    def __init__(self):
        self.name = 
        self.value =

class Shield: 
    def __init__(self):
        self.name = 
        self.value =

class Deck: 
    def __init__(self):
        self.cards = []

class Character:
    def __init__(self):
        self.shieldPower = 0
        self.hitPoints = 21
        self.experience = 0

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        match suit:
            case "spade":
                self.type = "monster"
                self.name = monsters[rank]
            case "club":
                self.type = "monster"
                self.name = monsters[rank]
            case "heart":
                self.type = "potion"
                self.name = potions[rank]
            case "diamond":
                self.type = "shield"
                self.name = shields[rank]

class GameState:
    def __init__(self):
        self.deck = Deck()
        self.character = Character()
        self.skipped_on_previous_draw = False

