"""
nulrtown.py
Module containing the insertion point into the Nurltown game, along with configurations and utilities
"""

# Importing external modules.
# Some of the statements have the form 'import [THIS] as [THAT]', which just allows as to use
# a shorter alias (alternate name to target the module) to reduce the amount we have to type
import sys                      # Allows access to information about the computer, its filesystem, etc
import pygame as pg             # The Pygame module
import config as cfg            # The configuration file containing parameters about the game
import entities as ntts
import random as rd             # Module which has useful functions involving random numbers
import colors                   # Imports variables describing colors

def main():
    """
    This is the entry point in to the Nurltown ecosystem simulator. The function does the following:
    1. Instantiates a Pygame session
    2. Set the game configuration and utilities
    3. Populates the ecosystem with an initial collection of nurlets and food
    4. Continuously runs a loop of updating the states of the game entities and redrawing the game state
    """
 
    

# Make sure this always stays at the end of the file
# This code block ensures that the main() function (the entry point to the game) only runs if this script
# file is run directly, and not imported as a module.
if __name__ == "__main__":
    main()
    width, height = cfg.GAME_WIDTH, cfg.GAME_HEIGHT     # import the game dimensions from the configuration file
    pg.init()       # initialize the pygame module
    pg.font.init()  # initialize the font library
    
    # Create a text object to test the game loop
    test_font = pg.font.SysFont('Helvetica', 30)
    test_text = test_font.render('GAME DEVELOPMENT IN PROGRESS...', False, (255, 0, 0))
    
    screen = pg.display.set_mode((width, height))       # create a display object representing the game screen
    nurlets = pg.sprite.Group()
    hostiles = pg.sprite.Group()
    food = pg.sprite.Group()
    
    nurlet = ntts.Nurlet(width / 2, height / 2)
    entities_groups = [food, nurlets, hostiles]

    nurlets.add(nurlet)

    while True:
    
        # Handle the events that the game instance encounters
        # Events can be mouse movements/clicks, key presses, window resizing, joystick use, etc.
        # You can read more about the supported event types here:
        # https://www.pg.org/docs/ref/event.html
        for event in pg.event.get():

            # Quit the game and program when the 'x' button on the window is pressed
            if event.type == pg.QUIT: sys.exit()
            # Adds a quick way to exit the game by press the ';' button
            if event.type == pg.KEYDOWN and event.key == pg.K_SEMICOLON: sys.exit()

        # Clear the screen
        screen.fill(colors.black)

        #Redraw the entities
        for group in entities_groups:
        	group.draw(screen)

        
        # Display test text
        screen.blit(test_text, (180, 500))

        pg.display.update()