import pygame

import pygame_widgets
from pygame_widgets.button import Button
from Blackjack import startgame  # Update the import statement
from board import initialize_board  # Import a function to initialize the board

# Set up Pygame
pygame.init()
win = pygame.display.set_mode((500, 800))

# Initialize the board (pass the screen object)
initialize_board(win)

# Creates the button with optional parameters
button = Button(
    # Mandatory Parameters
    win,  # Surface to place button on
    150,  # X-coordinate of top left corner
    50,  # Y-coordinate of top left corner
    200,  # Width
    100,  # Height

    # Optional Parameters
    text='Play',  # Text to display
    fontSize=25,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
    hoverColour=(150, 0, 0),  # Colour of button when being hovered over
    pressedColour=(0, 200, 20),  # Colour of button when being clicked
    radius = 20,  # Radius of border corners (leave empty for not curved)
    onClick = startgame  # Pass the function reference without calling it
)
run = True

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()