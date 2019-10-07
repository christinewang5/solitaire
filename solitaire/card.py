import random
import curses

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	
	def __str__(self): 
		return self.rank + self.suit[0].upper()

	def display(self, screen):
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		if self.suit == 'spade' or self.suit== 'club':
			screen.addstr(str(self), curses.color_pair(2))
		else:
			screen.addstr(str(self), curses.color_pair(1))

	def is_opposite_suit(self, card):
		if self.suit == 'club' or self.suit == 'spade':
			return card.suit == 'heart' or card.suit == 'diamond'
		else:
			return card.suit == 'spade' or card.suit == 'club'
	
	def is_smaller(self, card):
		rank_value_map = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
					  '8': 8, '9': 9 , '10': 10, 'J': 11, 'Q': 12, 'K': 13}
		self_value = rank_value_map[self.rank]
		card_value = rank_value_map[card.rank]
		return self_value == card_value - 1

	def can_place_card(self, card): 
		if card.is_smaller(self) and card.is_opposite_suit(self):
			return True
		else:
			return False
		
class Deck:
	def __init__(self):
		deck = []
		ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		suits = ['spade', 'diamond', 'heart', 'club']
		for rank in ranks:
			for suit in suits: 
				deck.append(Card(rank, suit))
		random.shuffle(deck)
		self.deck = deck

	def get_deck(self):
		return list(self.deck)

	def flip_card(self):
		return self.deck.pop()

	def deal_cards(self, num_cards):
		cards = self.deck[:num_cards]
		self.deck = self.deck[num_cards:]
		return cards