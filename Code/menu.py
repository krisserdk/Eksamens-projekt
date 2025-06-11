import pygame
import pygame_widgets
from pygame_widgets.button import Button
from blackjack import startgame  # Update the import statement

def stopRun():
    pygame.quit()
    quit()

def startGame():
    """
    Function to stop the game loop and exit the program.
    """
    play_button.hide()  # Hide the play button
    quit_button.hide()  # Hide the quit button
    startgame()  # Start the game
    global run
    run = False  # Stop the menu loop
    pygame.quit()
    quit()



pygame.init()
win = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Blackjack Menu")
run = True

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)

# Create buttons
play_button = Button(
    win, 
    150, 
    300, 
    200, 
    100,  # Position and size
    text='Play', 
    fontSize=25, 
    margin=20,
    inactiveColour=(0, 200, 0), 
    hoverColour=(0, 150, 0), 
    pressedColour=(0, 255, 0),
    radius=20, 
    onClick = startGame  # Pass the start function reference
)

quit_button = Button(
    win, 
    150, 
    450, 
    200, 
    100,  # Position and size
    text='Quit', 
    fontSize=25, 
    margin=20,
    inactiveColour=(200, 0, 0), 
    hoverColour=(150, 0, 0), 
    pressedColour=(255, 0, 0),
    radius=20, 
    onClick=stopRun
)

# Menu loop
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            stopRun()

    # Draw background
    win.fill(BLUE)

    # Draw title
    font = pygame.font.Font(None, 74)
    title_surface = font.render("Blackjack", True, WHITE)
    win.blit(title_surface, (125, 100))  # Center the title

    # Update buttons
    pygame_widgets.update(events)
    pygame.display.update()