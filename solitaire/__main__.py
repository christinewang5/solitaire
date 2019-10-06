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

required_height = 60
def perform_command(c, game):
	if c == "sw":
		game.stock_to_waste()
	elif c == "wf": 
		game.waste_to_foundation()
	

def main(screen):
	game = Solitaire()
	while True:		
		screen.clear()
		screen_height, screen_width = screen.getmaxyx()

		welcome_str = '#######################  SOLITAIRE. ######################\n'
			
		command_str = "\nEnter a command (type 'h' for help): "
		output_str = welcome_str + game.get_instructions() \
					 + str(game) + command_str
		screen.addstr(0, 0, output_str)
		
		curses.echo() 
		num_lines = output_str.count('\n')
		c = screen.getstr(num_lines, 37, 15)
		c = c.lower().replace(" ", "")
		if c == 'q':
			return
		else:
			perform_command(c, game)

if __name__ == "__main__":
	wrapper(main)