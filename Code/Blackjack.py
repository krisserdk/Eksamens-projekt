import pygame
import pygame_widgets
import random
import sys  # Import sys to exit the game loop and return to the menu
from board import *

def startgame():
    # Initialize pygame
    pygame.init()

    # Get screen dimensions from board module
    SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_dimensions()

    # Setup display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blackjack")

    # Load card images
    card_images = load_card_images()

    # Initialize buttons and pass the addCard, stand, and back_to_menu functions
    global buttons, button, back_button
    buttons = initialize_buttons(screen, addCard, stand)
    button = initialize_restart_button(screen, restartGame)  # Initialize the restart button

    game_loop(screen, card_images)

def load_card_images():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = ['ace'] + [str(i) for i in range(2, 11)] + ['jack', 'queen', 'king']
    card_images = {}
    placeholder_image = pygame.Surface((71, 96))  # Create a placeholder surface
    placeholder_image.fill((255, 255, 255))  # Fill it with white color
    pygame.draw.rect(placeholder_image, (0, 0, 0), placeholder_image.get_rect(), 1)  # Add a black border

    desired_width, desired_height = 100, 140  # Set the desired size for the card images

    for suit in suits:
        for value in values:
            card_name = f"{value}_of_{suit}"
            image_path = f"cards/{card_name}.png"  # Adjust the path to your images
            try:
                card_image = pygame.image.load(image_path)
                card_images[card_name] = pygame.transform.scale(card_image, (desired_width, desired_height))
            except FileNotFoundError:
                card_images[card_name] = pygame.transform.scale(placeholder_image, (desired_width, desired_height))
    return card_images

def create_deck():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = ['ace'] + [str(i) for i in range(2, 11)] + ['jack', 'queen', 'king']
    deck = []
    for suit in suits:
        for value in values:
            card_name = f"{value}_of_{suit}"
            card = {"value": value, "suit": suit, "name": card_name}
            deck.append(card)
    random.shuffle(deck)
    return deck

def display_hand(screen, hand, x, y, card_images, spacing=110):
    for i, card in enumerate(hand):
        card_image = card_images[card['name']]
        screen.blit(card_image, (x + i * spacing, y))

def calculate_score(hand):
    """
    Calculates the score of a hand.
    """
    score = 0
    aces = 0

    for card in hand:
        if card['value'] in ['jack', 'queen', 'king']:
            score += 10
        elif card['value'] == 'ace':
            aces += 1
            score += 11  # Initially count ace as 11
        else:
            score += int(card['value'])

    # Adjust for aces if score exceeds 21
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

def addCard():
    """
    Adds a card to the player's hand and checks for a loss.
    """
    global deck, player_hand, winner, player_turn
    if deck:
        new_card = deck.pop()
        player_hand.append(new_card)
        draw_cards(player_hand, "player_hit" + str(len(player_hand) - 1))
        if calculate_score(player_hand) > 21:
            player_turn = False  # End player's turn
            winner = "Dealer Wins!"  # Player loses if score exceeds 21
            buttons['buttonHit'].hide()  # Hide the Hit button
            buttons['buttonStand'].hide()  # Hide the Stand button
            button['buttonRestart'].show()  # Show the restart button

def stand():
    """
    Ends the player's turn, starts the dealer's turn, and determines the winner.
    """
    global player_turn, winner, dealer_hand, deck
    player_turn = False

    # Dealer's turn logic
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    # Calculate scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Determine the winner
    if dealer_score > 21 or player_score > dealer_score:
        winner = "Player Wins!"
    elif player_score == dealer_score:
        winner = "Tie!"
    else:
        winner = "Dealer Wins!"
    player_turn = False
    buttons['buttonHit'].hide()  # Hide the Hit button
    buttons['buttonStand'].hide()  # Hide the Stand button
    button['buttonRestart'].show()  # Show the restart button

def restartGame():
    """
    Restarts the game by reinitializing the game state.
    """
    global winner, player_turn, deck, player_hand, dealer_hand
    winner = None
    player_turn = True
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    button['buttonRestart'].hide()  # Hide the restart button
    buttons['buttonHit'].show()  # Show the Hit button
    buttons['buttonStand'].show()  # Show the Stand button

def game_loop(screen, card_images):
    global deck, player_hand, dealer_hand, winner, player_turn
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    running = True
    player_turn = True
    winner = None

    # Load the back of the card image
    back_image = pygame.image.load("cards/back.png")  # Adjust the path to your back image
    back = pygame.transform.scale(back_image, (100, 140))
    
    while running:
        events = pygame.event.get()  # Capture events
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if player_turn and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:  # Hit
                    player_hand.append(deck.pop())
                    if calculate_score(player_hand) > 21:
                        winner = "Dealer Wins!"
                        player_turn = False
                        buttons['buttonHit'].hide()  # Hide the Hit button
                        buttons['buttonStand'].hide()  # Hide the Stand button
                        button['buttonRestart'].show()  # Show the restart button

                elif event.key == pygame.K_s:  # Stand
                    player_turn = False
                    # Dealer's turn logic
                    while calculate_score(dealer_hand) < 17:
                        dealer_hand.append(deck.pop())
                    # Calculate scores
                    player_score = calculate_score(player_hand)
                    dealer_score = calculate_score(dealer_hand)
                    # Determine the winner
                    if dealer_score > 21 or player_score > dealer_score:
                        winner = "Player Wins!"
                    elif player_score == dealer_score:
                        winner = "Tie!"
                    else:
                        winner = "Dealer Wins!"
                    buttons['buttonHit'].hide()  # Hide the Hit button
                    buttons['buttonStand'].hide()  # Hide the Stand button
                    button['buttonRestart'].show()  # Show the restart button

        # Draw the board aesthetics from board.py
        draw_board(screen)

        # Display game information on top of the board
        draw_text("Player's Hand:", 50, 250)
        display_hand(screen, player_hand, 50, 280, card_images)

        draw_text("Dealer's Hand:", 50, 50)
        # Display the dealer's hand
        if player_turn:  # If it's still the player's turn, hide the dealer's first card
            screen.blit(back, (50, 80))  # Show the back of the first card
            screen.blit(card_images[dealer_hand[1]['name']], (160, 80))  # Show the second card
        else:  # Reveal the dealer's full hand
            display_hand(screen, dealer_hand, 50, 80, card_images)

        # Display scores
        draw_text(f"{calculate_score(player_hand)}", 230, 250)
        if not player_turn:  # Only show the dealer's score after the player's turn ends
            draw_text(f"{calculate_score(dealer_hand)}", 230, 50)

        # Display winner text
        if winner:
            if winner == "Dealer Wins!":
                draw_text("LOSER", 100, 475, font_size=50, color=(255, 0, 0))
            elif winner == "Player Wins!":
                draw_text("WINNER", 100, 475, font_size=50, color=(0, 255, 0))
            elif winner == "Tie!":
                draw_text("TIE", 125, 475, font_size=50, color=(255, 255, 0))
            else:
                draw_text("Error", 100, 475, font_size=50, color=(255, 0, 0))

        # Update buttons
        pygame_widgets.update(events)  # Ensure the button is updated

        pygame.display.flip()

    pygame.quit()
