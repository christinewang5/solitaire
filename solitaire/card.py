import random
# from termcolor import colored

suits = ['spade', 'diamond', 'heart', 'club']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:
	rank_value_map = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
					  '8': 8, '9': 9 , '10': 10, 'J': 11, 'Q': 12, 'K': 13}
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	
	def __str__(self): 
		suit_str = ''
		# CRED = '\033[91m'
		# CEND = '\033[0m'
		if self.suit == 'diamond' or self.suit == 'heart':
			# return CRED + self.rank + self.suit[0].upper() + CEND
			return self.rank + self.suit[0].upper()
		else:
			return self.rank + self.suit[0].upper()

	def is_opposite_suit(self, card):
		if self.suit == 'club' or self.suit == 'spade':
			return card.suit == 'heart' or card.suit == 'diamond'
		else:
			return card.suit == 'spade' or card.suit == 'club'
	
	def is_smaller(self, card):
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
		return self.deck[:num_cards]