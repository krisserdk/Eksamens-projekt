import pygame
import pygame_widgets
from pygame_widgets.button import Button

# Constants
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

def initialize_buttons(screen, on_hit):
    """
    Initializes buttons for the game.
    """
    global buttonHit  # Declare buttonHit as global to use it elsewhere
    buttonHit = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        150,  # X-coordinate of top left corner
        50,  # Y-coordinate of top left corner
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
        onClick = on_hit  # Pass the function reference without importing it
    )

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

def draw_cards(cards, card_place):
    """
    Draws the cards on the screen.
    """
    if card_place == "player_left":
        x, y = 50, 400
    elif card_place == "player_right":
        x, y = 400, 400
    elif card_place == "dealer_show":
        x, y = 50, 50
    elif card_place == "dealer_hide":
        x, y = 400, 50
    else:
        raise ValueError("Invalid card_place value.")
    for i, card in enumerate(cards):
        card_text = f"{card['name']}"
        draw_text(card_text, x + i * 90, y)

def draw_text(text, x, y, font_size=36, color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(text_surface, (x, y))