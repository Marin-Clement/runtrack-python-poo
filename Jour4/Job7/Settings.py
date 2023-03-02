import Card

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                "K": 10}

def get_deck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(Card.Card(suits_values[suit], card, cards_values[card]))
    return deck