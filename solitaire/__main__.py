import curses

from curses import wrapper
from curses.textpad import Textbox, rectangle
from solitaire import * 

required_height = 60
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
		if c == 'q':
			return


if __name__ == "__main__":
	wrapper(main)