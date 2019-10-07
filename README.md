# Play Solitaire In Your Console

## How to Run 
- *Important note: Terminal must be in full screen in order for game to run*
- Run `python solitaire/`in the terminal once you navigate to the correct folder
- The following commands are valid for use 
	- sw - move card from stock to waste
	- wf - move card from waste to foundation
	- wt - move card from waste to tableau
	- tf <num tableau> - move card from tableau to foundation
	- tt <num tableau 1> <num tableau 2> - move card from one tableau to another
	- q - quit the game

## External Libraries
- `curses` to handle terminal output

## Design Decisions
### Classes 
- `Card` class
- `Deck` class
- `Solitaire` which has the following fields
	- 

### Edge cases