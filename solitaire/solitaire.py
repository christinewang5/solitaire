from card import *
import random

class Solitaire():
	def __init__(self):
		self.deck = Deck()
		self.tableau = Tableau(self.deck.deal_cards(28))
		self.foundation = Foundation()
		self.stock_waste = StockWaste(self.deck.deal_cards(24))
		self.win = False

	def __str__(self):
		"""
		Generates string for current status of table
		"""
		header = "\n# in Stock \tWaste  \t\t Foundation C   H   S   D\n" 
		first_row = "{:10}  \t{:10} \t\t    {:3} {:3} {:3} {:3}\n".format(
			self.stock_waste.get_num_stock(), self.stock_waste.get_waste_card(), 
			self.foundation.get_top_card("club"), self.foundation.get_top_card("heart"), 
			self.foundation.get_top_card("spade"), self.foundation.get_top_card("diamond"))
		return header + first_row + str(self.tableau)
	
	def get_instructions(self):
		""" 
		Provides list of commands
		"""	
		instructions_str = 'Commands: \n' \
		+ 'sw - move card from stock to waste\n'\
		+ 'wf - move card from waste to foundation\n'\
		+ 'wt - move card from waste to tableau\n'\
		+ 'tf <num tableau> - move card from tableau to foundation\n'\
		+ 'tt <num tableau 1> <num tableau 2> - move card from one tableau to another\n'\
		+ 'q - quit\n'
		return instructions_str
	
	def stock_to_waste(self):
		""" Returns True if a card is sucessfully moved from the Stock pile to the
			Waste pile, returns False otherwise. """
		if len(self.stock_waste.stock) + len(self.stock_waste.waste) == 0:
			return False
		elif len(self.stock_waste.stock) == 0:
			self.stock_waste.waste.reverse()
			self.stock_waste.stock = self.stock_waste.waste
			self.stock_waste.waste = []
		else:
			self.stock_waste.waste.append(self.stock_waste.stock.pop())
		return True
	
	def waste_to_foundation(self):
		card = self.stock_waste.get_waste_card()
		if self.foundation.add_card(card): 
			self.stock_waste.pop_waste_card()
			return True
		return False

	def waste_to_tableau(self, column):
		""" Returns True if a card from the Waste pile is succesfully moved to a column
			on the Tableau, returns False otherwise. """
		card = self.stock_waste.get_waste_card()
		if self.tableau.add_cards_to_col([card], column):
			self.stock_waste.pop_waste_card()
			return True
		else:
			return False

	def tableau_to_tableau(self, c1, c2):
		"""
		Returns True if any card(s) are successfully moved from c1 to c2 on
		the Tableau
		Returns False otherwise. 
		"""
		c1_cards = self.flipped[c1]
		return self.add_cards_to_col(c1_cards, c2)
	
class Tableau:
	def __init__(self, cards): 
		num_col = 7
		self.unflipped = {x: cards[:x + 1] for x in range(num_col)}
		self.flipped = {x: [self.unflipped[x].pop()] for x in range(num_col)}

	def __str__(self):
		tableau_hdr = "\nTableau\n\t1 \t2 \t3 \t4 \t5 \t6 \t7 \n"
		tableau_str = ""
		for x in range(self.max_tableau_length()):
			tableau_col_str = ""
			for col in range(7):
				hidden = self.unflipped[col]
				shown = self.flipped[col]
				if len(hidden) > x:
					tableau_col_str += "\tx"
				elif len(shown) + len(hidden) > x:
					tableau_col_str += "\t" + str(shown[x-len(hidden)])
				else:
					tableau_col_str += "\t"
			tableau_str += tableau_col_str + '\n'
		return tableau_hdr + tableau_str
	
	def max_tableau_length(self):
		""" Returns the length of the longest pile on the Tableau """
		return max([len(self.flipped[x]) + len(self.unflipped[x]) for x in range(7)])

	def add_cards_to_col(self, cards, column):
		""" 
		Returns true if cards were successfully added to column on the Tableau. 
		Returns false otherwise. 
		"""
		column_cards = self.flipped[column]
		# Empty tableau column
		if len(column_cards) == 0 and cards[0].value == 13:
			column_cards.extend(cards)
			return True
		elif len(column_cards) > 0 and column_cards[-1].can_place_card(cards[0]):
			column_cards.extend(cards)
			return True
		else:
			return False

	def tableau_to_foundation(self, foundation, column):
		""" 
		Moves a card from the Tableau to the correct Foundation pile
		"""
		column_cards = self.flipped[column]
		if len(column_cards) == 0:
			return False
		if foundation.add_card(column_cards[-1]):
			column_cards.pop()
			if len(column_cards) == 0:
				self.flip_card(column)
			return True
		else:
			return False

class Foundation:
	def __init__(self):
		self.suits = {"club":[], "heart":[], 
					  "spade":[], "diamond":[]}
	
	def get_top_card(self, suit):
		stack = self.suits[suit]
		if len(stack) == 0:
			return '?'
		else:
			return self.suits[suit][-1]

	def is_finished(self):
		""" Returns whetsher the user has won the game. """
		for suit, stack in self.suits.items():
			if len(stack) != 13: 
				return False
		return True

	def add_card(self, card):
		""" Returns True if a card is successfully added to the Foundation,
			otherwise, returns False. """
		
		if not isinstance(card, Card):
			return False
		
		stack = self.suits[card.suit]
		if (len(stack) == 0 and card.rank == 'A'):
			self.suits[card.suit].append(card)
			return True
		elif len(stack) > 0 and stack[-1].is_smaller(card):
			self.suits[card.suit].append(card)
			return True
		else:
			return False

class StockWaste:
	def __init__(self, cards):
		self.stock = cards
		self.waste = []

	def pop_waste_card(self):
		""" Removes a card from the Waste pile. """
		if len(self.waste) > 0:
			return self.waste.pop()

	def get_waste_card(self):
		""" Retrieves the top card of the Waste pile. """
		if len(self.waste) > 0:
			return self.waste[-1]
		else:
			return "empty"

	def get_num_stock(self):
		""" Returns a string of the number of cards in the stock. """
		if len(self.stock) > 0:
			return str(len(self.stock)) + " card(s)"
		else:
			return "empty"