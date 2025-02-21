

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"  # "of" можна залишити, або замінити на "із" за бажанням

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
    # Створити та перемішати колоду
    deck = Deck()
    deck.shuffle()

    # Ініціалізувати руки гравця та дилера
    player_hand = Hand()
    dealer_hand = Hand()

    # Роздати по дві карти кожному
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print("Карти гравця:", player_hand)
    print("Перша карта дилера:", dealer_hand.cards[0])

    # Хід гравця
    while True:
        if player_hand.get_value() < 21:
            decision = input("Бажаєте ще карту? (y/n): ")
            if decision.lower() == 'y':
                player_hand.add_card(deck.deal_card())
                print("Карти гравця:", player_hand)
            else:
                break
        else:
            break

    # Хід дилера: дилер бере карти, доки значення руки менше 17
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())

    print("Карти дилера:", dealer_hand)
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    print("Значення гравця:", player_value)
    print("Значення дилера:", dealer_value)

    # Визначення результату
    if player_value > 21:
        print("Перебір! Ви програли.")
    elif dealer_value > 21 or player_value > dealer_value:
        print("Ви виграли!")
    elif player_value < dealer_value:
        print("Ви програли.")
    else:
        print("Нічия.")

if __name__ == '__main__':
    play_game()
