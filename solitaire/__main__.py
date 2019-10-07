import sys
import curses

from curses import wrapper
from curses.textpad import Textbox, rectangle
from solitaire import *

# instructions_str = 'Commands: \n' \
# 		+ 'sw - move card from stock to waste\n'\
# 		+ 'wf - move card from waste to foundation\n'\
# 		+ 'wt - move card from waste to tableau\n'\
# 		+ 'tf <num tableau> - move card from tableau to foundation\n'\
# 		+ 'tt <num tableau 1> <num tableau 2> - move card from one tableau to another\n'\
# 		+ 'q - quit\n'

def main(screen):
	game = Solitaire()

	while not game.foundation.is_finished():
		welcome_str = '#######################  SOLITAIRE. ######################\n'
			
		command_str = "\nEnter a command (type 'h' for help): "
		output_str = welcome_str + game.get_instructions() \
					 + str(game) + command_str
		screen.addstr(0, 0, output_str)
		
		curses.echo() 
		screen.refresh()
		num_lines, _ = screen.getyx()
		c = screen.getstr(num_lines, 37, 5).lower().replace(" ", "")

		if c == 'q':
			return
		elif c == 'sw':
			game.stock_to_waste()
		elif c == 'wf':
			game.waste_to_foundation()
		elif c.startswith('wt'):
			try: 
				col = int(c[-1])
				game.waste_to_tableau(col)
				continue
			except ValueError:
				continue
		y, x = screen.getyx()
		screen.addstr(y, x, '')
		screen.refresh()

if __name__ == "__main__":
	wrapper(main)