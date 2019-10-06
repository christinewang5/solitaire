from card import *
import random

class Solitaire():
	def __init__(self):
		self.deck = Deck()
		self.tableau = Tableau(self.deck)
		# self.foundation = Foundation()
		# self.Stock_waste = StockWaste(deck)

	def __str__(self):
		"""
		Generates string for current status of table
		"""
		header = "Stock \t # in Waste \t\t\t\t Foundation C H S D\n" 
		# first_row = "{}  \t {} \t\t\t\t          {} {} {} {}\n".format(
		# 	self.stock_waste.get_waste(), self.stock_waste.get_num_stock(), 
		# 	self.foundation.get_top_card("club"), self.foundation.get_top_card("heart"), 
		# 	self.foundation.get_top_card("spade"), self.foundation.get_top_card("diamond"))
		# return header + first_row + str(self.tableau)
		return header + str(self.tableau)

	def get_instructions(self):
		""" 
		Provides list of commands
		"""	
		instructions_str = 'Commands: \n' \
		+ 'hw - move card from Stock to waste\n'\
		+ 'wf - move card from waste to foundation\n'\
		+ 'wt - move card from waste to tableau\n'\
		+ 'tf <num tableau> - move card from tableau to foundation\n'\
		+ 'tt <num tableau 1> <num tableau 2> - move card from one tableau to another\n'\
		+ 'q - quit\n'
		return instructions_str

class Tableau:
	def __init__(self, deck): 
		card_list = deck.get_deck()
		self.unflipped = {x: card_list[:x + 1] for x in range(7)}
		self.flipped = {x: [self.unflipped[x].pop()] for x in range(7)}

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

	def tableau_to_tableau(self, c1, c2):
		""" 
		Returns True if any card(s) are successfully moved from c1 to c2 on
		the Tableau
		Returns False otherwise. 
		"""
		c1_cards = self.flipped[c1]
		return self.add_cards_to_col(c1_cards, c2)

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