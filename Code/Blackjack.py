import pygame
import random
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

    # Game assets and variables (example deck, hands, etc.)
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Font for text
    font = pygame.font.Font(None, 36)

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

def calculate_score(hand):
    # Simplified scoring: Convert face cards to 10, ace logic can be added
    score = 0
    aces = 0
    for card in hand:
        if card["value"] in ['jack', 'queen', 'king']:
            score += 10
        elif card["value"] == 'ace':
            score += 1
            aces += 1
        else:
            score += int(card["value"])
    # Adjust for ace (if possible to use as 11)
    while aces > 0 and score + 10 <= 21:
        score += 10
        aces -= 1
    return score

def display_hand(screen, hand, x, y, card_images, spacing=90):
    for i, card in enumerate(hand):
        card_image = card_images[card['name']]
        screen.blit(card_image, (x + i * spacing, y))

def cardHit():
    draw_text("Hit", 150, 50)

def game_loop(screen, card_images):
    global deck, player_hand, dealer_hand
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    running = True
    player_turn = True
    winner = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if player_turn and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:  # Hit
                    player_hand.append(deck.pop())
                    if calculate_score(player_hand) > 21:
                        winner = "Dealer Wins!"
                        player_turn = False

                elif event.key == pygame.K_s:  # Stand
                    player_turn = False

        # Dealer's turn after player stands
        if not player_turn and winner is None:
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)
            if dealer_score > 21 or player_score > dealer_score:
                winner = "Player Wins!"
            elif player_score == dealer_score:
                winner = "Tie!"
            else:
                winner = "Dealer Wins!"

        # Draw the board aesthetics from board.py
        draw_board(screen)

        # Display game information on top of the board
        draw_text("Player's Hand:", 50, 50)
        display_hand(screen, player_hand, 50, 80, card_images)

        draw_text("Dealer's Hand:", 50, 250)
        display_hand(screen, dealer_hand, 50, 280, card_images)

        if winner:
            draw_text(winner, 300, 500)

        pygame.display.flip()

    pygame.quit()



