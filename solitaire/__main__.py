import sys
import curses

from curses import wrapper
from curses.textpad import Textbox, rectangle
from solitaire import *

def main(screen):
	game = Solitaire()

	while not game.foundation.is_finished():
		screen.clear()
		welcome_str = '#######################  SOLITAIRE. ######################\n'	
		screen.addstr(0, 0,  welcome_str + game.get_instructions() )
		game.display(screen)
		command_str = "\nEnter a command (type 'h' for help): "
		screen.addstr(command_str)
		
		# Prepare for user input
		curses.echo() 
		c = screen.getstr(5).lower().replace(" ", "")

		if c == 'q':
			return
		elif c == 'sw':
			game.stock_to_waste()
		elif c == 'wf':
			game.waste_to_foundation()
		elif c.startswith('wt'):
			try: 
				col = int(c[-1]) - 1
				game.waste_to_tableau(col)
				continue
			except ValueError:
				continue
		elif c.startswith('tf'):
			try: 
				col = int(c[-1]) - 1
				game.tableau_to_foundation(col)
				continue
			except ValueError:
				continue
		elif c.startswith('tt'):
			try: 
				col1 = int(c[-2]) - 1
				col2 = int(c[-1]) - 1
				game.tableau_to_tableau(col1, col2)
				continue
			except ValueError:
				continue
		
if __name__ == "__main__":
	wrapper(main)
	print("\033[96m{}\033[00m" .format('Quitting Solitaire...')) 