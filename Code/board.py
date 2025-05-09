import pygame
import pygame_widgets
from pygame_widgets.button import Button

# Constants
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

def initialize_buttons(screen, on_hit, on_stand):
    """
    Initializes buttons for the game.
    """
    global buttonHit, buttonStand  # Declare buttons as global to use them elsewhere
    buttonHit = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        50,  # X-coordinate of top left corner
        450,  # Y-coordinate of top left corner
        200,  # Width
        100,  # Height

        # Optional Parameters
        text='Hit',  # Text to display
        fontSize=25,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=on_hit  # Pass the function reference without importing it
    )

    buttonStand = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        300,  # X-coordinate of top left corner
        450,  # Y-coordinate of top left corner
        200,  # Width
        100,  # Height

        # Optional Parameters
        text='Stand',  # Text to display
        fontSize=25,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=on_stand  # Pass the function reference without importing it
    )
    return {
    'buttonHit': buttonHit,
    'buttonStand': buttonStand
    }


def initialize_restart_button(screen, restartGame):
    """
    Initializes the restart button for the game.
    """
    global restart_button  # Declare restart_button as global to use it elsewhere
    restart_button = Button(
        screen,  # Surface to place button on
        300,  # X-coordinate of top left corner
        450,  # Y-coordinate of top left corner
        200,  # Width
        100,  # Height
        text='Restart',
        fontSize=25,
        margin=20,
        inactiveColour=(200, 50, 0),
        hoverColour=(150, 0, 0),
        pressedColour=(0, 200, 20),
        radius=20,
        onClick = restartGame  # Pass the restart function reference
    )
    restart_button.hide()  # Hide the button initially
    return {'buttonRestart': restart_button}

def initialize_back_to_menu_button(screen, backToMenu):
    """
    Initializes the 'Back to Menu' button for the game.
    """
    global back_button  # Declare back_button as global to use it elsewhere
    back_button = Button(
        screen, 600, 500, 150, 50,  # Position and size
        text='Menu', 
        fontSize=20, 
        margin=10,
        inactiveColour=(200, 200, 0), 
        hoverColour=(150, 150, 0), 
        pressedColour=(255, 255, 0),
        radius=10, 
        onClick = backToMenu
    )
    return back_button

def draw_board(screen):
    """
    Draws the game board aesthetics.
    """
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (20, 20, SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40), 5)

def get_screen_dimensions():
    """
    Returns the screen dimensions.
    """
    return SCREEN_WIDTH, SCREEN_HEIGHT

def draw_text(text, x, y, font_size=36, color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(text_surface, (x, y))

def draw_cards(cards, card_place):
    """
    Draws the cards on the screen.
    """
    if card_place == "player_left":
        x, y = 50, 400
    elif card_place == "player_right":
        x, y = 400, 400
    elif card_place == "dealer_show":
        x, y = 400, 50
    elif card_place == "dealer_hide":
        x, y = 50, 50
    elif card_place.startswith("player_hit"):  # Handle dynamic player_hitX values
        hit_index = int(card_place.replace("player_hit", ""))  # Extract the index
        x, y = 50 + hit_index * 110, 400  # Adjust x-coordinate based on index
    else:
        raise ValueError("Invalid card_place value.")
    for i, card in enumerate(cards):
        card_text = f"{card['name']}"
        draw_text(card_text, x + i * 90, y)