import random
import Card
import Settings


class Game:
    def __init__(self):
        self.player_cards = []
        self.dealer_cards = []

        self.player_score = 0
        self.dealer_score = 0

    def blackjack_game(self, deck):

        while len(self.player_cards) < 2:

            self.player_card = random.choice(deck)
            self.player_cards.append(self.player_card)
            deck.remove(self.player_card)

            self.player_score += self.player_card.card_value

            if len(self.player_cards) == 2:
                if self.player_cards[0].card_value == 11 and self.player_cards[1].card_value == 11:
                    self.player_cards[0].card_value = 1
                    self.player_score -= 10

            print("Cartes du joueur: ")
            Card.print_cards(self.player_cards, False)
            print("Score du joueur = ", self.player_score)

            input()

            self.dealer_card = random.choice(deck)
            self.dealer_cards.append(self.dealer_card)
            deck.remove(self.dealer_card)

            self.dealer_score += self.dealer_card.card_value

            print("Cartes du croupier: ")
            if len(self.dealer_cards) == 1:
                Card.print_cards(self.dealer_cards, False)
                print("Score du croupier = ", self.dealer_score)
            else:
                Card.print_cards(self.dealer_cards[:-1], True)
                print("Score du croupier = ", self.dealer_score - self.dealer_cards[-1].card_value)

            if len(self.dealer_cards) == 2:
                if self.dealer_cards[0].card_value == 11 and self.dealer_cards[1].card_value == 11:
                    self.dealer_cards[1].card_value = 1
                    self.dealer_score -= 10

            input()

        if self.player_score == 21:
            print("Joueur a un BLACKJACK!!!!")
            print("Le joueur a gagner!!!!")
            quit()

        print("Cartes du croupier: ")
        Card.print_cards(self.dealer_cards[:-1], True)
        print("Score du croupier = ", self.dealer_score - self.dealer_cards[-1].card_value)

        print()

        print("Cartes du joueur: ")
        Card.print_cards(self.player_cards, False)
        print("Score du joueur = ", self.player_score)

        while self.player_score < 21:
            choice = input("Entrer 1 pour Hit ou 2 pour Stand : ")

            if len(choice) != 1 or (choice != '1' and choice != '2'):
                print("Mauvais choix !!!")

            if choice == '1':

                self.player_card = random.choice(deck)
                self.player_cards.append(self.player_card)
                deck.remove(self.player_card)

                self.player_score += self.player_card.card_value

                c = 0
                while self.player_score > 21 and c < len(self.player_cards):
                    if self.player_cards[c].card_value == 11:
                        self.player_cards[c].card_value = 1
                        self.player_score -= 10
                        c += 1
                    else:
                        c += 1

                print("Cartes du croupier: ")
                Card.print_cards(self.dealer_cards[:-1], True)
                print("Score du croupier = ", self.dealer_score - self.dealer_cards[-1].card_value)

                print()

                print("Cartes du joueur: ")
                Card.print_cards(self.player_cards, False)
                print("Score du joueur = ", self.player_score)

            if choice == '2':

                break

        print("Cartes du joueur: ")
        Card.print_cards(self.player_cards, False)
        print("Score du joueur = ", self.player_score)

        print()
        print("LE CROUPIER RÉVÈLE LES CARTES....")

        print("Cartes du croupier: ")
        Card.print_cards(self.dealer_cards, False)
        print("Score du croupier = ", self.dealer_score)

        if self.player_score == 21:
            print("Le joueur a un BLACKJACK")
            quit()

        if self.player_score > 21:
            print("Le joueur a bruler!!! GAME OVER!!!")
            quit()

        input()

        while self.dealer_score < 17:

            print("Le croupier a decider de HIT.....")

            self.dealer_card = random.choice(deck)
            self.dealer_cards.append(self.dealer_card)
            deck.remove(self.dealer_card)

            self.dealer_score += self.dealer_card.card_value

            c = 0
            while self.dealer_score > 21 and c < len(self.dealer_cards):
                if self.dealer_cards[c].card_value == 11:
                    self.dealer_cards[c].card_value = 1
                    self.dealer_score -= 10
                    c += 1
                else:
                    c += 1

            print("Cartes du joueur: ")
            Card.print_cards(self.player_cards, False)
            print("Score du Joueur = ", self.player_score)

            print()

            print("Cartes du croupier: ")
            Card.print_cards(self.dealer_cards, False)
            print("Score du croupier = ", self.dealer_score)

            input()

        if self.dealer_score > 21:
            print("Le croupier a bruler!!! Tu a gagner!!!")
            quit()

        if self.dealer_score == 21:
            print("Le croupier a BLACKJACK!!! Le joueur perd")
            quit()

        if self.dealer_score == self.player_score:
            print("Égalité!!!!")

        elif self.player_score > self.dealer_score:
            print("Le joueur a gagner!!!")

        else:
            print("le Croupier a gagner!!!")


game = Game()
game.blackjack_game(Settings.get_deck())
