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

beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
from random import choice
# choice 应用于实例
print(choice(deck))

# 自带了切片功能
print(deck[:3])
print(deck[12::13]) #先取出索引为12，然后每隔13个数取一次

# 迭代
for card in deck:
    print(card)

# 反向迭代
for card in reversed(deck):
    print(card)

# 迭代通常是隐式的,一个集合类型没有实现__contains__方法，
# 那么in运算符就会按顺序执行一次迭代搜索

print(Card('7', 'bearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)