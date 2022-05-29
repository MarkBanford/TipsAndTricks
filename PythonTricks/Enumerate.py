from enum import Enum, auto


class Suite(Enum):
    DIAMOND = 100
    CLUB = 200
    HEART = 300
    SPADE = 400


class Value(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Card:
    def __init__(self, suite: Suite, value: Value):
        self.suite = suite
        self.value = value

    @property
    def suite(self):
        return self._suite

    @property
    def value(self):
        return self._value

    @suite.setter
    def suite(self, suite: Suite):
        if suite not in Suite:
            raise Exception
        self._suite = suite

    @value.setter
    def value(self, value: Value):
        if value not in Value:
            raise Exception
        self._value = value

    def __repr__(self):
        return f"<Card {self.value} of {self.suite}"


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in Suite for v in Value]

    def __repr__(self):
        output = [f"{c}\n" for c in self.cards]
        return "".join(output)


if __name__ == '__main__':
    card1 = Card(Suite.DIAMOND, Value.TWO)
    deck=Deck()
    print(deck)
