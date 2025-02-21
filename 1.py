# black_jack.py

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                value += 11
                aces += 1
            else:
                value += int(card.rank)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None
def play_game():
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Initialize player's and dealer's hands
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal two cards each
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print("Player's hand:", player_hand)
    print("Dealer's first card:", dealer_hand.cards[0])

    # Player's turn
    while True:
        if player_hand.get_value() < 21:
            decision = input("Do you want another card? (y/n): ")
            if decision.lower() == 'y':
                player_hand.add_card(deck.deal_card())
                print("Player's hand:", player_hand)
            else:
                break
        else:
            break

    # Dealer's turn: dealer hits until hand value is at least 17
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())

    print("Dealer's hand:", dealer_hand)
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    print("Player's value:", player_value)
    print("Dealer's value:", dealer_value)

    # Determine the outcome
    if player_value > 21:
        print("Bust! You lose.")
    elif dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("You lose.")
    else:
        print("Push (Tie).")

if __name__ == '__main__':
    play_game()
