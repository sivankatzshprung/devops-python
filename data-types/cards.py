import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    print ("Let's create one car 7 diamons:")
    beer_card = Card('7','diamons')
    print(beer_card)
    print ("*" * 10)
    print ("Let's create deck")
    deck = FrenchDeck()
    print ("Cards in deck:")
    print(len(deck))
    print ("*" * 10)
    print("Let's take random card:")
    print ("*" * 10)
    from random import choice
    print(choice(deck))
    for card in deck:
            print(card)
    print ("*" * 10)
    print("Print reversted deck:")
    print ("*" * 10)
    for card in reversed(deck):
            print(card)
    print (Card('Q', 'hearts') in deck)
    print (Card('7', 'beasts') in deck)
    print ("*" * 10)
    print("Let's sorted:")
    print ("*" * 10)
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    for card in sorted(deck, key=spades_high): 
        print(card)